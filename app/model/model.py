from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "inf_user"

    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(100))
    phone_number = db.Column(db.String(11))
    email = db.Column(db.String(100))
    address = db.Column(db.String(300))
    country = db.Column(db.String(50))
    city = db.Column(db.String(100))
    password = db.Column(db.String(500))

    password_history = db.relationship('Password', backref=db.backref('pw', lazy=True))
    

    def __init__(self, full_name, phone_number, email, address, country, city, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.country = country
        self.city = city
        self.password = password


class Password(db.Model):
    __tablename__ = "password"

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime)
    password_used = db.Column(db.Text)
    id_user = db.Column(db.Integer, db.ForeignKey("inf_user.id"))



    def __init__(self, date, password_used, id_user):
        self.date = date
        self.password_used = password_used
        self.id_user = id_user

class BlockList(db.Model):
    __tablename__ = "block_list_token"

    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(50))

    def __init__(self, jti):
        self.jti = jti
