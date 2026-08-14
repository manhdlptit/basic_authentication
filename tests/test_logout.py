from tests.data.data_signup import signup_valid


def test_logout_successfully(client):
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
