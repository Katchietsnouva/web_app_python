
# app/controllers/data_service_controller.py

# from flask import current_app
# from pathlib import Path

# class DataService:
# class UserController:
    # @staticmethod
    # app.config['JSON_DATA_FOLDER'] = 'user_data\\global_users_data\\customers_db.json'
    # current_app.config['users_data_path'] = 'user_data\\global_users_data\\customers_db.json'
    # folder_path = os.path.join(current_app.config['JSON_DATA_FOLDER'], folder)
    # file_path = os.path.join(folder_path, filename)
    # def __init__(current_app):
        # current_app.users_data_path = "user_data/global_users_data/customers_db.json"
        # current_app.config['users_data_path'] = 'user_data\\global_users_data\\customers_db.json'
        # current_app.users_data = current_app.load_or_create_users_data()  
        # JSON_DATA_FOLDER = 'user_data/global_users_data'
    # def __init__(self, username, password, name, phone, car_plate, email):

# app/controllers/data_service_controller.py
import json
import os
from datetime import datetime, timedelta
class UserController:
    def __init__(self):
        self.users_data_path = 'user_data\\global_users_data\\customers_db.json'
        self.time_data_path = 'user_data\\global_users_data\\time_data.json'
        self.payment_data_path = 'user_data\\global_users_data\\payment_data.json'
        self.users_data = self.load_or_create_users_data()
        self.time_data = self.load_or_create_time_data()
        self.payment_data = self.load_or_create_payment_data()
        self.last_booking_index = {}
        # self.users_data_path = current_app.config['users_data_path']
        self.tickets_data = [
            {'id': 8, 'arrival_date': '2024-02-01', 'departure_date': '2024-02-05'},
            {'id': 4, 'arrival_date': '2024-02-19', 'departure_date': '2024-02-15'},
        ]

    def get_latest_modified_ticket(self):
        latest_ticket = max(self.tickets_data, key=lambda x: x.get('modification_date', ''))
        return latest_ticket

    def get_all_users(self):
        return self.users_data 

    def save_users_data(self):
        with open(self.users_data_path, "w") as file:
            # json.dump(self.user_model, file, indent=4)
            json.dump(self.users_data, file, indent=4)

    def load_users_data(self):
        with open(self.users_data_path, "r") as file:
            return json.load(file)

    def load_or_create_users_data(self):
        directory = os.path.dirname(self.users_data_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(self.users_data_path):
            self.users_data = []
            self.save_users_data()
        else:
            self.users_data = self.load_users_data()
        return self.users_data

    def register_user(self, user_model):
        
        # Check if the username is already taken
        if any(user["username"] == user_model.username for user in self.users_data):
            return False  # Username is taken
        else:
            user_model.customer_number = self.generate_customer_number()
            self.users_data.append(vars(user_model))
            self.save_users_data()# Registration successful
            return True  # Registration successful
    
    def generate_customer_number(self):
        # Get the current number of users to generate a unique customer number
        current_user_count = len(self.users_data)
        # Assuming a simple method for generating customer numbers, you can customize this based on your requirements
        return f'CUST-{current_user_count + 1}'


    # def authenticate_user(self, username, password):
    #     return any(user["username"] == username and user["password"] == password for user in self.users_data)
    
    def authenticate_user(self, username, password):
        for user in self.users_data:
            if user["username"] == username and user["password"] == password:
                return True, user["user_id"], user.get("role", "user")  # Default role to 'user' if not present
        return False, None, None
    
    def get_customer_number(self, user_id):
        user = next((user for user in self.users_data if user["user_id"] == user_id), None)
        if user:
            return user["customer_number"]
        else:
            return None

    def save_time_data(self):
        with open(self.time_data_path, "w") as file:
            json.dump(self.time_data, file, indent=4)
            

    def load_time_data(self):
        with open(self.time_data_path, "r") as file:
            return json.load(file)

    def load_or_create_time_data(self):
        directory = os.path.dirname(self.time_data_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(self.time_data_path):
            self.time_data = []
            self.save_time_data()
        else:
            self.time_data = self.load_time_data()
        return self.time_data

    def save_user_time_data(self, time_model):
        # generating unique booking id
        booking_id = self.generate_booking_id(time_model.user_id)
        time_model.booking_id = booking_id
        # Calculate duration
        # duration = time_model.calculate_duration()
        # time_model.duration = duration
        self.time_data.append(vars(time_model))
        self.save_time_data()


    def get_user_time_data(self, user_id):
        return [time_entry for time_entry in self.time_data if time_entry['user_id'] == user_id]
    
    def generate_booking_id(self, user_id):
        # user_bookings = [entry for entry in self.time_data if entry['user_id'] == user_id]
        user_bookings = [entry for entry in self.time_data]
        if not user_bookings:
            return f'Book_id-001'
        else:
            latest_booking_id = user_bookings[-1]['booking_id']
            index = int(latest_booking_id.split('-')[1]) + 1
            return f'Book_id-{index:03d}'
            # if "-ext-" in latest_booking_id:
            #     base_id, ext = latest_booking_id.split("-ext-")
            #     next_ext = int(ext) + 1
            #     return f'{base_id}-ext-{next_ext}'
            # else:
            #     return f'{latest_booking_id}-ext-1'
        
        
    def get_user_registration_data(self, user_id):
        # Retrieve user registration data based on user_id
        user_data = next((user for user in self.users_data if user['user_id'] == user_id), None)
        return user_data
    
    # def get_user_booking_data(self, user_id):
    #     # Retrieve user registration data based on user_id
    #     user_data = next((user for user in self.users_data if user['user_id'] == user_id), None)
    #     return user_data
    
    def get_user_booking_data(self, user_id):
        # Assuming user_data and time_data are lists of dictionaries
        user_data = self.users_data
        time_data = self.time_data
        # Find the user in user_data based on user_id
        user = next((user_entry for user_entry in user_data if user_entry['user_id'] == user_id), None)

        if user:
            # Find bookings associated with the user in time_data
            user_bookings = [booking_entry for booking_entry in time_data if booking_entry['user_id'] == user_id]
            return user, user_bookings, self.calculate_amount  # Include calculate_amount in the returned data
        else:
            return None, [], self.calculate_amount
        
    def calculate_amount(self, duration_minutes):
        rate = 0.8 
        return round(duration_minutes * rate, 2)

        
    # def retrieve_user_ticket_ids(self, user_id):
    #     user = next((user_entry for user_entry in self.time_data if user_entry['user_id'] == user_id), None)

    def html_retrieve_user_ticket_ids(self, user_id):
        # self.time_data is a list of dictionaries representing booking entries
        time_data = self.time_data
        user_bookings = [entry for entry in time_data if entry['user_id'] == user_id]

        # user can have multiple bookings, return a list of booking IDs
        return [booking["booking_id"] for booking in user_bookings]
    
    def html_get_selected_ticket_details(self, ticket_id):
        # Find the entry in time_data with the given ticket_id
        time_data = self.time_data
        ticket_entry = next((entry for entry in time_data if entry['booking_id'] == ticket_id), None)

        if ticket_entry:
            return {
                "user_id": ticket_entry["user_id"],
                "customer_number": ticket_entry["customer_number"],
                "booking_id": ticket_entry["booking_id"],
                "arrival_date": ticket_entry["arrival_date"],
                "arrival_time": ticket_entry["arrival_time"],
                "departure_date": ticket_entry["departure_date"],
                "departure_time": ticket_entry["departure_time"],
                "duration_minutes": ticket_entry["duration_minutes"],
            }
        else:
            # Ticket ID not found, return an appropriate response or handle accordingly
            # return None
            return {"error": "Ticket ID not found"}
        
    def calculate_new_departure_time(self, original_departure_time, extension_time):
        # Convert to datetime object
        original_departure_datetime = datetime.strptime(original_departure_time, "%H:%M")

        # Add the extension_time (in minutes) to the original_departure_time
        updated_departure_datetime = original_departure_datetime + timedelta(minutes=extension_time)

        # Convert the result back to the desired format (e.g., string)
        updated_departure_time = updated_departure_datetime.strftime("%H:%M")

        return updated_departure_time
    

    def update_booking(self, selected_ticket_id, new_departure_time, extension_time):
        # Find the booking in the time_data list with the selected_ticket_id
        booking = next((entry for entry in self.time_data if entry['booking_id'] == selected_ticket_id), None)

        if booking:
            # Update the departure_time in the booking
            # booking['departure_time'] = new_departure_time

            # Modify the booking_id to indicate it's an extended booking
            extended_booking = {
                "user_id": booking["user_id"],
                "customer_number": booking["customer_number"],
                "booking_id": f"{booking['booking_id']}-ext",
                "arrival_date": booking["arrival_date"],
                "arrival_time": booking["arrival_time"],
                "departure_date": booking["departure_date"],
                "departure_time": new_departure_time,
                "duration_minutes": extension_time
                # "role": role,
            }

            # Append the new extended booking entry to the time_data
            self.time_data.append(extended_booking)
            # Save the updated time_data to the JSON file
            self.save_time_data()
            # Return the modified booking ID
            # return extended_booking["booking_id"]
            return extended_booking
        # Return None if the booking is not found
        return None



# app/controllers/data_service_controller.py
# class TimeController:
#     # ... existing code ...

#     def save_time_data(self, time_model):
#         self.time_data.append(vars(time_model))
#         self.save_time_data()

#     def load_time_data(self):
#         return self.load_data("time_data.json")


    

