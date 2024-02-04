# app/app.py v2
# from app import app
from flask import Flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from controllers/page_controller import PageController
from controllers.page_controller import PageController

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'
# db = SQLAlchemy(app)

# @app.route('/')
# def home():
#     return render_template('home_page.html')

# @app.route('/registration')
# def registration():
#     page_controller = PageController(app)
#     return page_controller.show_registration_page()

if __name__ == '__main__':
    page_controller = PageController(app)
    # db.create_all() # Create tables when the app is run
    app.run(debug=True)