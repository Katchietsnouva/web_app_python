def assign_parking_slot(self, bookings):
    available_slots = [slot for slot in self.get_all_parking_slots_available_data() if slot['available_for_use']]
    if not available_slots:
        return None, "No available slots at the moment. Please try again later."

    parking_slots_BOOK_ASSIGNMENTS = []
    # slot_counter = 1

    for booking in bookings:
        arrival_unix = self.convert_to_unix(booking["arrival_date"], booking["arrival_time"])
        departure_unix = self.convert_to_unix(booking["departure_date"], booking["departure_time"])
        customer_number = booking["customer_number"]

        assigned = False
        for slot in available_slots:
            slot_id = slot["parking_slot_id"]
            occupied = False
            for time_range in slot["time_occupied"]:
                if not (departure_unix <= time_range[0] or arrival_unix >= time_range[1]):
                    occupied = True
                    break
            if not occupied:
                parking_slots_BOOK_ASSIGNMENTS.append({
                    "slot_id": slot_id,
                    "time_occupied": [(arrival_unix, departure_unix, customer_number)]
                })
                assigned = True
                break

        if not assigned:
            return None, "No available slots for the specified time range."

    # return [SlotAssignmentModel(assignment["slot_id"], [
    #     {"from": self.convert_to_datetime(time_range[0]), "to": self.convert_to_datetime(time_range[1]), "customer_number": time_range[2]}
    #     for time_range in assignment["time_occupied"]
    # ]) for assignment in parking_slots_BOOK_ASSIGNMENTS]        
    return parking_slots_BOOK_ASSIGNMENTS, None


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
