from tkinter import Button
from config import colors


class ThemeBtn(Button):
    def __init__(self, root_):
        super().__init__(
            root_,
            text="Dark mode",
            bg=colors.neutral_100,
            fg=colors.neutral_900,
            width=15,
            borderwidth=2,
            relief="solid"
        )

        self.pack(anchor="ne", pady=(16, 0), padx=(0, 16))
