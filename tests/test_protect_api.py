from tests.data.data_signup import signup_valid

from freezegun import freeze_time

import datetime


def test_access_token_valid(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)
    
    access_token = response_signup.json["access_token"]

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



def test_access_token_expired(client):
    with freeze_time("2000-01-01 12:00:00") as frozen_time:
        payload_signup = signup_valid()
        response_signup = client.post("/signup", json = payload_signup)
    
        access_token = response_signup.json["access_token"]

        frozen_time.tick(datetime.timedelta(minutes=15))

        response_inf_user = client.get("/inf-user", headers = {"Authorization" : f"Bearer {access_token}"})

        assert response_inf_user.status_code == 401
        assert response_inf_user.json == {"Not Authentication" : "Token expired"}



def test_access_token_revoked(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)
    
    access_token = response_signup.json["access_token"]
    refresh_token = response_signup.json["refresh_token"]

    response_logout_access_token = client.post("/logout", headers = {"Authorization" : f"Bearer {access_token}"})


    assert response_logout_access_token.status_code == 200
    assert response_logout_access_token.json == {"Successfully": "access token has revoked"}

    response_logout_refresh_token = client.post("/logout", headers = {"Authorization" : f"Bearer {refresh_token}"})

    assert response_logout_refresh_token.status_code == 200
    assert response_logout_refresh_token.json == {"Successfully" : "revoked refresh token"}

    response_inf_user = client.get("/inf-user", headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_inf_user.status_code == 401
    assert response_inf_user.json == {"Not Authentication" : "Token has been revoked"}



def test_no_access_token_headers(client):
    payload_signup = signup_valid()
    client.post("/signup", json = payload_signup)
    
    response_logout_access_token = client.post("/logout")

    assert response_logout_access_token.status_code == 401
    assert response_logout_access_token.json == {'Not Authentication': 'Missing Authorization Header'}



def test_access_token_invalid(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]
    
    response_logout_access_token = client.post("/logout", headers = {"Authorization" : f"Bearer {access_token}k"})

    assert response_logout_access_token.status_code == 401
    assert response_logout_access_token.json == {"Not Authentication" : "Invalid token, signature edited or wrong type token"}



