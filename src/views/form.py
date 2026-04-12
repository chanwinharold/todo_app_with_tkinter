from tkinter import Frame, Label, Button, StringVar
from config import colors
from .components.field import FieldForm
from src.schemes.views import UserLoginView, UserRegisterView, UserManagerView


class RegisterFormView(Frame):
    def __init__(self, root_):
        super().__init__(
            root_,
            bg=colors.neutral_100,
            borderwidth=2,
            relief="solid",
            width=400,
            height=500,
            padx=32
        )
        self.pack_propagate(False)
        self.pack(expand=True, anchor="center")

        self.title = Label(
            self,
            text="ToDo List App",
            bg=colors.neutral_100,
            fg=colors.neutral_900,
            font=("Red Hat Mono", 20, "bold")
        )
        self.title.pack(pady=(16, 48))

        self.username_value = StringVar()
        self.username = FieldForm(self, "Username", text_variable=self.username_value)
        self.username.pack()

        self.password_value = StringVar()
        self.password = FieldForm(self, "Password", text_variable=self.password_value)
        self.password.pack()

        self.confirm_pwd_value = StringVar()
        self.confirm_pwd = FieldForm(self, "Confirm password", text_variable=self.confirm_pwd_value)
        self.confirm_pwd.pack()

        self.btn_register = Button(
            self,
            text="S'inscrire →",
            width=25,
            fg=colors.neutral_900,
            bg=colors.neutral_100,
            borderwidth=2,
            relief="solid",
            font=("Red Hat Mono", 10, "bold"),
            # command=
        )
        self.btn_register.pack(side="bottom", pady=32)

        self.credentials = UserRegisterView(
            username=self.username_value.get(),
            password=self.password_value.get(),
            confirm_pwd=self.confirm_pwd_value.get()
        )


class LoginFormView(Frame):
    def __init__(self, root_):
        super().__init__(
            root_,
            bg=colors.neutral_100,
            borderwidth=2,
            relief="solid",
            width=400,
            height=400,
            padx=32
        )
        self.pack_propagate(False)
        self.pack(expand=True, anchor="center")

        self.title = Label(
            self,
            text="ToDo List App",
            bg=colors.neutral_100,
            fg=colors.neutral_900,
            font=("Red Hat Mono", 20, "bold")
        )
        self.title.pack(pady=(16, 48))

        self.username_value = StringVar()
        self.username = FieldForm(self, "Username", text_variable=self.username_value)
        self.username.pack()

        self.password_value = StringVar()
        self.password = FieldForm(self, "Password", text_variable=self.password_value)
        self.password.pack()

        self.btn_register = Button(
            self,
            text="Se connecter →",
            width=25,
            fg=colors.neutral_900,
            bg=colors.neutral_100,
            borderwidth=2,
            relief="solid",
            font=("Red Hat Mono", 10, "bold"),
            # command=self.fetch_credentials
        )
        self.btn_register.pack(side="bottom", pady=32)

        self.credentials = UserLoginView(
            username=self.username_value.get(),
            password=self.password_value.get()
        )

