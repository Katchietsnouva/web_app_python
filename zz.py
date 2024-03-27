def assign_parking_slot(self, bookings):
    TO_BE_APPENDED_TO_parking_slots_BOOK_ASSIGNMENTS = []
    with open('user_data/global_users_data/slots.json', 'r') as file:
        parking_slots_BOOK_ASSIGNMENTS = json.load(file)

    available_slots = [slot for slot in self.get_all_parking_slots_available_data() if slot['available_for_use']]
    print("Available slots:", available_slots)

    if not available_slots:
        return None, "No available slots at the moment. Please try again later."

    print("Bookings:", bookings)

    # Process booking and obtain arrival_unix, departure_unix, customer_number
    arrival_unix = self.convert_to_unix(bookings["arrival_date"], bookings["arrival_time"])
    departure_unix = self.convert_to_unix(bookings["departure_date"], bookings["departure_time"])
    customer_number = bookings["customer_number"]
    print(f"The customer number that we want to assign a slot is {customer_number}")

    assigned = False

    for slot in available_slots:
        parking_slot_id = slot["parking_slot_id"]
        print("Parking slot id:", parking_slot_id)
        occupied = False

        for slot_assignment in parking_slots_BOOK_ASSIGNMENTS:
            for time_range in slot_assignment["time_occupied_data"]:
                from_unix = self.convert_to_unix_eq2(time_range['from'])
                to_unix = self.convert_to_unix_eq2(time_range['to'])

                if not (arrival_unix >= to_unix or departure_unix <= from_unix):
                    print("Booking overlaps with existing time range.")
                    occupied = True
                    break

            if not occupied:
                print("Booking does not overlap with existing time ranges.")
                TO_BE_APPENDED_TO_parking_slots_BOOK_ASSIGNMENTS.append({
                    "parking_slot_id": parking_slot_id,
                    "time_occupied_data": [(arrival_unix, departure_unix, customer_number)]
                })
                assigned = True
                break

        if assigned:
            break

    if not assigned:
        print("All available slots are occupied.")
        return None, "All available slots are occupied."

    print("Almost exiting the equation")
    print(TO_BE_APPENDED_TO_parking_slots_BOOK_ASSIGNMENTS)
    return TO_BE_APPENDED_TO_parking_slots_BOOK_ASSIGNMENTS
























def assign_parking_slot(self, bookings):
        TO_BE_APPENDED_TO_parking_slots_BOOK_ASSIGNMENTS = []
        with open('user_data/global_users_data/slots.json', 'r') as file:
            parking_slots_BOOK_ASSIGNMENTS = json.load(file)
        slot_counter = 1
        available_slots = self.get_all_parking_slots_available_data()
        available_slots = [slot for slot in self.get_all_parking_slots_available_data() if slot['available_for_use']]
        print(available_slots)
        if not available_slots:
            return None, "No available slots at the moment. Please try again later."

        # for booking in bookings:
        print("initiallisasation of debug")
        print("lets print already existing data in parking_slots_BOOK_ASSIGNMENTS below ")
        print(parking_slots_BOOK_ASSIGNMENTS)
        print("data of new record to be asigned a unique slot below")
        print(bookings)
        print("to test if new data has data lets print its arrival_date below")
        print(bookings["arrival_date"])

        

        # Process booking and obtain arrival_unix, departure_unix, customer_number
        arrival_unix = self.convert_to_unix(bookings["arrival_date"], bookings["arrival_time"])
        departure_unix = self.convert_to_unix(bookings["departure_date"], bookings["departure_time"])
        customer_number = bookings["customer_number"]
        print(f" the cutomer number that we want to assing a slot is {customer_number}")

        assigned = False        
        for slot_assignment in parking_slots_BOOK_ASSIGNMENTS:
        # for slot_assignment in parking_slots_BOOK_ASSIGNMENTS:
            # pass
            print("yyyyy now")
            print(parking_slots_BOOK_ASSIGNMENTS)
            print("yyyyy now middle")
            print(slot_assignment)
            print("yyyyy now end")
            parking_slot_id = slot_assignment["parking_slot_id"]
            print(parking_slot_id)
            print("yyyyy now end 2")
            occupied = False
            for time_range in slot_assignment["time_occupied_data"]:
                from_unix = self.convert_to_unix_eq2(time_range['from'])
                to_unix = self.convert_to_unix_eq2(time_range['to'])
                # if not (departure_unix <= time_range[0] or arrival_unix >= time_range[1]):
                if not (arrival_unix >= to_unix or departure_unix <= from_unix):
                # if  (arrival_unix >= from_unix and departure_unix <= to_unix ):
                    print("printing the data that managed to reach here")
                    print(customer_number)
                    occupied = True
                    break

                if not occupied:
                    print("printing the data that managed to reach here PART 2")
                    print(customer_number)
                    TO_BE_APPENDED_TO_parking_slots_BOOK_ASSIGNMENTS.append({
                        "parking_slot_id": parking_slot_id,
                        "time_occupied_data": [(arrival_unix, departure_unix, customer_number)]
                        })
                    assigned = True
                    break

        if not assigned:
            # Generate parking_slot_id
            print("printing the data that managed to reach here PART 3")
            parking_slot_id = f"SLOT-{str(slot_counter).zfill(3)}"
            # Append assignment with initial time_occupied_data
            TO_BE_APPENDED_TO_parking_slots_BOOK_ASSIGNMENTS.append({
                "parking_slot_id": parking_slot_id,
                "time_occupied_data": [(arrival_unix, departure_unix, customer_number)]
            })
            slot_counter += 1
            print(f"current slot cunter is {slot_counter}")

        print("almos exiting the equation")
        print(TO_BE_APPENDED_TO_parking_slots_BOOK_ASSIGNMENTS)
        return TO_BE_APPENDED_TO_parking_slots_BOOK_ASSIGNMENTS





