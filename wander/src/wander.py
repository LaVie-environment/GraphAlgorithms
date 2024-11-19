#!/usr/bin/env python3

# Function to load routes from a file
def load_routes_from_file(filename):
    routes = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Remove newline characters and extra spaces
            if ": " in line:  # Ensure the line has the correct format
                route_id, path = line.split(": ")
                signposts = path.split(" -> ")
                routes[route_id] = signposts
    return routes

# Function to find lost signposts where tourists got lost
def find_lost_signposts(routes):
    lost_signposts = set()  # Set to store unique lost signposts
    
    for route_id in routes:
        route = routes[route_id]
        for i in range(1, len(route)):
            # Check if the current signpost is the same as the previous one
            if route[i] == route[i - 1]:
                lost_signposts.add(route[i])
    
    return sorted(lost_signposts)  # Sort for consistent output

# Load routes from text file
routes = load_routes_from_file("routes.txt")

# Find and print lost signposts
lost_signposts = find_lost_signposts(routes)

print("The output is a list of signposts where tourists got lost")
print(", ".join(lost_signposts))
