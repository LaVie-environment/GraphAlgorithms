#!/usr/bin/env python3

from collections import deque

def breadth_first_print(graph, source):
    queue = deque([source])
    while queue:
        current = queue.popleft()
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

breadth_first_print(graph, 'a')
