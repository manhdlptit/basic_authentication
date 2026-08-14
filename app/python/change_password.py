from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

from app.model.model import User, Password, db

from datetime import datetime

change_password = Blueprint("change_password", __name__)

@change_password.route("/change-password", methods = ["POST"])
@jwt_required()
def change_password_when_logged_in():
    data = request.get_json(silent = True)

    current_password = data.get("current_password")
    new_password = data.get("new_password")
    
    id_user_get = get_jwt_identity()
    
    find_user = User.query.filter(User.id == int(id_user_get)).first()

    if not find_user:
        return jsonify({"Error": "Not authenticated"}), 401

    if not current_password or not check_password_hash(find_user.password, current_password):
        return jsonify({"Error": "Current password is incorrect"}), 400

    if not new_password or not new_password.replace(" ",""):
        return jsonify({"Error" : "Must input new password"}), 400

    if len(new_password) < 8 or len(new_password) > 32:
            return jsonify({"Error" : "Password between 8 and 32 characters"}), 400

    normalized_password = new_password.lower().replace(" ", "").strip()
    
    personal_info_fields = [
    find_user.full_name,
    find_user.email,
    find_user.phone_number,
    find_user.address,
    find_user.city,
    find_user.country,
    find_user.birthday
]
    new_list_normalized = [str(field).lower().replace(" ", "").strip() for field in personal_info_fields if field]

    for field in new_list_normalized:
        if normalized_password == field:
            return jsonify({"Error": "New password must not match personal info"}), 400
    
    check_datetime_password = Password.query.filter_by(id_user = find_user.id).with_entities(Password.password_used).order_by(Password.date.desc()).limit(3)
    
    list_password = [per_password[0] for per_password in check_datetime_password]  
    for old_hash_password in list_password:
        if check_password_hash(old_hash_password, new_password):
            return jsonify({"Error" : "The password must not match the last three passwords."}), 400
    
    password = generate_password_hash(new_password)
    find_user.password = password

    datetime_create_password = datetime.now()
    new_inf_password = Password(date=datetime_create_password, password_used=password, id_user=find_user.id)

    db.session.add(new_inf_password)

    list_id_user_not_delete = Password.query.filter_by(id_user = find_user.id).with_entities(Password.id).order_by(Password.date.desc()).limit(3)



    list_id_not_delete = [field[0] for field in list_id_user_not_delete]

    list_users_delete = Password.query.filter(Password.id.not_in(list_id_not_delete), Password.id_user == find_user.id).all()

    for per_id in list_users_delete:
        db.session.delete(per_id)

    

    db.session.commit()

    return jsonify({"Successfully" : "Change password successfully"}), 200




