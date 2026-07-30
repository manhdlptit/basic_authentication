from tests.data.data_signup import *
from tests.data.data_login import *


def test_login_successfully_and_login_with_email(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    payload_login = login_with_email_and_login_valid()
    response_login = client.post("/login", json = payload_login)

    assert response_login.status_code == 200
    assert response_login.json["access_token"] is not None
    assert response_login.json["re_fresh_token"] is not None


def test_login_with_phoneNumber_is_None(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)
    
    payload_login = login_with_phoneNumber_is_null()
    response_login = client.post("/login", json = payload_login)
    
    assert response_login.status_code == 400
    assert response_login.json == {"Error" : "Not null any value"}


def test_login_with_phoneNumber_and_password_is_None(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)
        
    payload_login = login_with_phoneNumber_and_password_is_null()
    response_login = client.post("/login", json = payload_login)
        
    assert response_login.status_code == 400
    assert response_login.json == {"Error" : "Not null any value"}


def test_login_with_email_but_wrong_password(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)
            
    payload_login = login_with_email_but_wrong_password()
    response_login = client.post("/login", json = payload_login)
            
    assert response_login.status_code == 400
    assert response_login.json == {"Error" : "Wrong email or phone number or password"}


def test_login_with_email_not_exsited_in_db(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)
            
    payload_login = login_with_email_not_exsited_in_DB()
    response_login = client.post("/login", json = payload_login)
            
    assert response_login.status_code == 400
    assert response_login.json == {"Error" : "Wrong email or phone number or password"}