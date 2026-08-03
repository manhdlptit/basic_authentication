from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash

from app.model.model import User, Password, db

from datetime import datetime

change_password = Blueprint("change_password", __name__)

@change_password.route("/change-password", methods = ["POST"])
@jwt_required()
def change_password_when_logged_in():
    new_password = request.json.get("new_password")

    id = get_jwt_identity()
                
    find_user = User.query.filter(User.id == int(id)).first()

    if len(new_password) < 8 or len(new_password) > 32:
        return jsonify({"Error" : "Password between 8 and 32 characters"}), 400
    
    password = generate_password_hash(new_password)
    find_user.password = password

    datetime_create_password = datetime.now()
    new_inf_password = Password(date=datetime_create_password, password_used=password, id_user=find_user.id)

    db.session.add(new_inf_password)
    db.session.commit()

    return jsonify({"successfully" : "change password successfully"}), 200





