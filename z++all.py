# pip install flask_mysqldb
# app/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/home/<username>')
def home(username):
    return render_template('home_page.html', username=username)

@app.route('/login')
def login():
    return render_template('login_page.html')

@app.route('/registration')
def registration():
    return render_template('registration_page.html')

if __name__ == '__main__':
    app.run(debug=True)




# app/app.py v2
# from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.page_controller import PageController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'
db = SQLAlchemy(app)


@app.route('/')
def home():
    page_controller = PageController(app)
    return page_controller.show_login_page()

@app.route('/login')
def login():
    page_controller = PageController(app)
    return page_controller.show_login_page()

@app.route('/registration')
def registration():
    page_controller = PageController(app)
    return page_controller.show_registration_page()

if __name__ == '__main__':
    page_controller = PageController(app)
    db.create_all() # Create tables when the app is run
    app.run(debug=True)

# app/__init__.py
from flask import Flask

app = Flask(__name__)


# app/pages/base_page.py
from flask import render_template

class BasePage:
    def __init__(self, page_controller):
        self.page_controller = page_controller

    def render_template(self, template_name, **kwargs):
        return render_template(template_name, **kwargs)
    

# app/pages/login_page.py
from .base_page import BasePage
from flask import request, redirect, url_for

class LoginPage(BasePage):
    def show(self):
        return self.render_template('login_page.html')

    # ... other methods remain similar


# app/templates\home_page.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Web App</title>
</head>
<body>
    <h1>Welcome to My Web App!</h1>
    <p>This is a simple example using Flask.</p>
    <h1>Welcome to My Web App, {{ username }}!</h1>
</body>
</html>



# app/models/user_model.py v1
class UserModel:
    def __init__(self, username, password, name, phone, car_plate, email):
        self.username = username
        self.password = password
        self.name = name
        self.phone = phone
        self.car_plate = car_plate
        self.email = email


# app/models/user_model.py v2
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    car_plate = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'



# controllers\page_controller.py version 1
from models.user_model import User

def login_controller(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        # Successful login logic
        return "Login successful"
    else:
        # Failed login logic
        return "Invalid credentials"


def registration_controller():
    # Your registration logic here
    return "Registration logic goes here"


# app/controllers/page_controller.py version 2
from flask import redirect, url_for
from pages.login_page import LoginPage
from pages.registration_page import RegisterPage
from pages.home_page import HomePage
from pages.booking_page import BookingPage
from pages.extend_parking_page import ExtendParkingPage
from pages.payment_page import PaymentPage
from pages.profit_loss_page import ProfitLossPage
from user_controller import UserController

class PageController:
    def __init__(self, app):
        self.app = app
        self.user_controller = UserController()
        self.login_page = LoginPage(self)
        self.registration_page = RegisterPage(self)
        self.home_page = HomePage(self)
        self.booking_page = BookingPage(self)
        self.extend_parking_page = ExtendParkingPage(self)
        self.payment_page = PaymentPage(self)
        self.profit_loss_page = ProfitLossPage(self)

        # Initial route
        @app.route('/')
        def home():
            return self.login_page.show()

        # Routes for other pages
        @app.route('/login')
        def login():
            return self.login_page.show()

        @app.route('/registration')
        def registration():
            return self.registration_page.show()

        @app.route('/home')
        def home():
            return self.home_page.show()

        @app.route('/booking')
        def booking():
            return self.booking_page.show()

        @app.route('/extend_parking')
        def extend_parking():
            return self.extend_parking_page.show()

        @app.route('/payment')
        def payment():
            return self.payment_page.show()

        @app.route('/profit_loss')
        def profit_loss():
            return self.profit_loss_page.show()

    def redirect_to(self, page_name):
        return redirect(url_for(page_name))

    def show_login_page(self):
        return self.redirect_to('login')

    def show_registration_page(self):
        return self.redirect_to('registration')

    def show_home_page(self):
        return self.redirect_to('home')

    def show_booking_page(self):
        return self.redirect_to('booking')

    def show_extend_parking_page(self):
        return self.redirect_to('extend_parking')

    def show_payment_page(self):
        return self.redirect_to('payment')

    def show_profit_loss_page(self):
        return self.redirect_to('profit_loss')


# app/controllers/page_controller.py
from flask import redirect, url_for
from flask import render_template
from flask import request
from pages.login_page import LoginPage
from pages.registration_page import RegisterPage
from pages.home_page import HomePage
from models.user_model import User, db

class PageController:
    def __init__(self, app):
        # ... (other initialization code)

        @app.route('/')
        def home():
            return self.login_page.show()

        @app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                # Handle login logic here
                pass
            return self.login_page.show()

        @app.route('/registration', methods=['GET', 'POST'])
        def registration():
            if request.method == 'POST':
                # Handle registration logic here
                pass
            return self.registration_page.show()

        @app.route('/home')
        def home():
            return self.home_page.show()

    def redirect_to(self, page_name):
        return redirect(url_for(page_name))



# app/pages/login_page.py
from flask import render_template
from pages.base_page import BasePage
from customtkinter import CTkLabel, CTkEntry, CTkButton

class LoginPage(BasePage):
    def create_widgets(self):
        # Page-specific widgets for the login page
        label_title = CTkLabel(self, text="Login Page", font=("ar", 15, "bold"))
        label_title.pack(pady=20)

        # Add your login form elements here using CTkEntry, CTkButton, etc.
        # Example:
        # username_entry = CTkEntry(self, textvariable=self.username_var)
        # password_entry = CTkEntry(self, textvariable=self.password_var, show="*")
        # login_button = CTkButton(self, text="Login", command=self.getvals_login)
        # ... (add more widgets as needed)
