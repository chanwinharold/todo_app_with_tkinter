from tkinter import Frame, Label, Button, Canvas, Scrollbar
from config import colors
from src.views.components.category import CategoryFrame
from src.schemes.views import CategoryView
from src.utils.event_bus import event_bus
from src.utils.auth import jwt_decoder
from src.models.category import get_categories


class CoreView(Canvas):
    def __init__(self, root_, on_click_add_cat):
        super().__init__(root_, bg=colors.neutral_100)
        self.pack(side="left", fill="both", expand=True, padx=16)

        # Scrollbar dans root_ — on garde la référence pour la détruire proprement
        self.scrollbar = Scrollbar(root_, orient="vertical", command=self.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.configure(yscrollcommand=self.scrollbar.set)

        self.interior = Frame(self, bg=colors.neutral_100)
        self.interior_id = self.create_window(0, 0, window=self.interior, anchor="nw")
        self.interior.bind("<Configure>", lambda e: self.configure(scrollregion=self.bbox("all")))
        self.bind("<Configure>", lambda e: self.itemconfig(self.interior_id, width=e.width))

        self.title = Label(
            self.interior,
            text="ToDo List App",
            bg=colors.neutral_100,
            fg=colors.neutral_900,
            font=("Red Hat Mono", 20, "bold"),
            width=100,
            anchor="nw"
        )
        self.title.pack()

        self.cat_add_btn = Button(
            self.interior,
            text="Ajouter une catégorie",
            bg=colors.neutral_100,
            fg=colors.neutral_900,
            width=20,
            borderwidth=1,
            relief="solid",
            command=on_click_add_cat
        )
        self.cat_add_btn.pack(anchor="w", pady=16)

        self.wrapper = Frame(self.interior, bg=colors.neutral_100, padx=32, pady=32)
        self.wrapper.pack(fill="both", expand=True)

        self.categories = []

        self.load_categories()

        event_bus.inscrire("category_created", self.add_category)

    def destroy(self):
        """Détruit aussi la scrollbar qui vit dans root_, pas dans self."""
        if self.scrollbar and self.scrollbar.winfo_exists():
            self.scrollbar.destroy()
        super().destroy()

    def add_category(self, new_category):
        category_view = CategoryView(id_cat=new_category[0], name=new_category[1], color=new_category[2])
        cat_frame = CategoryFrame(
            self.wrapper,
            category_view,
            on_add_todo=lambda: self.on_add_todo(category_view),
            on_delete_cat=lambda: self.on_delete_category(category_view),
            on_refresh=self.refresh
        )
        self.categories.append(cat_frame)
        cat_frame.pack(fill="x", expand=True, pady=8)

    def refresh(self):
        for cat in self.categories:
            cat.destroy()
        self.categories = []
        self.load_categories()

    def load_categories(self):
        try:
            id_user = jwt_decoder()
            categories = get_categories(id_user)
            if categories:
                for cat in categories:
                    self.add_category(cat)
        except Exception as e:
            print(f"Error loading categories: {e}")

    def on_add_todo(self, category_view):
        from src.views.modal import TodoModalView
        from src.controllers.todo import todo_controller
        TodoModalView(self.master, category_view, todo_controller.on_create, self.refresh)

    def on_delete_category(self, category_view):
        from src.models.category import delete_category
        from tkinter import messagebox
        try:
            res = delete_category(category_view.id_cat)
            messagebox.showinfo("Succès", res)
            self.refresh()
        except Exception as err:
            messagebox.showerror("Erreur", f"{err}")
