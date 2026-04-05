from flask import request, Flask, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from model.model import User, db
import uuid

signup = Blueprint("signup", __name__)

@signup.route("/signup", methods = ["POST"])
def sign_up():
    data = request.get_json()
    full_name = data.get("full_name")
    phone_number = data.get("phone_number")
    email = data.get("email")
    input_password = data.get("input_password")
    check_password = data.get("check_password")
    address = data.get("address")
    country = data.get("country")
    city = data.get("city")

    if phone_number is None and email is None:
        return jsonify({"error" : "not null email or phone_number"}), 400
    found_email = User.query.filter(User.email == email).first()
    if found_email:
        return jsonify({"error" : "email existed!"}), 400
    found_phone = User.query.filter(User.phone_number == phone_number).first()
    if found_phone:
        return jsonify({"error" : "phone existed!"}), 400
    if len(input_password) < 8:
        return jsonify({"error" : "password must longer than 8 character"}), 400
    if input_password != check_password:
        return jsonify({"error" : "input password different check password"}), 400
    token = uuid.uuid4().hex
    password = generate_password_hash(input_password)
    new_user = User(full_name = full_name, phone_number=phone_number, email=email, password=password, address=address, country=country, city=city, token= token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        "full_name" : new_user.full_name,
        "phone_number" : new_user.phone_number,
        "email" : new_user.email,
        # "password" : new_user.password,
        "address" : new_user.address,
        "country" : new_user.country,
        "city" : new_user.city,
        "token" : new_user.token
    }), 201


