from app import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    phonenumber = db.Column(db.String(80),unique=True, nullable=False)




