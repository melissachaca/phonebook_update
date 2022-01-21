from app import app 
from flask import render_template
from app.forms import RegisterForm

@app.route('/')
def index():
    my_name = 'Melissa'
    return render_template('index.html', name=my_name)

@app.route('/name')
def name():
    my_name= 'Melissa'
    return f"Hello {my_name}"

@app.route('/register', methods= ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print("FORM  HAS BEEN VLIDATED")
    return render_template('register.html', form=form)
