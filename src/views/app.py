from src.views.components.theme import ThemeBtn
from tkinter import Frame
from config import colors
from src.views.form import RegisterFormView, LoginFormView
from src.views.core import CoreView
from src.views.modal import CategoryModalView
from src.controllers.form import auth_controller as auth
from src.controllers.category import cat_controller as cat


class AppView(Frame):
    def __init__(self, root_):
        super().__init__(root_, bg=colors.neutral_100)
        self.pack(fill="both", expand=True)

        self.theme_btn = ThemeBtn(self)
        self.current_view = RegisterFormView(self, on_register=auth.on_register, goto=self.goto_login)

    def goto_login(self):
        self.current_view.destroy()
        self.current_view = LoginFormView(self, on_login=auth.on_login, goto=self.goto_core)

    def goto_category(self):
        self.current_view.destroy()
        self.current_view = CategoryModalView(self, on_create=cat.on_create, goto=self.goto_core)

    def goto_core(self):
        self.current_view.destroy()
        self.current_view = CoreView(self, on_click_add_cat=self.goto_category)

