# Explain code and config

## 1. Config code

Config app imported from os, takes only one parameter

`app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")`

`app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")`

`app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES")))`

`app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES")))`

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

Save in .env file with access_token and refresh_token

`app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES")))`

Expires 5 minute after creation

`app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES")))`

Expires 30 day after creation

## 3. Explain JWT in my coding

### 3.1. The parameters key is created automatic in payload

“fresh”, “iat”, “jti”, “type”, “nbf”, “csrf”, “exp”

The key “type” is “access” or “refresh” depend on what we create

The key “exp” depend on time we define

### 3.2. Create token JWT

Create access_token and refresh_token when login or signup, with identity is “id user”, save in payload with [“key:value”] is : [“sub” : id_user]

Time expire access_token is defined in init.py, function `create_access_token()` get automatic

Time expire refresh_token is defined in init.py, function `create_refresh_token()` get automatic

### 3.3. Access api protected

The decorator `@jwt_required()` to require access_token in headers, if not in headers or wrong something, deny access

### 3.4. Refresh token

The decorator `@jwt_required()` with parameter name is refreshand value is True to require refresh_token in headers, if not in headers, send access_token or wrong something, deny refresh_token

### 3.5. Logout - revoke token

When send both access_token and refresh_token in headers, loggout successfully, save “jti” per token in DB. Decorator `token_in_blocklist_loader` query in DB to assess token valid or invalid(revoked) when send token in headers, if revoked, deny access.
