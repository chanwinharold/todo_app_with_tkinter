from database import conn, cursor
from passlib.hash import bcrypt
from src.schemes.models import UserModel
import jwt
import os
import dotenv

dotenv.load_dotenv("../../.env")
SECRET_KEY = os.getenv('JWT_SECRET_KEY')


def create_user(user: UserModel):
    user.password = bcrypt.hash(user.password)

    cursor.execute("""
        INSERT INTO USERS (username, password)
            VALUES (?, ?)
    """, [user.username, user.password])
    conn.commit()

    return "User registered !"


def login_user(user: UserModel):
    cursor.execute("""
        SELECT *
        FROM USERS
        WHERE username = ?
    """, user.username)

    res: UserModel = cursor.fetchone()
    if not res:
        raise Exception

    valid: bool = bcrypt.verify(user.password, res.password)
    if not valid:
        raise Exception

    return jwt.encode(
        {"id_user": res.id_user, "created_at": res.created_at},
        SECRET_KEY,
        algorithms=["HS256"]
    )


def update_user(user: UserModel):
    cursor.execute("""
        UPDATE USERS
        SET 
            username = ?, 
            password = ?
        WHERE id_user = ?
    """, [user.username, user.password, user.id_user])
    conn.commit()

    return "User updated !"


def delete_user(id_user: int):
    cursor.execute("""
        DELETE FROM USERS
            WHERE id_user = ?
    """, [id_user])
    conn.commit()

    return "User deleted !"

