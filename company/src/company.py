#!/usr/bin/env python3

# Function to load employees and project data from a file
def load_data_from_file(filename):
    employees = set()
    projects = {}
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Employee:"):
                # Parse the list of employees
                employee_list = line.replace("Employee: ", "").split(", ")
                employees.update(employee_list)
            elif ": " in line:
                # Parse each project and the list of its solvers
                project_id, solvers = line.split(": ")
                projects[project_id] = solvers.split(", ")
    
    return employees, projects

# Function to check if any pair of employees worked together
def has_worked_together(projects):
    collaborations = set()  # Store unique pairs of employees who worked together
    
    for solvers in projects.values():
        for i in range(len(solvers)):
            for j in range(i + 1, len(solvers)):
                # Create a sorted tuple to represent an undirected pair
                pair = tuple(sorted((solvers[i], solvers[j])))
                if pair in collaborations:
                    # If the pair already exists, return True
                    return True
                collaborations.add(pair)
    
    return False  # If no pairs are repeated, return False

# Load data from the text file
employees, projects = load_data_from_file("projects.txt")

# Check if any two employees have worked together
goal_met = has_worked_together(projects)

# Output the result
print("The output is information if the requirement is met")
print("Goal:", goal_met)
