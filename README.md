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

    python app.py

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

---

_return `jsonify` service for Frontend._
