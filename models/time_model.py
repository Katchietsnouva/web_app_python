# models/time_model.py
class TimeModel:
    def __init__(self, user_id, customer_no, arrival_date, arrival_time, departure_date, departure_time):
        self.user_id = user_id
        self.customer_number = customer_no
        self.arrival_date = arrival_date
        self.arrival_time = arrival_time
        self.departure_date = departure_date
        self.departure_time = departure_time
