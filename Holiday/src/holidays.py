#!/usr/bin/env python3

# Step 1: Load data from file and parse into desired places and routes
def load_data_from_file(filename):
    with open(filename, 'r') as file:
        desired_places = []
        routes = {}
        for line in file:
            line = line.strip()
            if line.startswith("Places:"):
                # Parse list of cities
                desired_places = [place.strip() for place in line.split(":")[1].split(",")]
            elif ":" in line and "->" in line:
                # Parse routes for each line
                route_name, path = line.split(": ")
                cities = [city.strip() for city in path.split("->")]
                routes[route_name.strip()] = cities
    return desired_places, routes

# Step 2: Find cities that were not visited in any route
def find_unvisited_cities(desired_places, routes):
    # Collect all visited cities
    visited_cities = set()
    for route in routes.values():
        visited_cities.update(route)
    
    # Identify unvisited cities by comparing to desired places
    unvisited_cities = [city for city in desired_places if city not in visited_cities]
    return sorted(unvisited_cities)

# Load data from file
desired_places, routes = load_data_from_file("routes.txt")

# Find unvisited cities
unvisited_cities = find_unvisited_cities(desired_places, routes)

# Output results
print("Cities that would be beneficial to visit:")
print(", ".join(unvisited_cities))
