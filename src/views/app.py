from tkinter import Frame
from config import colors
from src.views.form import RegisterFormView, LoginFormView
from src.views.modal import CategoryModalView, TodoModalView, TodoGlimpseModalView
from src.views.account import AccountView

from src.models.todo import Todo

class AppView(Frame):
    def __init__(self, root_):
        super().__init__(root_, bg=colors.neutral_100)
        self.pack(fill="both", expand=True)

        # todo_dict_ = Todo(**{
        #     "title": "My todo name is awesome",
        #     "description": "Voici une approche propre, professionnelle et extensible pour construire une Todo List en Tkinter, sans tomber dans le piège du “script fourre-tout”. Je vais te guider comme pour un vrai projet logiciel : architecture, séparation des responsabilités, classes réutilisables, dépendances propres, puis évolution itérativ"
        # })

        self.current_view = AccountView(self)
