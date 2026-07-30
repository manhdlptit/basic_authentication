import pytest

from main import app
from app.model.model import db

@pytest.fixture
def cr_app():
    app.config.update({
        "TESTING" : True,
        "SQLALCHEMY_URI_DATABASE" : "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(cr_app):
    return app.test_client()


