from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserModel(BaseModel):
    id_user: int
    username: str
    password: str
    created_at: Optional[datetime]


class TodoModel(BaseModel):
    id_todo: int
    title: str
    description: str
    done: bool
    created_at: Optional[datetime]
    id_cat: Optional[int]


class CategoryModal(BaseModel):
    id_cat: int
    name: str
    color: str
    created_at: Optional[datetime]
    id_user: Optional[datetime]

