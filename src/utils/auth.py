import jwt
import os
import dotenv

dotenv.load_dotenv(".env")
SECRET_KEY = os.getenv('JWT_SECRET_KEY')
ALGORITHM = "HS256"

_token = None

def set_token(token):
    global _token
    _token = token

def get_token():
    return _token

def jwt_decoder():
    if _token is None:
        raise Exception("No token found. Please login first.")
    payload = jwt.decode(_token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload["id_user"]