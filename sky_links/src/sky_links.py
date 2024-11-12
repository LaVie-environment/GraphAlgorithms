#!/usr/bin/env python3

from collections import defaultdict

# Step 1: Define the input data
routes = {
    "LS2021": ["Prague", "Berlin", "Paris", "Prague"],
    "ZS2020": ["Prague", "London", "Paris", "Vienna"],
    "AB111": ["Vienna", "London", "Paris", "Berlin"],
    "XYZ007": ["Prague", "Paris", "Vienna"]
}

# Step 2: Build the graph
graph = defaultdict(list)
for route in routes.values():
    for i in range(len(route) - 1):
        start, end = route[i], route[i + 1]
        graph[start].append(end)

# Step 3: Function to check for an alternative path (including indirect connections)
def has_alternative_path(graph, start, end):
    # Helper function to perform DFS
    def dfs(city, target, visited):
        if city == target:
            return True
        visited.add(city)
        for neighbor in graph[city]:
            if neighbor not in visited and dfs(neighbor, target, visited):
                return True
        return False

    return dfs(start, end, set())

# Step 4: Test specific routes for redundancy
redundant_routes = []
test_routes = [("London", "Paris"), ("Paris", "Vienna")]

for city, destination in test_routes:
    if has_alternative_path(graph, city, destination):
       redundant_routes.append(f"{city} -> {destination}")

# Output the redundant routes
print("The output is a list of connections between cities that are in addition:")
for route in redundant_routes:
    print(route)