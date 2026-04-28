from tkinter import messagebox
from src.schemes.views import CategoryView
from src.schemes.models import CategoryModal
from src.models.category import create_category, get_categories
from src.utils.auth import jwt_decoder
from src.utils.event_bus import event_bus


class CategoryController:
    def __init__(self):
        self.categories = None

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
            id_user = jwt_decoder()
            created_cat = create_category(category_model, id_user)
            messagebox.showinfo("Succès", "Catégorie créée !")
            event_bus.emet("category_created", created_cat)
            goto()
        except Exception as err:
            messagebox.showerror("Erreur", f"{err}")

    def on_get(self):
        try:
            id_user = jwt_decoder()
            res = get_categories(id_user)
            self.categories = res
        except Exception as err:
            messagebox.showerror("Erreur", f'{err}')


cat_controller = CategoryController()