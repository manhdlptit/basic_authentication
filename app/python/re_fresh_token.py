from flask import Blueprint, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required

from app.data.datetime_jwt import expires_delta_refresh
from app.model.model import User


re_tk = Blueprint("re_tk", __name__)

@re_tk.route("/refresh-token", methods = ["GET"])
@jwt_required(refresh=True)
def create_new_token():
    id = get_jwt_identity()
    identity = User.query.filter(User.id == int(id)).first()
    new_access_token = create_access_token(identity=identity)
    new_refresh_token = create_refresh_token(identity=identity, expires_delta=expires_delta_refresh)

    return jsonify({"refresh_token_successfully" : {
        "new_access_token" : new_access_token,
        "new_refresh_token" : new_refresh_token
    }}), 201