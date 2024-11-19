#!/usr/bin/env python3

# Function to load shipment data from a file
def load_shipment_data(filename):
    stores = set()
    shipments = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Store:"):
                # Parse the list of stores
                store_list = line.replace("Store: ", "").split(", ")
                stores.update(store_list)
            elif "->" in line:
                # Parse each shipment entry
                route_id, path = line.split(": ")
                sender, receiver = path.split(" -> ")
                shipments.append((sender, receiver))
    
    return stores, shipments

# Function to calculate the number of exports and imports for each store
def calculate_exports_imports(shipments):
    exports = {}
    imports = {}

    # Count exports and imports for each store
    for sender, receiver in shipments:
        exports[sender] = exports.get(sender, 0) + 1
        imports[receiver] = imports.get(receiver, 0) + 1

    # Find the store with the most exports and most imports
    max_export_store = max(exports, key=exports.get)
    max_import_store = max(imports, key=imports.get)

    return max_export_store, exports[max_export_store], max_import_store, imports[max_import_store]

# Load shipment data from text file
stores, shipments = load_shipment_data("shipments.txt")

# Calculate exports and imports
max_export_store, max_exports, max_import_store, max_imports = calculate_exports_imports(shipments)

# Print the result
print(f"Export: {max_export_store} ({max_exports})")
print(f"Import: {max_import_store} ({max_imports})")
