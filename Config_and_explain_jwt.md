# Explain code and config

## 1. Config code

Config app imported from os, get the first parameter, the second parameter used preventive

`app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "295cf9403f60488db75622286b422803")`

`app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///user.db")`

`app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 5)))`

Only access_token has expiration in file .env, refresh token is configured in “app/data/datetime_jwt.py” because I want the refresh token expire in specific time

## 2. Config JWT

### Config data JWT save in app/jwt/jwt.py

Decorator “`user_identity_loader`” : is used to find user, save in payload in JWT, with key is “sub” and value is “id user”

Decorator “`user_lookup_loader`" : is used to query data user, get value from key “sub” in payload from JWT and use value to query user

Decorator “`token_in_blocklist_loader`" : is used to revoked token, get value from key “jti”, query in DB with value just received

Decorator `expired_token_loader` : is used to return message error when token expired

Decorator `invalid_token_loader` : is used to return message error when token invalid, signature is edited or wrong type token

Decorator `revoked_token_loader` : is used to return message error when token revoked

Decorator `unauthorized_loader` : is used to return message error when missing token in header

### Config datetime

Save in app/data/datetime_jwt.py with fresh_token

`target_time = datetime(2026,12,31,23,59,59)`

Expires at the beginning of 2027

Save in .env file with access_token

`app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 5)))`

Expires 5 minute after creation

## 3. Explain JWT in my coding

### 3.1. The parameters key is created automatic in payload

“fresh”, “iat”, “jti”, “type”, “nbf”, “csrf”, “exp”

The key “type” is “access” or “refresh” depend on what we create

The key “exp” depend on time we define

### 3.2. Create token JWT

Create access_token and refresh_token when login or signup, with identity is “id user”, save in payload with [“key:value”] is : [“sub” : id_user]

Time expire access_token is defined in init.py, function `create_access_token()` get automatic

Time expire refresh_token is defined in app/data/datetime_jwt.py, function `create_refresh_token()` with parameter name expires_delta and value is gotexpires_delta_refresh

### 3.3. Access api protected

The decorator `@jwt_required()` to require access_token in headers, if not in headers or wrong something, deny access

### 3.4. Refresh token

The decorator `@jwt_required()` with parameter name is refreshand value is True to require refresh_token in headers, if not in headers, send access_token or wrong something, deny refresh_token

### 3.5. Logout - revoke token

When send both access_token and refresh_token in headers, loggout successfully, save “jti” per token in DB. Decorator `token_in_blocklist_loader` query in DB to assess token valid or invalid(revoked) when send token in headers, if revoked, deny access.

### 3.6. Decode in signup

Function `decode_token` to decode token, is returned dict - key:value, take key like "sub" to return "id_user" or take key "exp" to return timestamp
