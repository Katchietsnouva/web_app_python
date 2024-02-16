# models/payment_model.py
from datetime import datetime;
class TimeModel:
    def __init__(self, user_id, customer_no, booking_id, arrival_date, arrival_time, departure_date, departure_time, duration_minutes):
        self.user_id = user_id
        self.customer_number = customer_no
        self.booking_id = booking_id
        