from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

from app.model.model import User


login = Blueprint("login", __name__)

@login.route("/login", methods = ["POST"])
def login_user():
    data = request.get_json(silent= True)
    
    username = data.get("username", None)
    password = data.get("password", None)

    if not username or not (username.replace(" ","")).strip():
        return jsonify({"Error" : "Not null username"}), 400

    if not password or not (password.replace(" ","")).strip():
        return jsonify({"Error" : "Not null password"}), 400

    check_user = User.query.filter((User.email == username) | (User.phone_number == username)).first()
    if check_user is None:
        return jsonify({"Error" : "Wrong email or phone number or password"}), 400
    
    if check_password_hash(check_user.password, password) is False:
        return jsonify({"Error" : "Wrong email or phone number or password"}), 400
    
    access_token = create_access_token(identity=check_user)
    refresh_token = create_refresh_token(identity=check_user)

    ids_to_exclude = [1, 2, 3]
    users = User.query.filter(User.id.not_in(ids_to_exclude)).all()

    print(users)
    
    return jsonify(access_token = access_token, refresh_token = refresh_token), 200