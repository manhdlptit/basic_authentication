from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

from app.data.datetime_jwt import expires_delta_refresh
from app.model.model import User, db



login = Blueprint("login", __name__)

@login.route("/login", methods = ["POST"])
def login_user():
    data = request.get_json()
    
    email = data.get("email")
    phone_number = data.get("phone_number")
    password = data.get("password")
    
    if ((email or phone_number) and password) is None:
        return jsonify({"Error" : "Not null any value"}), 400
    
    check_user = User.query.filter((User.email == email) | (User.phone_number == phone_number)).first()
    if check_user is None:
        return jsonify({"Error" : "Wrong email or phone number or password"}), 400
    
    if check_password_hash(check_user.password, password) is False:
        return jsonify({"Error" : "Wrong email or phone number or password"}), 400
    
    access_token = create_access_token(identity=check_user)
    re_fresh_token = create_refresh_token(identity=check_user, expires_delta=expires_delta_refresh)
    
    db.session.commit()

    return jsonify(access_token = access_token, re_fresh_token = re_fresh_token), 200