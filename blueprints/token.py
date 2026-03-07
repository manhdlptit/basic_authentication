from flask import request, Flask, jsonify,Blueprint
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from model.model import User,db
import uuid

def get_token():
    data = request.headers.get("Auth")
    if data and data.startswith("Token") and len(data.split()) == 2:
        token = data.split(" ")[1]
        user = User.query.filter(User.token == token).first()
        if user:
            return user
    return None
        
