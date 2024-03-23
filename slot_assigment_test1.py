import datetime

def convert_to_unix(date_str, time_str):
    dt = datetime.datetime.strptime(date_str + ' ' + time_str, '%Y-%m-%d %H:%M')
    return int(dt.timestamp())

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

# Sample booking data
bookings = [
    {
        "user_id": "d4365c4c-ff32-448a-b14c-a318e3b41675",
        "customer_number": "CUST-1",
        "booking_id": "Book_id-001",
        "arrival_date": "2024-02-07",
        "arrival_time": "04:00",
        "departure_date": "2024-02-09",
        "departure_time": "03:00",
        "duration_minutes": 2820
    },
    {
        "user_id": "d4365c4c-ff32-448a-b14c-a318e3b41675",
        "customer_number": "CUST-1",
        "booking_id": "Book_id-002",
        "arrival_date": "2024-02-08",
        "arrival_time": "02:10",
        "departure_date": "2024-02-20",
        "departure_time": "06:10",
        "duration_minutes": 17520
    }
]

# Generate parking slot assignments
parking_assignments = assign_parking_slot(bookings)

# Print the parking slot assignments
print(parking_assignments)
