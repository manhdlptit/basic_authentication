from flask import Blueprint, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required

from app.model.model import User


refresh_token = Blueprint("refresh_token", __name__)

@refresh_token.route("/refresh-token", methods = ["POST"])
@jwt_required(refresh=True, verify_type=True)
def create_new_token():
    id = get_jwt_identity()
    
    identity = User.query.filter(User.id == int(id)).first()
    new_access_token = create_access_token(identity=identity)
    new_refresh_token = create_refresh_token(identity=identity)

    return jsonify({"refresh_token_successfully" : {
        "access_token" : new_access_token,
        "refresh_token" : new_refresh_token
    }}), 201