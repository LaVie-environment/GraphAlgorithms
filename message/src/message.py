#!/usr/bin/env python3

input_file = "network_data.txt"

def create_graph(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            # Parse each line
            parts = line.strip().split(": ")
            people = parts[0].split(" - ")
            time = int(parts[1])
            person1, person2 = people[0], people[1]
            
            if person1 not in graph:
                graph[person1] = []
            if person2 not in graph:
                graph[person2] = []
            
            graph[person1].append((person2, time))
            graph[person2].append((person1, time))
    return graph


def calculate_message_times(graph, start):
    import heapq

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_time, current_person = heapq.heappop(priority_queue)

        for neighbor, time_to_meet in graph[current_person]:
            new_time = current_time + time_to_meet
            if new_time < distances[neighbor]:
                distances[neighbor] = new_time
                heapq.heappush(priority_queue, (new_time, neighbor))
    
    return distances

def main():
    graph = create_graph(input_file)
    message_times = calculate_message_times(graph, "You")
    
    sorted_message_times = sorted(message_times.items(), key=lambda x: x[1])
    print("List of members in order of message receipt and time of receipt:")
    for person, time in sorted_message_times:
        print(f"{person}: {time}")

# Run the program
if __name__ == "__main__":
    main()
