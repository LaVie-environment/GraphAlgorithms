#!/usr/bin/env python3

# Step 1: Load data from file and create the graph
def load_group_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    group = []
    for line in lines:
        line = line.strip()
        if "-" in line:
            friend1, friend2 = line.split(" - ")
            group.append((friend1, friend2))
    return group

# Step 2: Create the graph from the group
def create_graph(group):
    graph = {}
    all_individuals = set()

    for friend1, friend2 in group:
        if friend1 not in graph:
            graph[friend1] = []
        if friend2 not in graph:
            graph[friend2] = []
        graph[friend1].append(friend2)
        graph[friend2].append(friend1)
        all_individuals.update([friend1, friend2])

    # Include all individuals in the graph even if they have no direct friends
    for person in all_individuals:
        if person not in graph:
            graph[person] = []

    return graph

# Step 3: Calculate direct reachability for each person
def calculate_reachability(graph, person):
    visited = [person]
    queue = [person]
    reachability_count = 0  # Direct friends count

    while queue:
        current = queue.pop(0)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
        reachability_count = len(graph[person])  # Direct friends only

    return reachability_count

# Step 4: Find the top 3 individuals by reachability count
def find_top_distributors(graph):
    reachability = {}
    for person in graph:
        reachability[person] = calculate_reachability(graph, person)

    # Sort by reachability count in descending order and pick the top 3
    top_distributors = sorted(reachability.items(), key=lambda item: (-item[1], item[0]))
    return top_distributors[:3]

# Load the group data from file and create graph
group = load_group_from_file("friends.txt")
graph = create_graph(group)

# Find and print the top 3 distributors
top_distributors = find_top_distributors(graph)

print("List of three people to visit and how many people they can deliver tickets to:")
for person, reachability in top_distributors:
    print(f"{person} ({reachability})")
