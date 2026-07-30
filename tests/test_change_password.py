from tests.data.data_signup import *
from tests.data.data_login import *
from tests.data.data_forgotPassword import *


def test_change_password_firstTime_with_access_token_and_successfully(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]

    payload_change_password = password_change_first_time()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password.status_code == 200
    assert response_change_password.json == {"successfully" : "change password successfully"}



def test_change_password_secondTime_with_access_token_and_successfully(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]

    payload_change_password_firstTime = password_change_first_time()
    response_change_password_firstTime = client.post("/change-password", json = payload_change_password_firstTime, headers = {"Authorization" : f"Bearer {access_token}"})

    payload_change_password_secondTime = password_change_second_time()
    response_change_password_secondTime = client.post("/change-password", json = payload_change_password_secondTime, headers = {"Authorization" : f"Bearer {access_token}"})
    
    assert response_change_password_secondTime.status_code == 200
    assert response_change_password_secondTime.json == {"successfully" : "change password successfully"}



def test_change_password_thirdTime_with_access_token_and_successfully(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]

    payload_change_password_firstTime = password_change_first_time()
    response_change_password_firstTime = client.post("/change-password", json = payload_change_password_firstTime, headers = {"Authorization" : f"Bearer {access_token}"})

    payload_change_password_secondTime = password_change_second_time()
    response_change_password_secondTime = client.post("/change-password", json = payload_change_password_secondTime, headers = {"Authorization" : f"Bearer {access_token}"})

    payload_change_password_thirdTime = password_change_third_time()
    response_change_password_thirdTime = client.post("/change-password", json = payload_change_password_thirdTime, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password_thirdTime.status_code == 200
    assert response_change_password_thirdTime.json == {"successfully" : "change password successfully"}



def test_change_password_with_access_token_but_match_the_last_3_password(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]

    payload_change_password_firstTime = password_change_first_time()
    response_change_password_firstTime = client.post("/change-password", json = payload_change_password_firstTime, headers = {"Authorization" : f"Bearer {access_token}"})

    payload_change_password_secondTime = password_change_second_time()
    response_change_password_secondTime = client.post("/change-password", json = payload_change_password_secondTime, headers = {"Authorization" : f"Bearer {access_token}"})

    payload_change_password_thirdTime = password_change_third_time_same_like_first_time()
    response_change_password_thirdTime = client.post("/change-password", json = payload_change_password_thirdTime, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password_thirdTime.status_code == 400
    assert response_change_password_thirdTime.json == {'error': 'the password must not match the last three passwords.'}



def test_change_password_and_password_like_fullname(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]

    payload_change_password = password_same_like_full_name()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password.status_code == 400
    assert response_change_password.json == {"Error" : "Password not match profile data"}



def test_change_password_fourth_time_like_first_time(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)

    access_token = response_signup.json["access_token"]

    payload_change_password_firstTime = password_change_first_time()
    response_change_password_firstTime = client.post("/change-password", json = payload_change_password_firstTime, headers = {"Authorization" : f"Bearer {access_token}"})

    payload_change_password_secondTime = password_change_second_time()
    response_change_password_secondTime = client.post("/change-password", json = payload_change_password_secondTime, headers = {"Authorization" : f"Bearer {access_token}"})

    payload_change_password_thirdTime = password_change_third_time()
    response_change_password_thirdTime = client.post("/change-password", json = payload_change_password_thirdTime, headers = {"Authorization" : f"Bearer {access_token}"})

    payload_change_password_fourthTime = password_change_fourth_time()
    response_change_password_fourthTime = client.post("/change-password", json = payload_change_password_fourthTime, headers = {"Authorization" : f"Bearer {access_token}"})

    assert response_change_password_fourthTime.status_code == 200
    assert response_change_password_fourthTime.json == {"successfully" : "change password successfully"}


def test_change_password_with_current_password_correct_and_have_access_token(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)
    
    access_token = response_signup.json["access_token"]
    
    payload_change_password = password_change_first_time()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token}"})
    
       
    assert response_change_password.status_code == 200
    assert response_change_password.json == {"successfully" : "change password successfully"}


def test_change_password_with_current_password_incorrect_and_have_access_token(client):
    payload_signup = signup_valid()
    response_signup = client.post("/signup", json = payload_signup)
    
    access_token = response_signup.json["access_token"]
    
    payload_change_password = change_password_first_time_but_current_password_wrong()
    response_change_password = client.post("/change-password", json = payload_change_password, headers = {"Authorization" : f"Bearer {access_token}"})
    
       
    assert response_change_password.status_code == 400
    assert response_change_password.json == {"Error" : "Password current not correct"}