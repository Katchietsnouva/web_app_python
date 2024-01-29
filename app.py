from flask import Flask, render_template

app = Flask(__name__)

# Your existing code can be imported here

@app.route('/')
def home():
    return render_template('home_page.html')  # Create templates folder and HTML files accordingly

if __name__ == '__main__':
    app.run(debug=True)
