import pytest

from main import create_app
from model.model import db

@pytest.fixture
def cr_app():
    app = create_app({
        "TESTING" : True,
        "SQLALCHEMY_DATABASE_URI" : "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(cr_app):
    return cr_app.test_client()


