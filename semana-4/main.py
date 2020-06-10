import jwt

ALGORITHM = "HS256"

SALT = "acelera"


def create_token(data, secret=SALT):
    return jwt.encode(payload=data, key=secret, algorithm=ALGORITHM)


def verify_signature(token):
    try:
        return jwt.decode(token, key=SALT, algorithms=[ALGORITHM])
    except jwt.exceptions.DecodeError:
        return {"error": 2}
