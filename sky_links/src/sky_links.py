#!/usr/bin/env python3

from collections import defaultdict

# Step 1: Define cities and routes data
cities = ["Prague", "Berlin", "Paris", "Vienna", "London"]
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
        if end not in graph[start]:
            graph[start].append(end)

# Function to check if a path exists between two cities without using a direct edge
def has_alternative_path(graph, start, end, exclude_edge):
    visited = set()
    stack = [start]
    while stack:
        city = stack.pop()
        if city == end:
            return True
        if city not in visited:
            visited.add(city)
            for neighbor in graph[city]:
                # Skip the excluded edge to check for alternative path
                if (city, neighbor) != exclude_edge:
                    stack.append(neighbor)
    return False

# Step 3: Find redundant routes
redundant_routes = []
for city in graph:
    for destination in graph[city]:
        # Check for alternative path from city to destination without using the direct edge
        if has_alternative_path(graph, city, destination, (city, destination)):
            redundant_routes.append(f"{city} -> {destination}")

# Output the redundant routes
print("Redundant Routes:")
for route in redundant_routes:
    print(route)
