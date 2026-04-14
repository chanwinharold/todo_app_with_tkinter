from tkinter import messagebox
from src.schemes.views import CategoryView
from src.schemes.models import CategoryModal
from src.models.category import create_category
from src.utils.auth import jwt_decoder


class CategoryController:
    def __init__(self):
        self.category = None

    @staticmethod
    def on_create(category: CategoryView, goto):
        if not category:
            messagebox.showerror("Erreur", "Erreur interne du serveur. Veuillez réessayer.")
            raise Exception
        if len(category.name)==0 or len(category.color)==0:
            messagebox.showerror("Erreur", "Champs vides ou invalides !")
            raise Exception

        category_model = CategoryModal(name=category.name, color=category.color)
        try:
            token = jwt_decoder()
            res = create_category(category_model, token)
            messagebox.showinfo("Succès", res)
            goto()
        except Exception as err:
            messagebox.showerror("Erreur", f"{err}")


cat_controller = CategoryController()