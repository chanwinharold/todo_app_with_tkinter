from tkinter import Frame, Button, Label
from src.views.components.todo import TodoFrame
from src.schemes.views import TodoView, CategoryView
from src.models.todo import get_all_todos
from config import colors


class CategoryFrame(Frame):
    def __init__(self, root_, category: CategoryView, on_add_todo, on_delete_cat, on_refresh):
        super().__init__(root_, bg=colors.neutral_100)
        self.pack(fill="x", expand=True)

        self.category_view = category
        self.on_add_todo_callback = on_add_todo
        self.on_delete_cat_callback = on_delete_cat
        self.on_refresh_callback = on_refresh

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
            relief="solid",
            command=self.on_add_todo_callback
        )
        self.cat_del_btn = Button(
            self.cat_container,
            text="Supprimer",
            bg=colors.neutral_100,
            fg=colors.neutral_900,
            width=15,
            borderwidth=1,
            relief="solid",
            command=self.on_delete_cat_callback
        )

        self.cat_name.grid(row=0, column=0)
        self.todo_add_btn.grid(row=0, column=6)
        self.cat_del_btn.grid(row=0, column=7)

        self.todo_container = Frame(self, bg=colors.neutral_100)
        self.todo_container.pack(fill="x", expand=True)

        self.todos = []
        self.load_todos()

    def load_todos(self):
        try:
            todos = get_all_todos(self.category_view.id_cat)
            if todos:
                for todo in todos:
                    todo_view = TodoView(
                        id_todo=todo[0],
                        title=todo[1],
                        description=todo[2],
                        done=todo[3]
                    )
                    self.add_todo(todo_view)
        except Exception as e:
            print(f"Error loading todos: {e}")

    def add_todo(self, todo_view):
        from src.controllers.todo import todo_controller
        todo_frame = TodoFrame(
            self.todo_container,
            todo_view,
            on_toggle=lambda state: todo_controller.on_toggle(todo_view.id_todo, state),
            on_delete=lambda: (todo_controller.on_delete(todo_view.id_todo), self.on_refresh_callback())
        )
        self.todos.append(todo_frame)
        todo_frame.pack(fill="x", expand=True, pady=4)

    def refresh(self):
        for todo in self.todos:
            todo.destroy()
        self.todos = []
        self.load_todos()