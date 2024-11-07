#!/usr/bin/env python3

def depth_first_print(graph, source):
    list = [source]
    while list:
        current = list.pop()
        print(current)

        for neighbor in graph[current]:
            list.append(neighbor)

graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depth_first_print(graph, 'a')
