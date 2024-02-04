
# app/controllers/data_service_controller.py
import json
import os
# from pathlib import Path

class DataService:
    @staticmethod
    def save_data(folder, filename, data):
        folder_path = os.path.join(app.config['JSON_DATA_FOLDER'], folder)
        file_path = os.path.join(folder_path, filename)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open(file_path, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def load_data(folder, filename):
        file_path = os.path.join(app.config['JSON_DATA_FOLDER'], folder, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        return None
    
    def __init__(self):
        # user_data_path = "user_data\\"
        self.users_data_path = "user_data\\global_users_data\\customers_db.json"
        # self.users_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "user_data/global_users_data/customers_db.json"))
        self.users_data = self.load_or_create_users_data()

    def save_users_data(self):
        with open(self.users_data_path, "w") as file:
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
            self.users_data.append(vars(user_model))
            self.save_users_data()
            return True  # Registration successful

    def authenticate_user(self, username, password):
        return any(user["username"] == username and user["password"] == password for user in self.users_data)
