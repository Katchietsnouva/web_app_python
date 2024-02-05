# app/models/user_model.py
class UserModel:
    def __init__(self, user_id, customer_no, username, password, name, phone, car_plate, email):
        self.user_id = user_id
        self.customer_number = customer_no
        self.username = username
        self.password = password
        self.name = name
        self.phone = phone
        self.car_plate = car_plate
        self.email = email



# # app/models/user_model.py
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)
#     name = db.Column(db.String(80), nullable=False)
#     phone = db.Column(db.String(15), nullable=False)
#     car_plate = db.Column(db.String(20), nullable=False)
#     email = db.Column(db.String(120), nullable=False)

#     def __repr__(self):
#         return f'<User {self.username}>'


