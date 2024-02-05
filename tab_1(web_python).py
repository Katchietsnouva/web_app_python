# Create a file named app.py:
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_page.html')

if __name__ == '__main__':
    app.run(debug=True)




@app.route('/login')
def login():
    return render_template('login_page.html')

@app.route('/registration')
def registration():
    return render_template('registration_page.html')

# in  app.py:

@app.route('/home/<username>')
def home(username):
    return render_template('home_page.html', username=username)

# page_controller.py:
def login_controller():
    return "Login logic  "

def registration_controller():
    return "Registration logic  "


# user_model.py, might use in  controllers:

from models.user_model import User

def login_controller(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return "Login successful"
    else:
        return "Invalid credentials"
    
