from tests.data.data_signup import signup_valid


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
