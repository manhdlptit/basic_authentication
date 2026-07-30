from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token
from werkzeug.security import generate_password_hash, check_password_hash

from app.data.datetime_jwt import expires_delta_refresh
from app.model.model import User, Password, db

from datetime import datetime

change_password = Blueprint("change_password", __name__)

@change_password.route("/change-password", methods = ["POST"])
@jwt_required()
def change_password_when_logged_in():
    current_password = request.json.get("current_password")
    new_password = request.json.get("new_password")

    id = get_jwt_identity()
                
    find_user = User.query.filter(User.id == int(id)).first()

    if not check_password_hash(find_user.password, current_password):
        return jsonify({"Error" : "Password current not correct"})

    if len(new_password) < 8 or len(new_password) > 32:
        return jsonify({"Error" : "Password between 8 and 32 characters"}), 400
    
    password = generate_password_hash(new_password)
    find_user.password = password

    datetime_create_password = datetime.now()
    new_inf_password = Password(date=datetime_create_password, password_used=password, id_user=find_user.id)

    db.session.add(new_inf_password)
    db.session.commit()

    return jsonify({"successfully" : "change password successfully"}), 200


@change_password.route("/forgot-password", methods = ["POST"])
def forgot_password():
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
    
    db.session.commit()
    return jsonify({
        "successfully" : "go to \"/change-password\" ",
        "your_access_token" : access_token,
        "your_refresh_token" : re_fresh_token
        })



