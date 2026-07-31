from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token

from werkzeug.security import generate_password_hash

from app.data.datetime_jwt import expires_delta_refresh
from app.model.model import User, db

forgot_password = Blueprint("forgot_password", __name__)


@forgot_password.route("/forgot-password", methods = ["POST"])
def forgot_password_user():
    data = request.get_json()
    phone_number = data.get("phone_number")
    email = data.get("email")
    address = data.get("address")
    country = data.get("country")
    city = data.get("city")
    full_name = data.get("full_name")

    if (full_name 
            and phone_number
            and email
            and address
            and country
            and city) is None:
            return jsonify({"Error" : "Not null any value"}), 400

    find_user = User.query.filter((User.email == email) | (User.phone_number == phone_number)).first()
    if not find_user:
        return jsonify({"error" : "information is not the same"}), 400
    if not (find_user.address == address and find_user.country == country and find_user.city == city and find_user.full_name == full_name):
        return jsonify({"error" : "information is not the same"}), 400

    access_token = create_access_token(identity=find_user)
    re_fresh_token = create_refresh_token(identity=find_user, expires_delta=expires_delta_refresh) 

    password_default = generate_password_hash("12345678")

    find_user.password = password_default
    
    db.session.commit()
    return jsonify({
        "successfully" : "go to \"/change-password\" with password default is '12345678' ",
        "your_access_token" : access_token,
        "your_refresh_token" : re_fresh_token
        }), 200