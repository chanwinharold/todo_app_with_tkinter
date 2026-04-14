from tkinter import Frame, Label, Button, Canvas, Scrollbar
from config import colors
from src.views.components.category import CategoryFrame
from src.schemes.views import CategoryView

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

    def destroy(self):
        """Détruit aussi la scrollbar qui vit dans root_, pas dans self."""
        if self.scrollbar and self.scrollbar.winfo_exists():
            self.scrollbar.destroy()
        super().destroy()