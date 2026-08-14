from tests.data.data_signup import signup_valid, signup_valid_second
from tests.data.data_login import (login_with_email_and_login_valid, 
                                   login_with_password_change_first_time,
                                   login_with_password_change_second_time,
                                   login_with_password_change_third_time)
from tests.data.data_changePassword import (wrong_current_password,
                                            change_password_first_time,
                                            change_password_second_time,
                                            change_password_third_time,
                                            change_password_third_time_same_password_signup,
                                            change_password_fourth_time_same_password_signup,
                                            change_password_whitespace,
                                            password_like_full_name,
                                            password_like_email,
                                            password_like_phone_number       
                                            )

def test_change_password_not_token(client):
    payload_change_password = change_password_first_time()
    response_change_password = client.post("/change-password", json = payload_change_password)

    assert response_change_password.status_code == 401
    assert response_change_password.json == {"Not Authentication": "Missing Authorization Header"}



def test_wrong_current_password(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token_signup = response_signup.json["access_token"]

    payload_change_password = wrong_current_password()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token_signup}"})

    assert response_change_password.status_code == 400
    assert response_change_password.json == {"Error": "Current password is incorrect"}



def test_change_password_first_time_successfully(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token_signup = response_signup.json["access_token"]
   
    payload_change_password = change_password_first_time()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token_signup}"})

    assert response_change_password.status_code == 200
    assert response_change_password.json == {
            "Successfully" : "Change password successfully"}

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
            "Successfully" : "Change password successfully"}

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
            "Successfully" : "Change password successfully"}

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
            "Successfully" : "Change password successfully"}

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

    payload_change_password_third_time = change_password_third_time_same_password_signup()
    response_change_password_third_time = client.post("/change-password", json = payload_change_password_third_time, headers = {"Authorization" : f"Bearer {access_token_signup}"})

    assert response_change_password_third_time.status_code == 400
    assert response_change_password_third_time.json == {"Error": "The password must not match the last three passwords."}



def test_change_password_match_fullname(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token_signup = response_signup.json["access_token"]
   
    payload_change_password = password_like_full_name()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token_signup}"})


    assert response_change_password.status_code == 400
    assert response_change_password.json == {"Error" : "New password must not match personal info"}



def test_change_password_match_email(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token_signup = response_signup.json["access_token"]
   
    payload_change_password = password_like_email()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token_signup}"})


    assert response_change_password.status_code == 400
    assert response_change_password.json == {"Error" : "New password must not match personal info"}



def test_change_password_match_phone_number(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token_signup = response_signup.json["access_token"]
   
    payload_change_password = password_like_phone_number()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token_signup}"})


    assert response_change_password.status_code == 400
    assert response_change_password.json == {"Error" : "New password must not match personal info"}



def test_change_password_is_white_space(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]

    payload_change_password = change_password_whitespace()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password.status_code == 400
    assert response_change_password.json == {"Error" : "Must input new password"}



def test_password_user1_same_password_user2(client):
    payload_signup1 = signup_valid()
    client.post("/signup", json = payload_signup1)

    print(payload_signup1)

    payload_signup2 = signup_valid_second()
    response_signup2 = client.post("/signup", json = payload_signup2)

    print(payload_signup2)

    access_token = response_signup2.json["access_token"]

    payload_change_password = change_password_first_time()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password.status_code == 200
    assert response_change_password.json == {"Successfully" : "Change password successfully"}


 


