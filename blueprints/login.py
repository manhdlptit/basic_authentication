from flask import request, Flask, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from model.model import User,db
from blueprints.token import get_token


login = Blueprint("login", __name__)

@login.route("/login", methods = ["POST"])
def login_user():
    user = get_token()
    if user is None:
        return jsonify({"error" : "not authentic"}), 401
    data = request.get_json()
    phone_number = data.get("phone_number")
    email = data.get("email")
    input_password = data.get("input_password")

    if phone_number is None and email is None:
        return jsonify({"error" : "must input phone_number or email"}), 400
    if input_password is None:
        return jsonify({"error" : "must input password"}), 400
    found_user = User.query.filter((User.email == email) | (User.phone_number == phone_number)).first()
    if not found_user:
        return jsonify({"error" : "wrong email/phone or password"}), 400
    if not check_password_hash(found_user.password, input_password):
        return jsonify({"error" : "wrong email/phone or password"}), 400
    return jsonify({"successfully" : "login successfully"}), 200
