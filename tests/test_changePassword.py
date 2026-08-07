from tests.data.data_signup import signup_valid
from tests.data.data_login import (login_with_email_and_login_valid, 
                                   login_with_password_change_first_time,
                                   login_with_password_change_second_time,
                                   login_with_password_change_third_time)
from tests.data.data_changePassword import (change_password_first_time,
                                            change_password_second_time,
                                            change_password_third_time,
                                            change_password_fourth_time_same_password_signup,
                                            change_password_whitespace,
                                            password_like_full_name       
                                            )

def test_change_password_first_time_successfully(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token_signup = response_signup.json["access_token"]
   
    payload_change_password = change_password_first_time()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token_signup}"})

    assert response_change_password.status_code == 200
    assert response_change_password.json == {
            "successfully" : "change password successfully"}

    payload_login = login_with_password_change_first_time()
    response_login = client.post("/login", json = payload_login)

    access_token_login = response_login.json["access_token"]
    refresh_token_login = response_login.json["refresh_token"]

    assert response_login.status_code == 200
    assert response_login.json == {"access_token" : access_token_login, "refresh_token" : refresh_token_login}



def test_change_password_second_time_successfully(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token_signup = response_signup.json["access_token"]
   
    payload_change_password_first_time = change_password_first_time()
    client.post("/change-password", json = payload_change_password_first_time, headers = {"Authorization" : f"Bearer {access_token_signup}"})
   
    payload_change_password_second_time = change_password_second_time()
    response_change_password_second_time = client.post("/change-password", json = payload_change_password_second_time, headers = {"Authorization" : f"Bearer {access_token_signup}"})

    assert response_change_password_second_time.status_code == 200
    assert response_change_password_second_time.json == {
            "successfully" : "change password successfully"}

    payload_login = login_with_password_change_second_time()
    response_login = client.post("/login", json = payload_login)

    access_token_login = response_login.json["access_token"]
    refresh_token_login = response_login.json["refresh_token"]

    assert response_login.status_code == 200
    assert response_login.json == {"access_token" : access_token_login, "refresh_token" : refresh_token_login}



def test_change_password_third_time_successfully(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token_signup = response_signup.json["access_token"]
   
    payload_change_password_first_time = change_password_first_time()
    client.post("/change-password", json = payload_change_password_first_time, headers = {"Authorization" : f"Bearer {access_token_signup}"})
   
    payload_change_password_second_time = change_password_second_time()
    client.post("/change-password", json = payload_change_password_second_time, headers = {"Authorization" : f"Bearer {access_token_signup}"})
   
    payload_change_password_third_time = change_password_third_time()
    response_change_password_third_time = client.post("/change-password", json = payload_change_password_third_time, headers = {"Authorization" : f"Bearer {access_token_signup}"})

    assert response_change_password_third_time.status_code == 200
    assert response_change_password_third_time.json == {
            "successfully" : "change password successfully"}

    payload_login = login_with_password_change_third_time()
    response_login = client.post("/login", json = payload_login)

    access_token_login = response_login.json["access_token"]
    refresh_token_login = response_login.json["refresh_token"]

    assert response_login.status_code == 200
    assert response_login.json == {"access_token" : access_token_login, "refresh_token" : refresh_token_login}



def test_password_fourth_time_same_password_signup(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token_signup = response_signup.json["access_token"]
   
    payload_change_password_first_time = change_password_first_time()
    client.post("/change-password", json = payload_change_password_first_time, headers = {"Authorization" : f"Bearer {access_token_signup}"})
   
    payload_change_password_second_time = change_password_second_time()
    client.post("/change-password", json = payload_change_password_second_time, headers = {"Authorization" : f"Bearer {access_token_signup}"})
   
    payload_change_password_third_time = change_password_third_time()
    client.post("/change-password", json = payload_change_password_third_time, headers = {"Authorization" : f"Bearer {access_token_signup}"})

    payload_change_password_fourth_time = change_password_fourth_time_same_password_signup()
    response_change_password_fourth_time = client.post("/change-password", json = payload_change_password_fourth_time, headers = {"Authorization" : f"Bearer {access_token_signup}"})

    assert response_change_password_fourth_time.status_code == 200
    assert response_change_password_fourth_time.json == {
            "successfully" : "change password successfully"}

    payload_login = login_with_email_and_login_valid()
    response_login = client.post("/login", json = payload_login)

    access_token_login = response_login.json["access_token"]
    refresh_token_login = response_login.json["refresh_token"]

    assert response_login.status_code == 200
    assert response_login.json == {"access_token" : access_token_login, "refresh_token" : refresh_token_login}
        
    

def test_change_password_match_3_last_time(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token_signup = response_signup.json["access_token"]
   
    payload_change_password_first_time = change_password_first_time()
    client.post("/change-password", json = payload_change_password_first_time, headers = {"Authorization" : f"Bearer {access_token_signup}"})
   
    payload_change_password_second_time = change_password_second_time()
    client.post("/change-password", json = payload_change_password_second_time, headers = {"Authorization" : f"Bearer {access_token_signup}"})
   
    payload_change_password_third_time = change_password_fourth_time_same_password_signup()
    response_change_password_third_time = client.post("/change-password", json = payload_change_password_third_time, headers = {"Authorization" : f"Bearer {access_token_signup}"})

    assert response_change_password_third_time.status_code == 400
    assert response_change_password_third_time.json == {"error": "the password must not match the last three passwords."}



def test_change_password_match_profile_user(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token_signup = response_signup.json["access_token"]
   
    payload_change_password = password_like_full_name()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token_signup}"})


    assert response_change_password.status_code == 400
    assert response_change_password.json == {"Error" : "Password not match profile data"}



def test_change_password_is_white_space(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]

    payload_change_password = change_password_whitespace()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password.status_code == 400
    assert response_change_password.json == {"Error" : "Must input new password"}