def assign_parking_slot(self, bookings):
    parking_slots_BOOK_ASSIGNMENTS = []
    slot_counter = 1

    for booking in bookings:
        arrival_unix = self.convert_to_unix(booking["arrival_date"], booking["arrival_time"])
        departure_unix = self.convert_to_unix(booking["departure_date"], booking["departure_time"])
        customer_number = booking["customer_number"]

        assigned = False
        for slot_assignment in parking_slots_BOOK_ASSIGNMENTS:
            slot_id = slot_assignment["slot_id"]
            occupied = False
            for time_range in slot_assignment["time_occupied"]:
                if not (departure_unix <= time_range[0] or arrival_unix >= time_range[1]):
                    occupied = True
                    break
            if not occupied:
                slot_assignment["time_occupied"].append((arrival_unix, departure_unix, customer_number))
                assigned = True
                break

        if not assigned:
            parking_slots_BOOK_ASSIGNMENTS.append({
                "slot_id": f"SLOT-{str(slot_counter).zfill(3)}",
                "time_occupied": [(arrival_unix, departure_unix, customer_number)]
            })
            slot_counter += 1

    return parking_slots_BOOK_ASSIGNMENTS




def assign_parking_slot(self, bookings):
    if not bookings:
        return []  # Return an empty list if there are no bookings
    
    parking_slots_BOOK_ASSIGNMENTS = []
    slot_counter = 1

    for booking in bookings:
        arrival_unix = self.convert_to_unix(booking["arrival_date"], booking["arrival_time"])
        departure_unix = self.convert_to_unix(booking["departure_date"], booking["departure_time"])
        customer_number = booking["customer_number"]

        assigned = False
        for slot_assignment in parking_slots_BOOK_ASSIGNMENTS:
            slot_id = slot_assignment["slot_id"]
            occupied = False
            for time_range in slot_assignment["time_occupied"]:
                if not (departure_unix <= time_range[0] or arrival_unix >= time_range[1]):
                    occupied = True
                    break
            if not occupied:
                slot_assignment["time_occupied"].append((arrival_unix, departure_unix, customer_number))
                assigned = True
                break

        if not assigned:
            parking_slots_BOOK_ASSIGNMENTS.append({
                "slot_id": f"SLOT-{str(slot_counter).zfill(3)}",
                "time_occupied": [(arrival_unix, departure_unix, customer_number)]
            })
            slot_counter += 1

    return [SlotAssignmentModel(assignment["slot_id"], [
        {"from": self.convert_to_datetime(time_range[0]), "to": self.convert_to_datetime(time_range[1]), "customer_number": time_range[2]}
        for time_range in assignment["time_occupied"]
    ]) for assignment in parking_slots_BOOK_ASSIGNMENTS]












import time
from datetime import datetime

def convert_to_unix(timestamp_str):
    # Convert timestamp string to datetime object
    timestamp_dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")
    # Convert datetime object to Unix timestamp
    timestamp_unix = int(time.mktime(timestamp_dt.timetuple()))
    return timestamp_unix

# Modify the loop to use converted Unix timestamps for comparison
for time_range in slot_assignment["time_occupied_data"]:
    from_unix = convert_to_unix(time_range['from'])
    to_unix = convert_to_unix(time_range['to'])
    if not (departure_unix <= from_unix or arrival_unix >= to_unix):
        occupied = True
        break

def convert_to_unix(self, timestamp_str):
    dt = datetime.datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M')
    return int(dt.timestamp())
