from database import conn, cursor
from passlib.hash import bcrypt
from src.schemes.models import UserModel
import jwt
import os
import dotenv

dotenv.load_dotenv(".env")
SECRET_KEY = os.getenv('JWT_SECRET_KEY')


def create_user(user: UserModel):
    try:
        user.password = bcrypt.hash(user.password)

        cursor.execute("""
                       INSERT INTO USERS (username, password)
                       VALUES (?, ?)
                       """, [user.username, user.password])
        conn.commit()

        return "User registered !"
    except Exception as errors:
        raise errors


def login_user(user: UserModel):
    try:
        cursor.execute("""
                       SELECT *
                       FROM USERS
                       WHERE username = ?
                       """, [user.username])
        res = cursor.fetchone()
        res = UserModel(
            id_user=res[0],
            username=res[1],
            password=res[2],
            created_at=res[3]
        )
        if not res:
            raise Exception

        valid: bool = bcrypt.verify(user.password, res.password)
        if not valid:
            raise Exception

        return jwt.encode(
            {"id_user": res.id_user},
            SECRET_KEY,
            algorithm="HS256"
        )
    except Exception as errors:
        raise errors


def update_user(user: UserModel):
    try:
        cursor.execute("""
                       UPDATE USERS
                       SET username = ?,
                           password = ?
                       WHERE id_user = ?
                       """, [user.username, user.password, user.id_user])
        conn.commit()

        return "User updated !"
    except Exception as errors:
        raise errors


def delete_user(id_user: int):
    try:
        cursor.execute("""
                       DELETE
                       FROM USERS
                       WHERE id_user = ?
                       """, [id_user])
        conn.commit()

        return "User deleted !"
    except Exception as errors:
        raise errors

