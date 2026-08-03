from dotenv import load_dotenv
load_dotenv()

import os

from flask import Flask

from app.model.model import db
from app.jwt.jwt import jwt
from app.python.change_password import change_password
from app.python.login import login
from app.python.signup import signup
from app.python.inf_user import inf_user
from app.python.logout import logout
from app.python.refresh_token import refresh_token
from app.python.forgot_password import forgot_password
from datetime import timedelta

def create_app(config_overrides= None):
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES")))
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES")))

    if config_overrides:
        app.config.update(config_overrides)
    
    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(change_password)
    app.register_blueprint(login)
    app.register_blueprint(signup)
    app.register_blueprint(inf_user)
    app.register_blueprint(logout)
    app.register_blueprint(refresh_token)
    app.register_blueprint(forgot_password)

    print(os.getenv("SECRET_KEY"))
    return app
