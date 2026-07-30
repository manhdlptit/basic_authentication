from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, current_user


inf_user = Blueprint("inf_user", __name__)

@inf_user.route("/inf-user", methods = ["GET"])
@jwt_required()
def all_inf_user():
    return jsonify({"inf" : {
        "full name" : current_user.full_name,
        "email" : current_user.email,
        "phone number" : current_user.phone_number,
        "address" : current_user.address,
        "city" : current_user.city,
        "country" : current_user.country
    }}), 200

