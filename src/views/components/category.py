from tkinter import Frame, Button, Label
from src.views.components.todo import TodoFrame
from src.schemes.views import TodoView, CategoryView
from config import colors


class CategoryFrame(Frame):
    def __init__(self, root_, category: CategoryView):
        super().__init__(root_, bg=colors.neutral_100)
        self.pack(fill="x", expand=True)

        self.cat_container = Frame(self, bg=colors.neutral_100)
        self.cat_container.columnconfigure(1, weight=1)
        self.cat_container.pack(fill="x", expand=True)

        self.cat_name = Label(
            self.cat_container,
            text=category.name,
            bg=colors.neutral_100,
            fg=colors.neutral_900,
            font=("Red Hat Mono", 16, "bold")
        )
        self.todo_add_btn = Button(
            self.cat_container,
            text="Ajouter une tâche",
            bg=colors.neutral_100,
            fg=colors.neutral_900,
            width=15,
            borderwidth=1,
            relief="solid"
        )
        self.cat_del_btn = Button(
            self.cat_container,
            text="Supprimer",
            bg=colors.neutral_100,
            fg=colors.neutral_900,
            width=15,
            borderwidth=1,
            relief="solid"
        )

        self.cat_name.grid(row=0, column=0)
        self.todo_add_btn.grid(row=0, column=6)
        self.cat_del_btn.grid(row=0, column=7)

        self.todo_container = Frame(self, bg=colors.neutral_100)
        self.todo_container.pack(fill="x", expand=True)

        self.todos = []