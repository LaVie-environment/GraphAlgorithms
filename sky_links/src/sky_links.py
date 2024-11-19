#!/usr/bin/env python3

# Step 1: Load data from file and parse routes
def load_routes_from_file(filename):
    routes = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if ":" in line and "->" in line:
                route_name, path = line.split(": ")
                cities = path.split(" -> ")
                routes[route_name.strip()] = cities
    return routes

# Step 2: Build the graph of direct connections
def build_graph(routes):
    graph = {}
    for route in routes.values():
        for i in range(len(route) - 1):
            start, end = route[i], route[i + 1]
            if start not in graph:
                graph[start] = []
            if end not in graph[start]:
                graph[start].append(end)
    return graph

# Step 3: Check for alternative paths using Depth-First Search (DFS)
def has_alternative_path(graph, start, end):
    def dfs(city, target, visited):
        if city == target:
            return True
        visited.add(city)
        for neighbor in graph.get(city, []):
            if neighbor not in visited and dfs(neighbor, target, visited):
                return True
        return False
    return dfs(start, end, set())

# Step 4: Identify redundant connections based on alternative paths
def find_redundant_connections(graph, connections_to_test):
    redundant_routes = []
    for city, destination in connections_to_test:
        if has_alternative_path(graph, city, destination):
            redundant_routes.append(f"{city} -> {destination}")
    return redundant_routes

# Load routes from file and create the graph
routes = load_routes_from_file("routes.txt")
graph = build_graph(routes)

# Define connections to check
connections_to_test = [("London", "Paris"), ("Paris", "Vienna")]

# Identify and print redundant connections
redundant_routes = find_redundant_connections(graph, connections_to_test)

# Output results
print("The output is a list of connections between cities that are in addition:")
for route in redundant_routes:
    print(route)
