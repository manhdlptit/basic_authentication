from tests.data.data_signup import signup_valid

def test_get_new_access_token_with_refresh_token_in_headers(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    re_fresh_token = response_signup.json["re_fresh_token"]

    response_new_access_token = client.get("/refresh-token",  headers = {"Authorization" : f"Bearer {re_fresh_token}"})

    new_access_token = response_new_access_token.json["refresh_token_successfully"]["new_access_token"]
    new_refresh_token = response_new_access_token.json["refresh_token_successfully"]["new_refresh_token"]

    assert response_new_access_token.status_code == 201
    assert response_new_access_token.json["refresh_token_successfully"] == {"new_access_token" : new_access_token,
            "new_refresh_token" : new_refresh_token}


def test_get_new_access_token_with_accessToken_in_headers(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]

    response_new_access_token = client.get("/refresh-token",  headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_new_access_token.status_code == 422
    assert response_new_access_token.json == {'msg': 'Only refresh tokens are allowed'}
