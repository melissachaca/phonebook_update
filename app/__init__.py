from flask import Flask 

app = Flask (__name__)
app.config['SECRET KEY'] = 'please work'

from . import routes 