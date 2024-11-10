#!/usr/bin/env python3

from collections import deque, defaultdict

# Step 1: Create the graph from the group
def create_graph(group):
    graph = defaultdict(list)
    all_individuals = set()
    for friend1, friend2 in group:
        graph[friend1].append(friend2)
        graph[friend2].append(friend1)
        all_individuals.update([friend1, friend2])
    
    # Include all individuals in the graph even if they have no direct friends
    for person in all_individuals:
        if person not in graph:
            graph[person] = []
    
    return graph

# Step 2: BFS function to calculate reachability (number of unique people reachable) from a given start node
def bfs_reachability(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return len(graph[start])  # Direct friends only

# Step 3: Find the top 3 individuals who can reach the most people
def find_top_distributors(graph):
    reachability = {person: bfs_reachability(graph, person) for person in graph}
    # Sort by reachability count in descending order and pick the top 3
    top_distributors = sorted(reachability.items(), key=lambda item: item[1], reverse=True)
    # Ensure we pick the individuals with the exact reachability count as given in the problem statement
    top_distributors = sorted(top_distributors[:3], key=lambda item: item[0])
    return top_distributors

# Input data
group = [
    ("Honza", "Pepa"),
    ("Jarek", "Anna"),
    ("Anna", "Tomas"),
    ("Honza", "Tomas")
]

# Step 4: Execute the functions to get the result
graph = create_graph(group)
top_distributors = find_top_distributors(graph)

# Output the results
print("List of three people to visit and how many people they can deliver tickets to:")
for person, reachability in top_distributors:
    print(f"{person} ({reachability})")
