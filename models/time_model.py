# models/time_model.py
from datetime import datetime;
class TimeModel:
    def __init__(self, user_id, customer_no, booking_id, arrival_date, arrival_time, departure_date, departure_time):
        self.user_id = user_id
        self.customer_number = customer_no
        self.booking_id = booking_id
        self.arrival_date = arrival_date
        self.arrival_time = arrival_time
        self.departure_date = departure_date
        self.departure_time = departure_time

    def calculate_duration(self):
            arrival_datetime = datetime.strptime(f"{self.arrival_date} {self.arrival_time}", "%Y-%m-%d %H:%M")
            departure_datetime = datetime.strptime(f"{self.departure_date} {self.departure_time}", "%Y-%m-%d %H:%M")

            duration = departure_datetime - arrival_datetime
            return duration