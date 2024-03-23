import json
import datetime

def convert_to_unix(date_str, time_str):
    dt = datetime.datetime.strptime(date_str + ' ' + time_str, '%Y-%m-%d %H:%M')
    return int(dt.timestamp())

def convert_to_datetime(unix_timestamp):
    return datetime.datetime.fromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M')

def assign_parking_slot(bookings):
    parking_slots_BOOK_ASSIGNMENTS = []
    slot_counter = 1

    for booking in bookings:
        arrival_unix = convert_to_unix(booking["arrival_date"], booking["arrival_time"])
        departure_unix = convert_to_unix(booking["departure_date"], booking["departure_time"])

        assigned = False
        for slot_assignment in parking_slots_BOOK_ASSIGNMENTS:
            slot_id = slot_assignment["slot_id"]
            occupied = False
            for time_range in slot_assignment["time_occupied"]:
                if not (departure_unix <= time_range[0] or arrival_unix >= time_range[1]):
                    occupied = True
                    break
            if not occupied:
                slot_assignment["time_occupied"].append((arrival_unix, departure_unix))
                assigned = True
                break

        if not assigned:
            parking_slots_BOOK_ASSIGNMENTS.append({"slot_id": f"SLOT-{str(slot_counter).zfill(3)}", "time_occupied": [(arrival_unix, departure_unix)]})
            slot_counter += 1

    return parking_slots_BOOK_ASSIGNMENTS

# Load data from JSON file
with open('user_data/global_users_data/time_data.json', 'r') as file:
    bookings = json.load(file)

# Generate parking slot assignments
parking_assignments = assign_parking_slot(bookings)

# Print the parking slot assignments in human-readable format
for assignment in parking_assignments:
    print(f"Slot ID: {assignment['slot_id']}")
    print("Time Occupied:")
    for time_range in assignment['time_occupied']:
        print(f"  - From: {convert_to_datetime(time_range[0])}, To: {convert_to_datetime(time_range[1])}")
    print()
