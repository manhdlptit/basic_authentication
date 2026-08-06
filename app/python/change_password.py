from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

from app.model.model import User, Password, db

from datetime import datetime

change_password = Blueprint("change_password", __name__)

@change_password.route("/change-password", methods = ["POST"])
@jwt_required()
def change_password_when_logged_in():
    new_password = request.json.get("new_password")

    id = get_jwt_identity()
                
    find_user = User.query.filter(User.id == int(id)).first()

    if not new_password or not new_password.replace(" ",""):
        return jsonify({"Error" : "Must input new password"}), 400

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





