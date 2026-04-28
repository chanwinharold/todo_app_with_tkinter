from tkinter import messagebox
from src.schemes.views import TodoView
from src.schemes.models import TodoModel
from src.models.todo import create_todo, get_all_todos, get_one_todo, update_todo, delete_todo, toggle_todo
from src.utils.event_bus import event_bus


class TodoController:
    def __init__(self):
        self.todos = None

    @staticmethod
    def on_create(todo: TodoView, id_cat: int, goto):
        if not todo:
            messagebox.showerror("Erreur", "Erreur interne du serveur. Veuillez réessayer.")
            raise Exception
        if len(todo.title) == 0:
            messagebox.showerror("Erreur", "Le titre ne peut pas être vide !")
            raise Exception

        todo_model = TodoModel(title=todo.title, description=todo.description)
        try:
            created_todo = create_todo(todo_model, id_cat)
            messagebox.showinfo("Succès", "Tâche créée !")
            event_bus.emet("todo_created", created_todo)
            goto()
        except Exception as err:
            messagebox.showerror("Erreur", f"{err}")

    @staticmethod
    def on_update(todo: TodoView, todo_id: int):
        if not todo:
            messagebox.showerror("Erreur", "Erreur interne du serveur. Veuillez réessayer.")
            raise Exception
        if len(todo.title) == 0:
            messagebox.showerror("Erreur", "Le titre ne peut pas être vide !")
            raise Exception

        todo_model = TodoModel(id_todo=todo_id, title=todo.title, description=todo.description)
        try:
            res = update_todo(todo_model)
            messagebox.showinfo("Succès", res)
        except Exception as err:
            messagebox.showerror("Erreur", f"{err}")

    @staticmethod
    def on_delete(todo_id: int):
        try:
            res = delete_todo(todo_id)
            messagebox.showinfo("Succès", res)
        except Exception as err:
            messagebox.showerror("Erreur", f"{err}")

    @staticmethod
    def on_toggle(todo_id: int, state: bool):
        try:
            toggle_todo(todo_id, state)
        except Exception as err:
            messagebox.showerror("Erreur", f"{err}")

    def on_get_all(self, id_cat: int):
        try:
            res = get_all_todos(id_cat)
            self.todos = res
            return res
        except Exception as err:
            messagebox.showerror("Erreur", f"{err}")
            return None


todo_controller = TodoController()