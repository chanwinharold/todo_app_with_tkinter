from src.schemes.models import UserModel
from src.schemes.views import UserRegisterView, UserLoginView
from src.models.auth import create_user, login_user
from src.utils.auth import set_token
from tkinter import messagebox


class AuthController:
    def __init__(self):
        self.current_user = None
        self.token = None

    @staticmethod
    def on_register(user: UserRegisterView, goto):
        if not user:
            messagebox.showerror("Erreur", "Erreur interne du serveur. Veuillez réessayer.")
            raise Exception
        if len(user.username)==0 or len(user.password)==0:
            messagebox.showerror("Erreur", "Champs vides ou invalides !")
            raise Exception
        if user.password != user.confirm_pwd:
            messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas !")
            raise Exception

        user_model = UserModel(username=user.username, password=user.password)
        try:
            res = create_user(user=user_model)
            messagebox.showinfo("Succès", res)
            goto()
        except Exception as errors:
            messagebox.showerror("Erreur", f"{errors}")


    def on_login(self, user: UserLoginView, goto):
        if not user:
            messagebox.showerror("Erreur", "Erreur interne du serveur. Veuillez réessayer.")
            raise Exception
        if len(user.username)==0 or len(user.password)==0:
            messagebox.showerror("Erreur", "Champs vides ou invalides !")
            raise Exception

        user_model = UserModel(username=user.username, password=user.password)
        try:
            self.token = login_user(user_model)
            set_token(self.token)
            messagebox.showinfo("Succès", "User logged !")
            goto()
        except Exception as errors:
            messagebox.showerror("Error", f"{errors}")


auth_controller = AuthController()
