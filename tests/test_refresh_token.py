from tests.data.data_signup import signup_valid

def test_refresh_token_in_headers(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    refresh_token = response_signup.json["refresh_token"]

    response_new_access_token = client.post("/refresh-token",  headers = {"Authorization" : f"Bearer {refresh_token}"})

    new_access_token = response_new_access_token.json["refresh_token_successfully"]["access_token"]
    new_refresh_token = response_new_access_token.json["refresh_token_successfully"]["refresh_token"]

    assert response_new_access_token.status_code == 201
    assert response_new_access_token.json["refresh_token_successfully"] == {"access_token" : new_access_token,
            "refresh_token" : new_refresh_token}



def test_access_token_in_headers(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]

    response_new_access_token = client.post("/refresh-token",  headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_new_access_token.status_code == 401
    assert response_new_access_token.json == {"Not Authentication" : "Invalid token, signature edited or wrong type token"}
