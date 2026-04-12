from src.views.components.theme import ThemeBtn
from src.views.core import CoreView
from tkinter import Frame
from config import colors

class AppView(Frame):
    def __init__(self, root_):
        super().__init__(root_, bg=colors.neutral_100)
        self.pack(fill="both", expand=True)

        self.theme_btn = ThemeBtn(self)
        self.current_view = CoreView(self)

