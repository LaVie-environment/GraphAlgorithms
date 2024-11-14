#!/usr/bin/env python3

from collections import defaultdict

def find_unvisited_cities(desired_places, routes):
    # Create sets for easier lookup
    desired_places_set = set(desired_places)
    
    # Build graph from routes
    graph = defaultdict(set)
    for route in routes.values():
        for i in range(len(route) - 1):
            city1, city2 = route[i], route[i + 1]
            graph[city1].add(city2)
            graph[city2].add(city1)

    # Find unvisited cities
    unvisited_cities = []
    for place in desired_places_set:
        if place not in graph:
            unvisited_cities.append(place)
        else:
            visited_neighbors = set()
            for neighbor in graph[place]:
                visited_neighbors.add(neighbor)
            
            if len(visited_neighbors) == 0:
                unvisited_cities.append(place)
            elif len(graph[place]) != len(visited_neighbors):
                unvisited_cities.append(place)

    return sorted(unvisited_cities)


# Input data
desired_places = ["Prague", "Berlin", "Rome", "Paris", "Vienna", "London", "Brno"]
routes = {
    "2018": ["Prague", "Berlin", "Paris", "Prague"],
    "2019": ["Prague", "London", "Paris", "Vienna"],
    "2020": ["Vienna", "London", "Paris", "Berlin"],
    "2021": ["Prague", "Paris", "Vienna"]
}

# Find unvisited cities
unvisited_cities = find_unvisited_cities(desired_places, routes)

print("Cities that would be beneficial to visit:")
for city in unvisited_cities:
    print(", ".join(map(str, unvisited_cities)))