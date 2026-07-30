from flask_jwt_extended import JWTManager

from app.model.model import db, User, Password, BlockList

jwt = JWTManager()

@jwt.user_identity_loader
def loader_identity(user):
    return str(user.id)

@jwt.user_lookup_loader
def lookup_loader(header, payload):
    id = payload["sub"]
    find_user = User.query.filter(User.id == id).first()
    return find_user



@jwt.token_in_blocklist_loader
def check_block_list(header, payload):
    jti = payload['jti']
    check_jwt_block_list = BlockList.query.filter(BlockList.jti == jti).first()
    return check_jwt_block_list is not None