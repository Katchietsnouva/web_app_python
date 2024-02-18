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
        

        @app.route('/admin', methods=['GET'])
        def admin_page():
            # Check if the user is logged in and has admin role
            if 'user_id' in session and 'username' in session:
                user = self.user_controller.get_user_registration_data(session['user_id'])
                # if user.role == 'admin':
                # if user['role'] == 'admin':
                # if user.get('phone') == 'm':
                if user.get('role') == 'admin':
                    # Get a list of all users (you need to implement this method)
                    all_users = self.user_controller.get_all_users()

                    # Render the admin page with the list of users
                    return render_template('admin_page.html', all_users=all_users)

            # If not an admin or not logged in, redirect to login
            flash('You do not have permission to access this page.', 'error')
            return redirect(url_for('login'))
                    
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
                user_authenticated, user_id, user_role   = self.user_controller.authenticate_user(username, password)

                if user_authenticated:
                    session['user_id'] = user_id
                    session['username'] = username 

                    # admin_user = self.user_controller.get_user_registration_data(session['user_id'])
                    # if admin_user.role == 'admin':
                    print(user_role)
                    if user_role == 'admin':
                        # return render_template('admin_page.html')
                        return redirect(url_for('admin_page'))
                    else:
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
                role = request.form.get('role')

                user_id = str(uuid.uuid4())

                # Create UserModel instance
                user_model = UserModel(user_id, None, username, password, phone, email, carmanufacturer, carmodel, car_plate, role)
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
                user, user_bookings, calculate_amount  =  self.user_controller.get_user_booking_data(session['user_id'])
                latest_booking_id  = None

                # Rearranginh tume model to fing the duration difference
                # user_bookings = [TimeModel(**booking) for booking in user_bookings]
                return render_template('home_page.html', user_registration_data=user_registration_data, user=user, user_bookings=user_bookings, calculate_amount=calculate_amount, latest_booking_id=latest_booking_id)
            except KeyError:
                # If KeyError occurs (no 'user_id' in session), redirect to registration or login
                flash('Please log in or register to access the home page.', 'error')
                return redirect(url_for('login')) 
        
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
                return render_template('booking_page.html', duration=duration, booking_successful=True, latest_booking_id=time_model.booking_id)
            
                return render_template('booking_page.html', duration=duration, booking=time_model.to_dict())
            return render_template('booking_page.html')
        
        @app.route('/extendbook', methods=['GET', 'POST'])
        def extendbook():
            user_id = session['user_id']
            # usercontroller = UserController()
            user_booked_ticket_ids = UserController.html_retrieve_user_ticket_ids(self.user_controller, user_id)
            if request.method == 'POST':
                # Retrieve form data
                extension_time = int(request.form.get('extension_time'))
                if extension_time > 300:
                    flash('Extension time cannot be greater than 300 minutes.', 'error')
                    return redirect(url_for('extendbook'))
                selected_ticket_id = request.form.get('ticket_id')
                # # Retrieve ticket details
                ticket_details = UserController.html_get_selected_ticket_details(self.user_controller, selected_ticket_id)
                print(ticket_details)

                # departure_time= request.form.get('departure_time')
                departure_time = ticket_details['departure_time']
                new_departure_time = UserController.calculate_new_departure_time(self.user_controller, departure_time, extension_time)
                print(new_departure_time)

                # Update the booking and capture the modified booking ID
                modified_booking_id = UserController.update_booking(self.user_controller, selected_ticket_id, new_departure_time, extension_time)

                if modified_booking_id:
                    flash('Booking Extended Successfully!', 'success')
                    return render_template('extend_booking_page.html', duration=extension_time, extended_booking_successful=True, latest_booking_id=modified_booking_id["booking_id"])
                else:
                    flash('Failed to extend booking.', 'error')
                    return redirect(url_for('extendbook'))
            return render_template('extend_booking_page.html', user_booked_ticket_ids=user_booked_ticket_ids)
        
        # # @app.route('/payment')
        # # @app.route('/payment/<latest_booking_id>')
        # @app.route('/payment/<latest_booking_id>')
        # def payment(latest_booking_id):
        #     # latest_ticket = self.user_controller.get_latest_modified_ticket()
        #     # return render_template('payment_page.html', latest_ticket=latest_ticket)
        #     latest_mod_ticket_details = self.user_controller.html_get_selected_ticket_details(latest_booking_id)
        #     return render_template('payment_page.html', latest_mod_ticket_details=latest_mod_ticket_details)
        
        # @app.route('/payment/<latestBookingId>', defaults={'latestBookingId': None})
        @app.route('/payment/<latest_booking_id>')
        def payment(latest_booking_id):
            print(latest_booking_id + " -this is the value of latest_booking_id ") 
            if latest_booking_id is not None:
                print(latest_booking_id + " this should be executed if latest_booking_id has a value") 
                # If latestBookingId is provided, fetch details for that specific ticket
                latest_mod_ticket_details = self.user_controller.html_get_selected_ticket_details(latest_booking_id)
                return render_template('payment_page.html', latest_mod_ticket_details=latest_mod_ticket_details)
            else:
                print(latest_booking_id + " this should be executed if latest_booking_id has no value") 
                # try:
                # If latestBookingId is not provided, fetch details for all tickets
                user_id = session['user_id']
                user_registration_data =  self.user_controller.get_user_registration_data(session['user_id'])
                user, user_bookings, calculate_amount  =  self.user_controller.get_user_booking_data(session['user_id'])
                return render_template('payment_page.html', user_registration_data=user_registration_data, user=user, user_bookings=user_bookings, calculate_amount=calculate_amount)


            
        @app.route('/get_selected_ticket_details', methods=['GET'])
        def get_selected_ticket_details():
            selected_ticket_id = request.args.get('ticket_id')
            # Implement logic to fetch details based on the selected ticket ID
            # usercontroller = UserController()
            details = UserController.html_get_selected_ticket_details(self.user_controller, selected_ticket_id)
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
