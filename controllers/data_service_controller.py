
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
        self.users_data.append(vars(user_model))
        self.save_users_data()
        return True  # Registration successful
        # Check if the username is already taken
        # if any(user["username"] == user_model.username for user in self.users_data):
        #     return False  # Username is taken
        # else:
        #     self.users_data.append(vars(user_model))
        #     self.save_users_data()
            # return True  # Registration successful

    # def authenticate_user(self, username, password):
    #     return any(user["username"] == username and user["password"] == password for user in self.users_data)
    
    def authenticate_user(self, username, password):
        for user in self.users_data:
            if user["username"] == username and user["password"] == password:
                return True, user["user_id"]
        return False, None

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
        self.time_data.append(vars(time_model))
        self.save_time_data()

    def get_user_time_data(self, user_id):
        return [time_entry for time_entry in self.time_data if time_entry['user_id'] == user_id]


# app/controllers/data_service_controller.py
# class TimeController:
#     # ... existing code ...

#     def save_time_data(self, time_model):
#         self.time_data.append(vars(time_model))
#         self.save_time_data()

#     def load_time_data(self):
#         return self.load_data("time_data.json")


    

