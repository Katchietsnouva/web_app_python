
# app/controllers/page_controller.py version 2
from flask import redirect, url_for, request, render_template
from pages.login_page import LoginPage
# from pages.registration_page import RegisterPage
# from pages.home_page import HomePage
# from pages.booking_page import BookingPage
# from pages.extend_parking_page import ExtendParkingPage
# from pages.payment_page import PaymentPage
# from pages.profit_loss_page import ProfitLossPage
from controllers.data_service_controller import UserController
from models.user_model import UserModel

class PageController:
    def __init__(self, app):
        self.app = app
        self.user_controller = UserController()
        # self.user_controller = UserController(username, password, name, phone, car_plate, email)
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

        @app.route('/register', methods=['GET', 'POST'])
        def registration():
            if request.method == 'POST':
            # if self.app.request.method == 'POST':
                # Get form data
                username = request.form.get('username')
                password = request.form.get('password')
                name = request.form.get('name')
                phone = request.form.get('phone')
                car_plate = request.form.get('car_plate')
                email = request.form.get('email')

                # Create a UserModel instance
                user_model = UserModel(username, password, name, phone, car_plate, email)

                # Register the user
                registration_successful = UserController.register_user(self, user_model)
                # registration_successful = self.page_controller.user_controller.register_user(user_model)

                if registration_successful:
                    return redirect(url_for('registration_success'))

            return render_template('registration_page.html')
        
        @app.route('/registration-success')
        def registration_success():
            return 'Registration Successful!'

        # @app.route('/register')
        # def registration():
        #     return render_template('registration_page.html')

        @app.route('/home')
        def home():
            return render_template('home_page.html')

        @app.route('/book')
        def booking():
            return render_template('booking_page.html')

        # @app.route('/extend_parking')
        # def extend_parking():
        #     return self.extend_parking_page.show()


    def redirect_to(self, page_name):
        return redirect(url_for(page_name))

    def show_login_page(self):
        return self.redirect_to('login')

    # def show_registration_page(self):
    #     return self.redirect_to('registration')

    # def show_home_page(self):
    #     return self.redirect_to('home')
