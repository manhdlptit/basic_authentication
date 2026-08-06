import pytest
import datetime

from app import create_app
from app.model.model import db

@pytest.fixture
def cr_app():
    app = create_app({
        "TESTING" : True,
        "SQLALCHEMY_DATABASE_URI" : "sqlite:///:memory:",
        "SECRET_KEY" : "14bf4650a7364ae68e73ff125e848ba1",
        "JWT_ACCESS_TOKEN_EXPIRES" : datetime.timedelta(minutes=15),
        "JWT_REFRESH_TOKEN_EXPIRES" : datetime.timedelta(days=30)
    })
            
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(cr_app):
    return cr_app.test_client()


