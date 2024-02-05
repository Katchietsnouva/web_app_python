# app/app.py v2
# from app import app
# pip install flask_mysqldb
# pip install pymysql

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from controllers.page_controller import PageController

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'
# db = SQLAlchemy(app)  

# @app.route('/registration')
# def registration():
#     page_controller = PageController(app)
#     return page_controller.show_registration_page()

if __name__ == '__main__':
    with app.app_context():
        # db.create_all()  # Create tables when the app is run
        page_controller = PageController(app)
        app.run(debug=True)
