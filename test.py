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
    },
    {
        "user_id": "cf80c157-67ba-4673-a75b-2f9fec622f0b",
        "customer_number": "CUST-2",
        "booking_id": "Book_id-003",
        "arrival_date": "2024-02-20",
        "arrival_time": "02:10",
        "departure_date": "2024-02-24",
        "departure_time": "02:10",
        "duration_minutes": 5760
    },
    {
        "user_id": "d4365c4c-ff32-448a-b14c-a318e3b41675",
        "customer_number": "CUST-1",
        "booking_id": "Book_id-004",
        "arrival_date": "2024-02-29",
        "arrival_time": "02:10",
        "departure_date": "2024-03-02",
        "departure_time": "02:10",
        "duration_minutes": 2880
    },
    {
        "user_id": "d4365c4c-ff32-448a-b14c-a318e3b41675",
        "customer_number": "CUST-1",
        "booking_id": "Book_id-004-ext",
        "arrival_date": "2024-02-29",
        "arrival_time": "02:10",
        "departure_date": "2024-03-02",
        "departure_time": "02:16",
        "duration_minutes": 2
    },
    {
        "user_id": "d4365c4c-ff32-448a-b14c-a318e3b41675",
        "customer_number": "CUST-1",
        "booking_id": "Book_id-005",
        "arrival_date": "2024-02-20",
        "arrival_time": "02:10",
        "departure_date": "2024-02-22",
        "departure_time": "02:16",
        "duration_minutes": 2885
    },
    {
        "user_id": "dd8c0e44-de40-49e8-8e07-de86398241f6",
        "customer_number": "CUST-3",
        "booking_id": "Book_id-006",
        "arrival_date": "2024-02-19",
        "arrival_time": "19:00",
        "departure_date": "2024-02-23",
        "departure_time": "21:59",
        "duration_minutes": 5939
    },
    {
        "user_id": "d4365c4c-ff32-448a-b14c-a318e3b41675",
        "customer_number": "CUST-1",
        "booking_id": "Book_id-005-ext",
        "arrival_date": "2024-02-20",
        "arrival_time": "02:10",
        "departure_date": "2024-02-22",
        "departure_time": "02:18",
        "duration_minutes": 2
    },
    {
        "user_id": "d4365c4c-ff32-448a-b14c-a318e3b41675",
        "customer_number": "CUST-1",
        "booking_id": "Book_id-005-ext-ext",
        "arrival_date": "2024-02-20",
        "arrival_time": "02:10",
        "departure_date": "2024-02-22",
        "departure_time": "02:25",
        "duration_minutes": 2
    },
    {
        "user_id": "d4365c4c-ff32-448a-b14c-a318e3b41675",
        "customer_number": "CUST-1",
        "booking_id": "Book_id-005-ext-ext-ext",
        "arrival_date": "2024-02-20",
        "arrival_time": "02:10",
        "departure_date": "2024-02-22",
        "departure_time": "02:28",
        "duration_minutes": 3
    }
    # Add more bookings here...
]

# Generate parking slot assignments
parking_assignments = assign_parking_slot(bookings)

# Print the parking slot assignments
print(parking_assignments)
