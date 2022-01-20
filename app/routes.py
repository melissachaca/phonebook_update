from app import app 
from flask import render_template

@app.route('/')
def index():
    my_name = 'Melissa'
    return render_template('index.html', name=my_name)

@app.route('/name')
def name():
    my_name= 'Melissa'
    return f"Hello {my_name}"

@app.route('/addcontact')
def test():
    return "this is a test"