import jwt

SECRET_KEY = "mysecretkey"
expires_in=3600

def create_token(user_id):
    """Create a JWT token for the given user."""
    payload = {
        'sub': user_id,
        expires_in: expires_in
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def verify_token(token):
    """Verify the JWT token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return NotImplemented