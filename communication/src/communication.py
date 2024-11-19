#!/usr/bin/env python3

# Function to load employees and communication data from a file
def load_communication_data(filename):
    employees = set()
    communication = {}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Employ:"):
                # Parse the list of employees
                employee_list = line.replace("Employ: ", "").split(", ")
                employees.update(employee_list)
                # Initialize communication dictionary for each employee
                for emp in employee_list:
                    communication[emp] = set()
            elif "->" in line:
                # Parse each communication entry
                sender, receiver = line.split(" -> ")
                if sender in communication:
                    communication[sender].add(receiver)
    
    return employees, communication

# Function to find missing communication channels
def find_missing_communication(communication):
    missing_communication = []

    # Check for unreciprocated communication
    for sender in communication:
        for receiver in communication[sender]:
            if sender not in communication.get(receiver, set()):
                missing_communication.append(f"{receiver} -> {sender}")

    return sorted(missing_communication)

# Load data from the text file
employees, communication = load_communication_data("communication.txt")

# Find and print missing communication channels
missing_channels = find_missing_communication(communication)

print("The output is a list of missing communication channels.")
print(", ".join(missing_channels))
