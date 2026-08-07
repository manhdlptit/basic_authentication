from flask_jwt_extended import JWTManager

from app.model.model import db, User, Password, BlockList

from flask import jsonify

jwt = JWTManager()

@jwt.user_identity_loader
def loader_identity(user):
    return str(user.id)

@jwt.user_lookup_loader
def lookup_loader(header, payload):
    user_id = payload["sub"]
    find_user = User.query.filter(User.id == user_id).first()
    return find_user



@jwt.token_in_blocklist_loader
def check_block_list(header, payload):
    jti = payload['jti']
    check_jwt_block_list = BlockList.query.filter(BlockList.jti == jti).first()
    return check_jwt_block_list is not None


@jwt.expired_token_loader
def return_message_expired_token(header, payload):
    return jsonify({"Not Authentication" : "Token expired"}), 401


@jwt.invalid_token_loader
def return_message_invalid_token(error):
    return jsonify({"Not Authentication" : "Invalid token, signature edited or wrong type token"}), 401


@jwt.revoked_token_loader
def return_message_token_revoked(header, payload):
    return jsonify({"Not Authentication" : "Token has been revoked"}), 401


@jwt.unauthorized_loader
def return_message_token_is_missed(error):
    return jsonify({"Not Authentication" : "Missing Authorization Header"}), 401



