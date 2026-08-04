from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

from app.model.model import User, db, Password

from datetime import datetime

signup = Blueprint("signup", __name__)

@signup.route("/signup", methods = ["POST"])
def signup_user():
    data = request.get_json()

    full_name = data.get("full_name", None)  
    phone_number = data.get("phone_number", None)  
    email = data.get("email", None)  
    address = data.get("address", None)  
    country = data.get("country", None)  
    city = data.get("city", None)  
    input_password = data.get("input_password", None)  
    check_password = data.get("check_password", None)

    

    
    if not full_name.replace(" ",""):
        return jsonify({"Error" : "Missing fullname"}), 400
    
    if not phone_number.replace(" ","") or not email.replace(" ",""):
        return jsonify({"Error" : "Missing username"}), 400

    if not input_password.replace(" ",""):
        return jsonify({"Error" : "Missing password"}), 400
    
    find_phone_number = User.query.filter(User.phone_number == phone_number).first()
    find_email = User.query.filter(User.email == email).first()

    if find_phone_number is not None:
        return jsonify({"Error" : "Phone number existed !"}), 400
    
    if find_email is not None:
        return jsonify({"Error" : "Email existed !"}), 400
    
    if len(input_password) < 8 or len(input_password) > 32:
        return jsonify({"Error" : "Password between 8 and 32 characters"}), 400
    
    if input_password != check_password:
        return jsonify({"Error" : "Input password different check password"}), 400
    
    password = generate_password_hash(input_password)

    new_user = User(full_name=full_name, 
                    phone_number=phone_number, 
                    email=email,
                    address=address,
                    country=country,
                    city=city,
                    password=password
                    )
    db.session.add(new_user)
    db.session.flush()
    
    datetime_now = datetime.now()
    new_password = Password(password_used=password, date=datetime_now, id_user=new_user.id)
    db.session.add(new_password)

    db.session.commit()

    access_token = create_access_token(identity=new_user)
    refresh_token = create_refresh_token(identity=new_user)

    return jsonify(access_token = access_token, refresh_token = refresh_token), 201



