from tkinter import Frame, Label
from tkinter.ttk import Entry
from config import colors


class FieldForm(Frame):
    def __init__(self, root_, label_: str, text_variable):
        super().__init__(root_, bg=colors.neutral_100)

        self.label = Label(
            self, text=label_,
            fg=colors.neutral_900,
            bg=colors.neutral_100,
            font=("Red Hat Mono", 12),
            width=100,
            pady=8,
            anchor="w"
        )
        self.label.pack()

        self.entry = Entry(self, width=100, textvariable=text_variable)
        self.entry.pack(ipady=4, pady=(0, 12))

