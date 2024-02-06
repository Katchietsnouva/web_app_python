
# app/controllers/data_service_controller.py
import json
import os
# from flask import current_app
# from pathlib import Path

# class DataService:
class UserController:
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
    def __init__(self):
        self.users_data_path = 'user_data\\global_users_data\\customers_db.json'
        self.time_data_path = 'user_data\\global_users_data\\time_data.json'
        self.users_data = self.load_or_create_users_data()
        self.time_data = self.load_or_create_time_data()
        self.last_booking_index = {}
        # self.users_data_path = current_app.config['users_data_path']

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
                return True, user["user_id"]
        return False, None
    
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

            return user, user_bookings
        else:
            return None, []
        
    def retrieve_user_booking_ids(self, user_id):
        # Retrieve user ID from the session
        # retrieved_user_bookings = [entry for entry in self.time_data if entry['user_id'] == user_id]
        # user_id = session.get('user_id')
        user_data = self.users_data
        time_data = self.time_data
        user = next((user_entry for user_entry in user_data if user_entry['user_id'] == user_id), None)
        if user:
                    # Find bookings associated with the user in time_data
                    user_bookings = [booking_entry for booking_entry in time_data if booking_entry['user_id'] == user_id]

                    return user, user_bookings
                else:
                    return None, []
        
        # Assuming you have a method to get booking IDs based on the user ID
        user_booking_ids = UserController.get_user_booking_ids(user_id)

        return user_booking_ids
        


# app/controllers/data_service_controller.py
# class TimeController:
#     # ... existing code ...

#     def save_time_data(self, time_model):
#         self.time_data.append(vars(time_model))
#         self.save_time_data()

#     def load_time_data(self):
#         return self.load_data("time_data.json")


    

