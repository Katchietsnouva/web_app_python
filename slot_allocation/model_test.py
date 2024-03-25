# Create an instance of SlotAssignmentModel

from models.Parking_slots_assignment_model import SlotAssignmentModel



import json
import os

# Define the file path
file_path = 'model_test.json'

# Create an instance of SlotAssignmentModel
assignment = SlotAssignmentModel("SLOT-017", [
    {"from": "2024-02-16 19:35", "to": "2024-02-23 20:57", "customer_number": "CUST-1"},
    {"from": "2024-03-18 17:43", "to": "2024-03-20 18:05", "customer_number": "CUST-10"}
])

# Convert the instance to a dictionary
assignment_dict = assignment.to_dict()

# Save the dictionary to a JSON file
with open(file_path, 'w') as json_file:
    json.dump(assignment_dict, json_file, indent=4)

# Confirm the file location
print(f"JSON file saved to: {os.path.abspath(file_path)}")

print(assignment_dict)