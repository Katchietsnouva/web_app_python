# app/controllers/page_controller.py version 2
from flask import redirect, url_for, request, render_template, flash
from flask import session, flash
from flask import jsonify
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
        # self.home_page = HomePage(    self)
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
                username = request.form.get('username')
                password = request.form.get('password')

                # Authenticate  user
                user_authenticated, user_id  = self.user_controller.authenticate_user(username, password)

                if user_authenticated:
                    session['user_id'] = user_id
                    session['username'] = username 
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
                phone = request.form.get('phone')
                email = request.form.get('email')
                carmanufacturer = request.form.get('carmanufacturer')
                carmodel = request.form.get('carmodel')
                car_plate = request.form.get('car_plate')

                user_id = str(uuid.uuid4())

                # Create UserModel instance
                user_model = UserModel(user_id, None, username, password, phone, email, carmanufacturer, carmodel, car_plate)
                # Register the user
                registration_successful = UserController.register_user(self.user_controller, user_model)
                # registration_successful = self.page_controller.user_controller.register_user(user_model)

                if registration_successful:
                    # Setingt the user_id in the session for future reference
                    session['user_id'] = user_id
                    session['username'] = username

                    # popup
                    flash('Registration Successful! You can now log in.', 'success')
                    return redirect(url_for('success', message='Registration Successful!', redirect_url=url_for('login')))

                    return redirect(url_for('home'))
                    # return redirect(url_for('registration_success'))

            return render_template('registration_page.html')
        
        @app.route('/success')
        def success():
            message = request.args.get('message', 'Operation Successful!')
            # duration = request.args.get('d\uration') 
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
            try:
                user_id = session['user_id']
                user_registration_data =  self.user_controller.get_user_registration_data(session['user_id'])
                user, user_bookings  =  self.user_controller.get_user_booking_data(session['user_id'])

                # Rearranginh tume model to fing the duration difference
                # user_bookings = [TimeModel(**booking) for booking in user_bookings]
                return render_template('home_page.html', user_registration_data=user_registration_data, user=user, user_bookings=user_bookings)
                return render_template('home_page.html', user_registration_data=user_registration_data, user=user, user_bookings=user_bookings)
                return render_template('home_page.html')
            except KeyError:
                # If KeyError occurs (no 'user_id' in session), redirect to registration or login
                flash('Please log in or register to access the home page.', 'error')
                return redirect(url_for('login'))  # Use 'registration' if you have a registration route
        
        # @app.route('/book', methods=['GET', 'POST'])
        # def booking():
        #     if request.method == 'POST':
        #         return redirect(url_for('success', message='Booking Successful!', redirect_url=url_for('home')))
        #     return render_template('booking_page.html')
        
        @app.route('/book', methods=['GET', 'POST'])
        def booking():
            if request.method == 'POST':
                user_id = session.get('user_id')  # storeD the userID in the session
                customer_number = UserController.get_customer_number(self.user_controller, user_id)

                # Get booking details from form
                arrival_date = request.form.get('arrival_date')
                arrival_time = request.form.get('arrival_time')
                departure_date = request.form.get('departure_date')
                departure_time= request.form.get('departure_time')

                # Create a TimeModel instance and filling details
                time_model = TimeModel(user_id, customer_number, None, arrival_date, arrival_time, departure_date, departure_time, None)

                 # Calculate duration before saving
                duration = time_model.calculate_duration()
                # duration = 0
                print(duration)
                duration_minutes = int(duration.total_seconds() / 60)
                print(f"Duration in minutes: {duration_minutes} minutes")

                if duration_minutes < 0:
                    flash('Invalid booking: Departure should be after arrival', 'error')
                    return redirect(url_for('booking'))
                
                # Create a TimeModel instance and filling details
                time_model = TimeModel(user_id, customer_number, None, arrival_date, arrival_time, departure_date, departure_time, duration_minutes)
                
                # Save the time entry to the data service controller
                UserController.save_user_time_data(self.user_controller, time_model)
                flash('Booking Successful!', 'success')

                # return redirect(url_for('success', message='Booking Successful!', duration=duration, redirect_url=url_for('home')))
                return render_template('booking_page.html', duration=duration)
                return render_template('booking_page.html', duration=duration, booking=time_model.to_dict())
            return render_template('booking_page.html')
        
        @app.route('/extendbook', methods=['GET', 'POST'])
        def extendbook():
            user_id = session['user_id']
            usercontroller = UserController()
            user_booked_ticket_ids = usercontroller.html_retrieve_user_ticket_ids(user_id)
            if request.method == 'POST':
                # Retrieve form data
                extension_time = int(request.form.get('extension_time'))
                if extension_time > 300:
                    flash('Extension time cannot be greater than 300 minutes.', 'error')
                    return redirect(url_for('extendbook'))
                selected_ticket_id = request.form.get('ticket_id')
                # # Retrieve ticket details
                ticket_details = usercontroller.html_get_selected_ticket_details(selected_ticket_id)
                print(ticket_details)

                # departure_time= request.form.get('departure_time')
                departure_time = ticket_details['departure_time']
                new_departure_time = usercontroller.calculate_new_departure_time(departure_time, extension_time)
                print(new_departure_time)
                # Update the booking with the new departure time
                usercontroller.update_booking(selected_ticket_id, new_departure_time, extension_time)

                flash('Booking Extended Successfully!', 'success')
                return redirect(url_for('extendbook'))
            return render_template('extend_booking_page.html', user_booked_ticket_ids=user_booked_ticket_ids)
        
        @app.route('/get_selected_ticket_details', methods=['GET'])
        def get_selected_ticket_details():
            selected_ticket_id = request.args.get('ticket_id')
            # Implement logic to fetch details based on the selected ticket ID
            # Replace the following line with your actual logic
            usercontroller = UserController()
            details = usercontroller.html_get_selected_ticket_details(selected_ticket_id)
            if details:
                return jsonify(details)
            else:
                return jsonify({"error": "Ticket ID not found"}), 404
            # details = {"arrival_date": "2024-02-15", "arrival_time": "12:30", "departure_date": "2024-02-16", "departure_time": "14:45"}
            # return jsonify(details)

        
        
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
