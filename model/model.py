from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(100))
    phone_number = db.Column(db.String(11))
    email = db.Column(db.String(100))
    address = db.Column(db.String(300))
    country = db.Column(db.String(50))
    city = db.Column(db.String(100))
    password = db.Column(db.String(20))
    token = db.Column(db.String(100))

    def __init__(self, full_name, phone_number, email, address, country, city, password, token):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.country = country
        self.city = city
        self.password = password
        self.token = token

