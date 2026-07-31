## Run app & Install

### 1. Create env

    python3 -m venv env

###

### 2. Activate env

Firstly, open Terminal and run:

- **With macOS/Linux:**
  ```bash
  source env/bin/activate
  ```
- **With window:**
  ```bash
  .\env\Scripts\activate
  ```

### 3. Install library

    pip install -r requirements.txt

### 4. Run app

    python main.py

###

### 5. Run test

    pytest -vv

###

## Summary the Test Cases

Write about testcase forgot-password, login, signup

### 1. Signup

- ✅ **Sign_up_successful** :201
- ❌ **Sign_up_null_username** :400
- ❌ **Email existed** :400
- ❌ **PhoneNumber existed** :400
- ❌ **Password not the same** :400
- ❌ **Password is short** :400
- ✅ **Password is 8 character** :201

### 2. Login

- ✅ **Login successful**:200
- ❌ **Wrong password**:400
- ❌ **Not token in header**:401
- ❌ **Login with username not existed**:400
- ❌ **Login with phoneNumber is None**:400
- ❌ **Null password**:400
- ❌ **Wrong format token**:401
- ❌ **Wrong token**:401

### 3. Forgot Password

- ✅ **Change password successful**:200
- ❌ **Inf profile invalid**:400
- ✅ **Login with default password successful**:200
- ❌ **Not url forgot password**:400
- ❌ **Username not signup**:400
- ❌ **Not token in header**:401
