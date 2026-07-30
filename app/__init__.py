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
from app.python.re_fresh_token import re_tk
from app.python.forgot_password import forgot_password
from datetime import timedelta

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "295cf9403f60488db75622286b422803")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///user.db")
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 5)))
    
    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(change_password)
    app.register_blueprint(login)
    app.register_blueprint(signup)
    app.register_blueprint(inf_user)
    app.register_blueprint(logout)
    app.register_blueprint(re_tk)
    app.register_blueprint(forgot_password)

    with app.app_context():
        db.create_all()

    return app
