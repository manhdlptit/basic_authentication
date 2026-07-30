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
        return jsonify({"Error" : "Password current not correct"}), 400

    password_refresh = (str(new_password).lower()).replace(" ", "")

    create_fullName_refresh = (str(find_user.full_name).lower()).replace(" ", "")
    if password_refresh == create_fullName_refresh:
        return jsonify({"Error" : "Password not match profile data"}), 400
    
    create_email_refresh = (str(find_user.email).lower()).replace(" ", "")
    if password_refresh == create_email_refresh:
          return jsonify({"Error" : "Password not match profile data"}), 400
    
    create_phoneNumber_refresh = (str(find_user.phone_number).lower()).replace(" ", "")
    if password_refresh == create_phoneNumber_refresh:
        return jsonify({"Error" : "Password not match profile data"}), 400
    
    create_address_refresh = (str(find_user.address).lower()).replace(" ", "")
    if password_refresh == create_address_refresh:
        return jsonify({"Error" : "Password not match profile data"}), 400

    create_city_refresh = (str(find_user.city).lower()).replace(" ", "")
    if password_refresh == create_city_refresh:
        return jsonify({"Error" : "Password not match profile data"}), 400

    create_country_refresh = (str(find_user.country).lower()).replace(" ", "")
    if password_refresh == create_country_refresh:
        return jsonify({"Error" : "Password not match profile data"}), 400

    check_datetime_password = Password.query.with_entities(Password.password_used).order_by(Password.date.desc()).limit(3)
    list_password = []
    for per_password in check_datetime_password:
        for _ in per_password:
            list_password.append(per_password[0])
    for check_password in list_password:
        if check_password_hash(check_password, new_password):
            return jsonify({"error" : "the password must not match the last three passwords."}), 400
    
    
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



