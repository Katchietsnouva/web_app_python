# from flask import Flask, render_template

# app = Flask(__name__)

# # Your existing code can be imported here

# @app.route('/')
# def home():
#     return render_template('home_page.html')  # Create templates folder and HTML files accordingly


# if __name__ == '__main__':
#     app.run(debug=True)

# app/app.py v2
# from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from controllers/page_controller import PageController
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