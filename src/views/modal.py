from tkinter import Frame, Label, StringVar, Button, Text
from tkinter.ttk import Combobox
from config import colors, CATEGORY_COLORS
from src.views.components.field import FieldForm
from src.schemes.views import CategoryView, TodoView

class CategoryModalView(Frame):
    def __init__(self, root_, on_create, goto):
        super().__init__(
            root_,
            bg=colors.neutral_100,
            borderwidth=2,
            relief="solid",
            width=400,
            height=400,
            padx=32
        )
        self.pack_propagate(False)
        self.pack(expand=True, anchor="center")

        self.title = Label(
            self,
            text="ToDo List App",
            bg=colors.neutral_100,
            fg=colors.neutral_900,
            font=("Red Hat Mono", 20, "bold")
        )
        self.title.pack(pady=(16, 48))

        self.category_value = StringVar()
        self.category = FieldForm(
            self,
            "Nom de la catégorie",
            text_variable=self.category_value
        )
        self.category.pack()

        self.label = Label(
            self, text="Couleur de la catégorie",
            fg=colors.neutral_900,
            bg=colors.neutral_100,
            font=("Red Hat Mono", 12),
            width=100,
            pady=8,
            anchor="w"
        )
        self.label.pack()
        self.menu_color_value = StringVar()
        self.menu_color = Combobox(
            self,
            textvariable=self.menu_color_value,
            values=CATEGORY_COLORS,
            width=100
        )
        self.menu_color.insert(0, CATEGORY_COLORS[0])
        self.menu_color.pack(ipady=4, pady=(0, 12))

        self.btn_register = Button(
            self,
            text="Créer la catégorie",
            width=25,
            fg=colors.neutral_900,
            bg=colors.neutral_100,
            borderwidth=2,
            relief="solid",
            font=("Red Hat Mono", 10, "bold"),
            command=lambda : on_create
            (
                CategoryView(
                    name=self.category_value.get(),
                    color=self.menu_color_value.get()
                ),
                goto
            )
        )
        self.btn_register.pack(side="bottom", pady=32)


class TodoModalView(Frame):
    def __init__(self, root_):
        super().__init__(
            root_,
            bg=colors.neutral_100,
            borderwidth=2,
            relief="solid",
            width=400,
            height=500,
            padx=32
        )
        self.pack_propagate(False)
        self.pack(expand=True, anchor="center")

        self.title = Label(
            self,
            text="ToDo List App",
            bg=colors.neutral_100,
            fg=colors.neutral_900,
            font=("Red Hat Mono", 20, "bold")
        )
        self.title.pack(pady=(16, 48))

        self.todo_value = StringVar()
        self.todo = FieldForm(
            self,
            "Nom de la tâche",
            text_variable=self.todo_value
        )
        self.todo.pack()

        self.label = Label(
            self, text="Description de la tâche",
            fg=colors.neutral_900,
            bg=colors.neutral_100,
            font=("Red Hat Mono", 12),
            width=100,
            pady=8,
            anchor="w"
        )
        self.label.pack()
        self.description = Text(self, width=50, height=8)
        self.description.pack()

        self.btn_register = Button(
            self,
            text="Créer la tâche",
            width=25,
            fg=colors.neutral_900,
            bg=colors.neutral_100,
            borderwidth=2,
            relief="solid",
            font=("Red Hat Mono", 10, "bold"),
            # command=self.fetch_credentials
        )
        self.btn_register.pack(side="bottom", pady=32)

        self.credentials = TodoView(
            title=self.todo_value.get(),
            description=self.description.get("1.0", "end-1c")
        )


class TodoGlimpseModalView(Frame):
    def __init__(self, root_, todo: TodoView):
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
            text="ToDo List App",
            bg=colors.neutral_100,
            fg=colors.neutral_900,
            font=("Red Hat Mono", 20, "bold")
        )
        self.title.pack(pady=(16, 48))

        self.label_title = Label(
            self, text="Titre de la tâche",
            fg=colors.neutral_900,
            bg=colors.neutral_100,
            font=("Red Hat Mono", 14, "bold", "underline"),
            width=100,
            pady=8,
            anchor="w"
        )
        self.label_title.pack()
        self.title = Label(
            self, text=todo.title,
            fg=colors.neutral_900,
            bg=colors.neutral_100,
            font=("Red Hat Mono", 12),
            width=100,
            pady=8,
            anchor="w"
        )
        self.title.pack()

        self.label_description = Label(
            self, text="Description de la tâche",
            fg=colors.neutral_900,
            bg=colors.neutral_100,
            font=("Red Hat Mono", 14, "bold", "underline"),
            width=100,
            pady=8,
            anchor="w"
        )
        self.label_description.pack()
        self.description = Label(
            self, text=todo.description,
            fg=colors.neutral_900,
            bg=colors.neutral_100,
            font=("Red Hat Mono", 12),
            pady=8,
            anchor="w",
            wraplength=320,
            justify="left"
        )
        self.description.pack(fill="x")

        self.btn_register = Button(
            self,
            text="Fermer",
            width=25,
            fg=colors.neutral_900,
            bg=colors.neutral_100,
            borderwidth=2,
            relief="solid",
            font=("Red Hat Mono", 10, "bold"),
            # command=self.close
        )
        self.btn_register.pack(side="bottom", pady=32)

