import jwt
from src.models.auth import SECRET_KEY, ALGORITHM
from src.controllers.form import auth_controller as auth


def jwt_decoder():
    payload = jwt.decode(auth.token, SECRET_KEY, algorithms=ALGORITHM)
    return payload["id_user"]