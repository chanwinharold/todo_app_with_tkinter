from tkinter import Frame, Checkbutton, Button, IntVar
from config import colors
from src.schemes.views import TodoView


class TodoFrame(Frame):
    def __init__(self, root_, todo: TodoView, on_toggle, on_delete):
        super().__init__(
            root_,
            bg=colors.neutral_100,
            borderwidth=1,
            relief="solid",
            pady=16, padx=16
        )
        self.pack(fill="x", expand=True, pady=4)

        self.todo_view = todo
        self.on_toggle_callback = on_toggle
        self.on_delete_callback = on_delete

        self.check_var = IntVar(value=1 if todo.done else 0)
        self.check = Checkbutton(
            self,
            text=todo.title,
            font=("Red Hat Mono", 14),
            bg=colors.neutral_100,
            variable=self.check_var,
            command=lambda: self.on_toggle_callback(bool(self.check_var.get()))
        )

        try:
            image_trash = ImageTk.PhotoImage(Image.open("src/assets/icons/icon_trash_light.png").resize((16, 16)))
            image_edit = ImageTk.PhotoImage(Image.open("src/assets/icons/icon_edit_light.png").resize((16, 16)))
            image_eye = ImageTk.PhotoImage(Image.open("src/assets/icons/icon_eye_light.png").resize((16, 16)))
        except Exception:
            image_trash = None
            image_edit = None
            image_eye = None

        if image_trash:
            self.del_btn = Button(self, image=image_trash, width=32, height=32, command=self.on_delete_callback)
            self.del_btn.image = image_trash
        else:
            self.del_btn = Button(self, text="🗑", width=4, command=self.on_delete_callback)

        self.check.grid(row=0, column=0)
        self.del_btn.grid(row=0, column=5, padx=(16, 0))

