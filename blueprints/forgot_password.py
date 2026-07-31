from flask import request, Flask, jsonify,Blueprint
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from model.model import User,db
from blueprints.token import get_token
import uuid


forget = Blueprint("forgot-password", __name__)

@forget.route("/forgot-password", methods = ["POST"])
def forgot_password():
    user = get_token()
    if user is None:
        return jsonify({"error" : "not authentic"}), 401
    data = request.get_json()
    phone_number = data.get("phone_number")
    email = data.get("email")

    address = data.get("address")
    country = data.get("country")
    city = data.get("city")
    full_name = data.get("full_name")


    found_user = User.query.filter((User.email == email) | (User.phone_number == phone_number)).first()
    if not found_user:
        return jsonify({"error" : "user not sign up yet"}), 400
    if not (found_user.address == address and found_user.country == country and found_user.city == city and found_user.full_name == full_name):
        return jsonify({"error" : "information is not the same"}), 400
    token = uuid.uuid4().hex
    found_user.token = token
    found_user.change_password = "OK"
    db.session.commit()
    return jsonify({
        "successfully" : "go to \"/new-password\" ",
        "your_token" : found_user.token
        })

    


@forget.route("/new-password", methods = ["PUT"])
def new_password():
    user = get_token()
    if user is None:
        return jsonify({"error" : "not authentic"}), 401
    data = request.get_json()
    if user.change_password != "OK":
        return jsonify({"error" : "Forbidden! You must successful in \"/forgot-password\""}), 403
    new_pass_word_you_choose = data.get("new_pass_word_you_choose")
    if new_pass_word_you_choose is None:
        user.password = generate_password_hash("123456789")
        db.session.commit()
        return jsonify({"successfully" : "password default is \"123456789\""}), 200
    user.password = generate_password_hash(new_pass_word_you_choose)
    user.change_password = "None"
    db.session.commit()
    return jsonify({"successfully" : "change password successfully"}), 200


    