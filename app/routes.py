from app import app 
from flask import render_template, redirect, url_for
from app.forms import RegisterForm

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/register', methods= ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print("FORM  HAS BEEN VLIDATED")
        return redirect(url_for ('index.html'))
    return render_template('register.html', form=form)
