from tkinter import Frame, Label, StringVar, Button

from config import colors
from src.views.components.field import FieldForm


class AccountView(Frame):
    def __init__(self, root_, on_submit_form=None):
        super().__init__(
            root_,
            bg=colors.neutral_100,
            borderwidth=2,
            relief="solid",
            width=400,
            height=600,
            padx=32
        )
        self.pack_propagate(False)
        self.pack(expand=True, anchor="center")

        self.title = Label(
            self,
            text="Gestion du compte",
            bg=colors.neutral_100,
            fg=colors.neutral_900,
            font=("Red Hat Mono", 20, "bold")
        )
        self.title.pack(pady=(16, 32))

        self.username_value = StringVar()
        self.username = FieldForm(self, "Nom d'utilisateur", text_variable=self.username_value)
        self.username.pack()

        self.old_password_value = StringVar()
        self.old_password = FieldForm(self, "Ancien mot de passe", text_variable=self.old_password_value)
        self.old_password.pack()

        self.new_password_value = StringVar()
        self.new_password = FieldForm(self, "Nouveau mot de passe", text_variable=self.new_password_value)
        self.new_password.pack()

        self.confirm_pwd_value = StringVar()
        self.confirm_pwd = FieldForm(self, "Confirmer le mot de passe", text_variable=self.confirm_pwd_value)
        self.confirm_pwd.pack()

        self.btn_register = Button(
            self,
            text="Enregistrer",
            width=25,
            fg=colors.neutral_900,
            bg=colors.yellow,
            borderwidth=2,
            relief="solid",
            font=("Red Hat Mono", 10, "bold"),
            command=self.fetch_credentials
        )
        self.btn_register.pack(fill='x', expand=True)

        self.btn_register = Button(
            self,
            text="Supprimer le compte",
            width=25,
            fg=colors.neutral_900,
            bg=colors.red,
            borderwidth=2,
            relief="solid",
            font=("Red Hat Mono", 10, "bold"),
            command=self.fetch_credentials
        )
        self.btn_register.pack(side="left", pady=(0, 24))

        self.btn_register = Button(
            self,
            text="Annuler",
            width=25,
            fg=colors.neutral_900,
            bg=colors.neutral_100,
            borderwidth=2,
            relief="solid",
            font=("Red Hat Mono", 10, "bold"),
            command=self.fetch_credentials
        )
        self.btn_register.pack(side="right", pady=(0, 24))

    def fetch_credentials(self):
        return {
            "username": self.username_value.get(),
            "old_password": self.old_password_value.get(),
            "new_password": self.new_password_value.get(),
            "confirmation": self.confirm_pwd_value.get()
        }