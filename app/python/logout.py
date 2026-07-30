from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity

from app.model.model import db, BlockList

logout = Blueprint("logout", __name__)

@logout.route("/logout", methods = ["GET"])
@jwt_required(verify_type=False)
def logout_user():
    payload = get_jwt()

    jti = payload["jti"]

    type_jwt = payload["type"]

    new_block_list = BlockList(jti=jti)

    db.session.add(new_block_list)

    db.session.commit()

    if type_jwt == "access":
        return jsonify({"log out successfully " :"log out successfully"}), 200
    if type_jwt == "refresh" :
        return jsonify({"successfully" : "revoked refresh token"}), 200