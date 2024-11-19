#!/usr/bin/env python3

# Function to load tours from a file
def load_tours_from_file(filename):
    tours_upper = set()
    tours_lower = set()

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if "->" in line:  # Process only tour lines with the format "City -> City"
                # Check if the tour is in uppercase or lowercase
                if line.isupper():
                    tours_upper.add(line)
                else:
                    tours_lower.add(line)

    return tours_upper, tours_lower

# Function to filter unique tours based on uppercase priority
def get_unique_tours(tours_upper, tours_lower):
    # Retain only lowercase tours that do not have an uppercase equivalent
    unique_tours = tours_upper.union({tour for tour in tours_lower if tour.upper() not in tours_upper})
    # Sort for consistent output
    return sorted(unique_tours)

# Load tours from the text file
tours_upper, tours_lower = load_tours_from_file("tours.txt")

# Get the list of unique tours
unique_tours = get_unique_tours(tours_upper, tours_lower)

# Print the output
print("The new offer of tours is:")
for tour in unique_tours:
    print(tour)

