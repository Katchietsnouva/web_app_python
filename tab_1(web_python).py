# Create a file named app.py:
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_page.html')

if __name__ == '__main__':
    app.run(debug=True)



# Add More Routes: Define additional routes in your app.py file to handle different pages. For example:

@app.route('/login')
def login():
    return render_template('login_page.html')

@app.route('/registration')
def registration():
    return render_template('registration_page.html')

# And in your app.py:

@app.route('/home/<username>')
def home(username):
    return render_template('home_page.html', username=username)

# page_controller.py:
def login_controller():
    # Your login logic here
    return "Login logic goes here"

def registration_controller():
    # Your registration logic here
    return "Registration logic goes here"


# user_model.py, you might use it in your controllers:

from models.user_model import User

def login_controller(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        # Successful login logic
        return "Login successful"
    else:
        # Failed login logic
        return "Invalid credentials"
    
