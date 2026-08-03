from tests.data.data_signup import signup_valid
from tests.data.data_login import (login_with_email_and_login_valid,
                                   login_with_phoneNumber_is_null,
                                   login_with_phoneNumber_and_password_is_null,
                                   login_with_email_but_wrong_password,
                                   login_with_email_not_existed_in_DB)


def test_login_successfully(client):
    payload_signup = signup_valid()
    client.post("/signup", json = payload_signup)

    payload_login = login_with_email_and_login_valid()
    response_login = client.post("/login", json = payload_login)

    access_token = response_login.json["access_token"]
    refresh_token = response_login.json["refresh_token"]

    assert response_login.status_code == 200
    assert response_login.json == {"access_token" : access_token, "refresh_token" : refresh_token}



def test_phoneNumber_is_None(client):
    payload_signup = signup_valid()
    client.post("/signup", json = payload_signup)
    
    payload_login = login_with_phoneNumber_is_null()
    response_login = client.post("/login", json = payload_login)
    
    assert response_login.status_code == 400
    assert response_login.json == {"Error" : "Not null username"}



def test_password_is_None(client):
    payload_signup = signup_valid()
    client.post("/signup", json = payload_signup)
        
    payload_login = login_with_phoneNumber_and_password_is_null()
    response_login = client.post("/login", json = payload_login)
        
    assert response_login.status_code == 400
    assert response_login.json == {"Error" : "Not null password"}



def test_wrong_password(client):
    payload_signup = signup_valid()
    client.post("/signup", json = payload_signup)
            
    payload_login = login_with_email_but_wrong_password()
    response_login = client.post("/login", json = payload_login)
            
    assert response_login.status_code == 400
    assert response_login.json == {"Error" : "Wrong email or phone number or password"}



def test_email_not_signup_yet(client):
    payload_signup = signup_valid()
    client.post("/signup", json = payload_signup)
            
    payload_login = login_with_email_not_existed_in_DB()
    response_login = client.post("/login", json = payload_login)
            
    assert response_login.status_code == 400
    assert response_login.json == {"Error" : "Wrong email or phone number or password"}
