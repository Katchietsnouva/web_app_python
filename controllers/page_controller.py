# app/controllers/page_controller.py version 2
from flask import redirect, url_for, request, render_template
from flask import session, flash
import uuid
from pages.login_page import LoginPage
# from pages.registration_page import RegisterPage
# from pages.home_page import HomePage
# from pages.booking_page import BookingPage
# from pages.extend_parking_page import ExtendParkingPage
# from pages.payment_page import PaymentPage
# from pages.profit_loss_page import ProfitLossPage
from controllers.data_service_controller import UserController
from models.user_model import UserModel
from models.time_model import TimeModel
# import user_data
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
            
        # @app.route('/login')
        # def login():
        #     return render_template('login_page.html')
        #     self.login_page.show()

        @app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                # Get form data
                username = request.form.get('username')
                password = request.form.get('password')

                # Authenticate the user
                user_authenticated, user_id  = self.user_controller.authenticate_user(username, password)

                if user_authenticated:
                    session['user_id'] = user_id
                    session['username'] = username  # Store the username in the session
                    flash('Login Successful', 'success')
                    return redirect(url_for('home'))
                else:
                    flash('Invalid username or password. Please try again.', 'error')

            return render_template('login_page.html')

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

                # Generate a unique user_id using uuid
                user_id = str(uuid.uuid4())

                # Create a UserModel instance
                user_model = UserModel(user_id, username, password, name, phone, car_plate, email)

                # Register the user
                registration_successful = UserController.register_user(self.user_controller, user_model)
                # registration_successful = self.page_controller.user_controller.register_user(user_model)

                if registration_successful:
                    # Set the user_id in the session for future reference
                    session['user_id'] = user_id

                    # popup 'Registration Successful!'
                    return redirect(url_for('success', message='Registration Successful!', redirect_url=url_for('home')))

                    return redirect(url_for('home'))
                    # return redirect(url_for('registration_success'))

            return render_template('registration_page.html')
        
        @app.route('/success')
        def success():
            message = request.args.get('message', 'Operation Successful!')
            redirect_url = request.args.get('redirect_url', url_for('home'))
            return render_template('success_page.html', message=message, redirect_url=redirect_url)

        @app.route('/registration-success')
        def registration_success():
            message = request.args.get('message', 'Registration Successful!')
            return render_template('registration_success.html', message=message)

        # @app.route('/registration-success')
        # def registration_success():
        #     return 'Registration Successful!'

        # @app.route('/register')
        # def registration():
        #     return render_template('registration_page.html')

        @app.route('/home')
        def home():
            return render_template('home_page.html')
        

        # @app.route('/book', methods=['GET', 'POST'])
        # def booking():
        #     if request.method == 'POST':
        #         return redirect(url_for('success', message='Booking Successful!', redirect_url=url_for('home')))
        #     return render_template('booking_page.html')
        
        @app.route('/book', methods=['GET', 'POST'])
        def booking():
            if request.method == 'POST':
                # Get user ID (you may use the username for simplicity)
                user_id = session.get('user_id')  # Assuming you store the username in the session

                # Get booking details from the form
                arrival_date = request.form.get('arrival_date')
                arrival_time = request.form.get('arrival_time')
                departure_date = request.form.get('departure_date')
                departure_time = request.form.get('departure_time')

                # Create a TimeModel instance with the user ID and booking details
                time_model = TimeModel(user_id, arrival_date, arrival_time, departure_date, departure_time)

                # Save the time entry to the data service controller
                UserController.save_user_time_data(self.user_controller, time_model)

                return redirect(url_for('success', message='Booking Successful!', redirect_url=url_for('home')))
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
