#!/usr/bin/env python3

# Step 1: Read the input data from a text file
def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Parse nodes
    nodes_line = lines[0].strip()
    nodes = nodes_line.split(":")[1].strip().split(", ")

    # Parse edges
    edges = []
    for line in lines[2:]:
        parts = line.strip().split(":")
        connection = parts[0].strip()
        weight = int(parts[1].strip())
        node1, node2 = connection.split(" - ")
        edges.append((node1.strip(), node2.strip(), weight))

    return nodes, edges

# Step 2: Implement Kruskal's Algorithm
def kruskal(nodes, edges):
    # Sort edges by weight
    edges = sorted(edges, key=lambda edge: edge[2])
    
    # Union-Find (Disjoint Set) Helper Functions
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}
    
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])  # Path compression
        return parent[node]
    
    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
    
    # Kruskal's MST Algorithm
    mst = []
    for node1, node2, weight in edges:
        if find(node1) != find(node2):  # If it doesn't form a cycle
            union(node1, node2)
            mst.append((node1, node2))
    
    return mst

# Step 3: Main function to integrate the steps
def main():
    # Read data from the file
    file_path = "mars_connections.txt"
    nodes, edges = read_input(file_path)

    # Get the Minimum Spanning Tree
    mst = kruskal(nodes, edges)

    # Sort MST connections alphabetically for deterministic output
    mst = sorted(mst)

    # Output the result
    print("Output of a list of activated lines:")
    for node1, node2 in mst:
        print(f"{node1} - {node2}")

# Run the main function
if __name__ == "__main__":
    main()
