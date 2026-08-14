# Create JWT, protect api with access_token - JWT

This project include building code about authentication and the testcase relative with **Flask**, **Pytest**, **Flask-sqlalchemy** and **Flask-jwt-extended**.

## Coding & Install

### 1. Version python

    Use Python version 3.10

### 2. Install env

    python3 -m venv env

### 3. Activate env

Firstly, open Terminal and run:

- **With macOS/Linux:**
  ```bash
  source env/bin/activate
  ```
- **With window:**
  ```bash
  .\env\Scripts\activate
  ```

### 4. Install library

    pip install -r requirements.txt

### 5. Run testcase

    pytest -vv

###

### 6. Run app

    python main.py

###

## Several config and describe about project

### 1. JWT

- Secret_key for both jwt and secret_key serve are used with **"SECRET_KEY"** in file **.env**
- Access token expire per 5 minutes
- Refresh token is created to create new access token
- Refresh token expire per 30 days

### 2. Feature change_password

- User **POST** method for save history password in DB, not use **PUT**

### 3. About project

- Config in file **init.py**, data about secret_key, uri_db, expired token of access token and expired token of refresh token save in file **.env**
- Every api important are protected with access_token(JWT)
- Completely eliminate the type **Auth: Token 'uuid'**
- Add many data for testcase in the future, several data not use in this project

## Summary the Test Cases

Write new testcase forgot-password, login, signup because completely eliminate the type **"Auth: Token 'uuid'"**, add testcase about test_protect_api(create, protect, revoke), test_case_refresh_token(create new token), test_case_logout, test_case_change-password

### 1. Signup

- ✅ **Sign_up_successful_not_null_any_value** :201
- ✅ **Sign_up_successful_null_value_not_important** :201
- ❌ **Test_sign_up_null_phoneNumber** :400
- ❌ **Test_sign_up_null_email** :400
- ❌ **Test_sign_up_null_input_password** :400
- ❌ **Email existed** :400
- ❌ **PhoneNumber existed** :400
- ❌ **Two password not same** :400
- ❌ **Password is short** :400
- ❌ **Fullname_is_space_white** :400
- ❌ **PhoneNumber_is_space_white** :400
- ❌ **Email_is_space_white** :400
- ❌ **Input_password_is_space_white** :400

### 2. Login

- ✅ **Login successful**:200
- ❌ **Login with phoneNumber is None**:400
- ❌ **Null password**:400
- ❌ **Wrong password**:400
- ❌ **Login with email not existed**:400
- ❌ **Login with username is whitespace**:400
- ❌ **Login with password is whitespace**:400

### 3. Forgot Password

- ✅ **Inf valid, change password successful**:200
- ❌ **Inf profile not valid**:400
- ✅ **Null_value_not_important_successfully**:200
- ❌ **Fullname_is_space_white** :400
- ❌ **PhoneNumber_is_space_white** :400
- ❌ **Email_is_space_white** :400

### 4. Logout

- ✅ **Logout successful**:200

### 5. Protect api

- ✅ **Having access token, access protect api**:200
- ❌ **Access_token expired**:401
- ❌ **Access_token revoked**:401
- ❌ **Access_token not in headers**:401
- ❌ **Access_token invalid, signature edited**:401

### 6. Refresh_token

- ✅ **Refresh_token_headers**:201
- ❌ **Access_token headers**:401

### 7. Change password

- ❌ **Not token in headers**:401
- ❌ **Wrong current password**:400
- ✅ **Change password first time successfully**:200
- ✅ **Change password second time successfully**:200
- ✅ **Change password third time successfully**:200
- ✅ **Password fourth time same password signup successfully**:200
- ❌ **New password match 3 last time**:400
- ❌ **New password like fullname user**:400
- ❌ **New password like email user**:400
- ❌ **New password like phoneNumber user**:400
- ❌ **New password is whitespace**:400
- ✅ **Password user1 same password user2, user2 change password successfully**:200

## Call API Change-password - [DT-03]

To call API change password, I use "POSTMAN".

### 1.Create data signup, and call signup API to take access_token

#### 1. Call signup API

`http://127.0.0.1:9999/signup ` , method : "POST"

#### 2.Add data in body, type row -> json

Example data

```
{
    "full_name" : "Le Duc Manh",
    "phone_number" : "0397618712",
    "email" : "manhdl.ptit@gmail.com",
    "input_password" : "Lwman8_1812",
    "check_password": "Lwman8_1812",
    "address" : "19,MP,VT,PT",
    "country" : "VN",
    "city" : "VT"
}
```

#### 3. Take access token

Press "Send"

Get `value` of `dictionary`, with `key` is "access_token"

Example output

```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjYzNDcxMCwianRpIjoiYmU0MTM0NWItZWZlMS00Yjg4LWI2YjgtNjNhZDA3NThiYThkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODY2MzQ3MTAsImNzcmYiOiI1ZDY2ZWU4OS1lYjFiLTQ5YWEtOWU2ZC1mOTlkZGMxMTc4MDciLCJleHAiOjE3ODY2MzUwMTB9.0njq_DKtzXVJmSoUfGiGqld-7VzVJZXyujYqaYeaL4E",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjYzNDcxMCwianRpIjoiZjQ3MGNmMDUtZTNlOS00MjMzLTlkNTQtYzVhZDJlZmIyZmQ3IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiIxIiwibmJmIjoxNzg2NjM0NzEwLCJjc3JmIjoiMTk1OTFkZjItYzE3Ny00MGFiLWIzY2EtYjRhMmFkZThkZjlkIiwiZXhwIjoxNzg5MjI2NzEwfQ.QCDiPpITGnFZXSs4yZudC0amq5BlQkXVNCjOLXw9Ctg"
}
```

### 2.Call change password API and change password

#### 1. Call change password API

`http://127.0.0.1:9999/change-password` , method : "POST"

#### 2.Add access token in headers

Go to "Authorization", choose "Bearer Token"

Paste "access_token" got in token input

#### 3.Add data in body, type row -> json, and send data to server

Example data change password

```
{
    "current_password" : "Lwman8_1812",
    "new_password" : "Manhdl.ptit@2026"
}
```

Press "Send"

#### 4. Get information Successfully or Error

---

_return `jsonify` service for Frontend._
