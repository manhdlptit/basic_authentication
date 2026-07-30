from tests.data.data_forgotPassword import *
from tests.data.data_login import *
from tests.data.data_signup import *

import time


def test_access_protect_api_with_access_token_success(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)
    
    access_token = response_signup.json["access_token"]

    print()

    response_inf_user = client.get("/inf-user", headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_inf_user.status_code == 200
    assert response_inf_user.json == {"inf" : {
        "full name" : payload_signup["full_name"],
        "email" : payload_signup["email"],
        "phone number" : payload_signup["phone_number"],
        "address" : payload_signup["address"],
        "city" : payload_signup["city"],
        "country" : payload_signup["country"]
    }}



def test_access_protect_api_with_access_token_expired(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)
    
    access_token = response_signup.json["access_token"]

    time.sleep(301)

    response_inf_user = client.get("/inf-user", headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_inf_user.status_code == 401
    assert response_inf_user.json == {"msg": "Token has expired"}



def test_access_protect_api_with_access_token_revoked(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)
    
    access_token = response_signup.json["access_token"]
    re_fresh_token = response_signup.json["re_fresh_token"]

    response_logout_access_token = client.get("/logout", headers = {"Authorization" : f"Bearer {access_token}"})


    assert response_logout_access_token.status_code == 200
    assert response_logout_access_token.json == {"log out successfully " :"log out successfully"}

    response_logout_refresh_token = client.get("/logout", headers = {"Authorization" : f"Bearer {re_fresh_token}"})

    assert response_logout_refresh_token.status_code == 200
    assert response_logout_refresh_token.json == {"successfully" : "revoked refresh token"}

    response_inf_user = client.get("/inf-user", headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_inf_user.status_code == 401
    assert response_inf_user.json == {"msg" : "Token has been revoked"}



def test_access_protect_api_with_no_headers(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)
    
    response_logout_access_token = client.get("/logout")

    assert response_logout_access_token.status_code == 401
    assert response_logout_access_token.json == {'msg': 'Missing Authorization Header'}



def test_access_protect_api_with_access_token_not_valid(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]
    
    response_logout_access_token = client.get("/logout", headers = {"Authorization" : f"Bearer {access_token+"k"}"})

    assert response_logout_access_token.status_code == 422
    assert response_logout_access_token.json == {'msg': 'Signature verification failed'}



