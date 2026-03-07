from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from blueprints.forgot_password import forget
from blueprints.signup import signup
from blueprints.login import login
from model.model import db, User

app = Flask(__name__)

app.config["SECRET_KEY"] = "manhdl"
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///user.db")
# app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

@app.route("/")
def get_token():
    data = request.headers.get("Auth")
    if data or data.startswith("Token") and len(data.split()) == 2:
        return jsonify({"error" : len(data.split())})


if __name__ == "__main__":
    app.run(debug=True, port= 8888)