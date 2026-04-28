from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserModel(BaseModel):
    id_user: Optional[int]=None
    username: str
    password: str
    created_at: Optional[datetime]=None


class TodoModel(BaseModel):
    id_todo: Optional[int]=None
    title: str
    description: str = ""
    done: bool = False
    created_at: Optional[datetime]=None
    id_cat: Optional[int]=None


class CategoryModal(BaseModel):
    id_cat: Optional[int]=None
    name: str
    color: str
    created_at: Optional[datetime]=None
    id_user: Optional[int]=None

