from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token

from app.model.model import User

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

    if not full_name or not full_name.replace(" ",""):
        return jsonify({"Error" : "Missing fullname"}), 400

    if not phone_number or not phone_number.replace(" ","") :
        return jsonify({"Error" : "Missing phone number"}), 400
    
    if not email or not email.replace(" ",""):
        return jsonify({"Error" : "Missing email"}), 400

    find_user = User.query.filter((User.email == email) | (User.phone_number == phone_number)).first()
    if not find_user:
        return jsonify({"error" : "information is not the same"}), 400
    if not (find_user.address == address and find_user.country == country and find_user.city == city and find_user.full_name == full_name):
        return jsonify({"error" : "information is not the same"}), 400

    access_token = create_access_token(identity=find_user)
    refresh_token = create_refresh_token(identity=find_user) 


    return jsonify({
        "successfully" : "go to \"/change-password\"",
        "access_token" : access_token,
        "refresh_token" : refresh_token
        }), 200