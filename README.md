# Create JWT, protect api with access_token - JWT

This project include building code about authentication and the testcase relative with **Flask**, **Pytest**, **Flask-sqlalchemy** and **Flask-jwt-extended**.

## Coding & Install

### 1. Activate env

Firstly, open Terminal and run:

- **With macOS/Linux:**
  ```bash
  source env/bin/activate
  ```
- **With window:**
  ```bash
  .\env\Scripts\activate
  ```

### 2. Install library

    pip install -r requirements.txt

### 3. Run testcase

    pytest -vv

###

### 4. Run app

    python main.py

###

## Several config and describe about project

### 1. JWT

- The expired token of refresh token save in file **datetime_jwt.py**
- Secret_key for both jwt and secret_key serve are used with **"SECRET_KEY"** in file **.env**
- Access token expire per 5 minutes
- Refresh token is created to create new access token
- Refresh token expire in 31/12/2026

### 2. Feature change_password

- User **POST** method for save history password in DB, not use **PUT**

### 3. About project

- Config in file **init.py**, data about secret_key, uri_db, or expired token of access token save in file **.env**
- Every api important are protected with access_token(JWT)
- Completely eliminate the type **Auth: Token 'uuid'**
- Add many data for testcase in the future, several data not use in this project
- Create secret_key with uuid

## Summary the Test Cases

Write new testcase forgot-password, login, signup because completely eliminate the type **"Auth: Token 'uuid'"**, add testcase about test_protect_api(create, protect, revoke), test_case_refresh_token(create new token), test_case_logout

### 1. Signup

- ✅ **Sign_up_successful** :201
- ❌ **Test_sign_up_null_email_and_phoneNumber** :400
- ❌ **Email existed** :400
- ❌ **PhoneNumber existed** :400
- ❌ **Two password not same** :400
- ❌ **Password is short** :400

### 2. Login

- ✅ **Login successful**:200
- ❌ **Login with phoneNumber is None**:400
- ❌ **Null password**:400
- ❌ **Wrong password**:400
- ❌ **Login with email not existed**:400

### 3. Forgot Password

- ✅ **Inf valid, change password successful**:200
- ❌ **Inf profile not valid**:400
- ❌ **Null value**:400
- ✅ **Access change password api, change password successful**:200
- ❌ **Current password**:400

### 4. Logout

- ✅ **Logout successful**:200

### 5. Protect api

- ✅ **Having access token, access protect api**:200
- ❌ **Access_token expired**:401
- ❌ **Access_token revoked**:401
- ❌ **Access_token not in headers**:401
- ❌ **Access_token invalid, signature edited**:422

### 6. Refresh_token

- ✅ **Refresh_token_headers**:201
- ❌ **Access_token headers**:422

---

_return `jsonify` service for Frontend._
