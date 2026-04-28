from pydantic import BaseModel


class UserRegisterView(BaseModel):
    username: str
    password: str
    confirm_pwd: str


class UserLoginView(BaseModel):
    username: str
    password: str


class UserAccountView(BaseModel):
    username: str
    old_password: str
    new_password: str
    confirm_pwd: str


class CategoryView(BaseModel):
    id_cat: int = 0
    name: str
    color: str


class TodoView(BaseModel):
    id_todo: int = 0
    title: str
    description: str = ""
    done: bool = False

