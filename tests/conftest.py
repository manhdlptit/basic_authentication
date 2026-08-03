import pytest
import datetime

from app import create_app
from app.model.model import db

@pytest.fixture
def cr_app():
    app = create_app({
        "TESTING" : True,
        "SQLALCHEMY_DATABASE_URI" : "sqlite:///:memory:",
        "JWT_ACCESS_TOKEN_EXPIRES" : datetime.timedelta(seconds=2)
    })
            
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(cr_app):
    return cr_app.test_client()


