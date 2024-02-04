
# app/controllers/page_controller.py version 2
from flask import redirect, url_for
from flask import Flask, render_template
from pages.login_page import LoginPage
# from pages.registration_page import RegisterPage
# from pages.home_page import HomePage
# from pages.booking_page import BookingPage
# from pages.extend_parking_page import ExtendParkingPage
# from pages.payment_page import PaymentPage
# from pages.profit_loss_page import ProfitLossPage
# from user_controller import UserController

class PageController:
    def __init__(self, app):
        self.app = app
        # self.user_controller = UserController()
        self.login_page = LoginPage(self)
        # self.registration_page = RegisterPage(self)
        # self.home_page = HomePage(self)
        # self.booking_page = BookingPage(self)
        # self.extend_parking_page = ExtendParkingPage(self)
        # self.payment_page = PaymentPage(self)
        # self.profit_loss_page = ProfitLossPage(self)

        # Initial route
        @app.route('/')
        def default():
            return render_template('home_page.html')
            self.home_page.show()
            page_controller = PageController(app)
            page_controller.show_home_page()
            
        @app.route('/login')
        def login():
            return render_template('login_page.html')
            self.login_page.show()

        @app.route('/register')
        def registration():
            return render_template('registration_page.html')

        @app.route('/home')
        def home():
            return render_template('home_page.html')

        @app.route('/book')
        def booking():
            return render_template('booking_page.html')

        # @app.route('/extend_parking')
        # def extend_parking():
        #     return self.extend_parking_page.show()

        # @app.route('/payment')
        # def payment():
        #     return self.payment_page.show()

        # @app.route('/profit_loss')
        # def profit_loss():
        #     return self.profit_loss_page.show()

    def redirect_to(self, page_name):
        return redirect(url_for(page_name))

    def show_login_page(self):
        return self.redirect_to('login')

    # def show_registration_page(self):
    #     return self.redirect_to('registration')

    # def show_home_page(self):
    #     return self.redirect_to('home')

    # def show_booking_page(self):
    #     return self.redirect_to('booking')

    # def show_extend_parking_page(self):
    #     return self.redirect_to('extend_parking')

    # def show_payment_page(self):
    #     return self.redirect_to('payment')

    # def show_profit_loss_page(self):
    #     return self.redirect_to('profit_loss')
