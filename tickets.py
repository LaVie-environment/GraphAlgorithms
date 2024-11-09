from collections import deque, defaultdict

# Step 1: Create the graph from the friendships
def create_graph(friendships):
    graph = defaultdict(list)
    for friend1, friend2 in friendships:
        graph[friend1].append(friend2)
        graph[friend2].append(friend1)
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
                
    return len(visited) - 1  # Exclude the start node itself

# Step 3: Find the top 3 individuals who can reach the most people
def find_top_distributors(graph):
    reachability = {person: bfs_reachability(graph, person) for person in graph}
    # Sort by reachability count in descending order and pick the top 3
    top_distributors = sorted(reachability, key=reachability.get, reverse=True)[:3]
    return top_distributors, {person: reachability[person] for person in top_distributors}

# Input data
friendships = [
    ("Honza", "Pepa"),
    ("Jarek", "Anna"),
    ("Anna", "Tomas"),
    ("Honza", "Tomas")
]

# Step 4: Execute the functions to get the result
graph = create_graph(friendships)
top_distributors, reachability_counts = find_top_distributors(graph)

# Output the results
print("Top 3 friends to distribute tickets to maximize reachability:")
for person in top_distributors:
    print(f"{person} can reach {reachability_counts[person]} people")
