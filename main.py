from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from blueprints.forgot_password import forget
from blueprints.signup import signup
from blueprints.login import login
from model.model import db

def create_app(config_overrides= None):

    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "default")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///user.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

    if config_overrides:
        app.config.update(config_overrides)

    db.init_app(app)

    app.register_blueprint(forget)
    app.register_blueprint(signup)
    app.register_blueprint(login)

    return app

app = create_app()
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port= 9999)