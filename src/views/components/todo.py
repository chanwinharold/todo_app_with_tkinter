from tkinter import Frame, Checkbutton, Button
from PIL import Image, ImageTk
from config import colors
from src.schemes.views import TodoView


class TodoFrame(Frame):
    def __init__(self, root_, todo: TodoView):
        super().__init__(
            root_,
            bg=colors.neutral_100,
            borderwidth=1,
            relief="solid",
            pady=16, padx=16
        )
        self.columnconfigure(1, weight=1)
        self.pack(fill="x", expand=True, pady=16)

        self.check = Checkbutton(
            self,
            text=todo.title,
            font=("Red Hat Mono", 14),
            bg=colors.neutral_100
        )

        image_trash = ImageTk.PhotoImage(Image.open("src/assets/icons/icon_trash_light.png").resize((16, 16)))
        image_edit = ImageTk.PhotoImage(Image.open("src/assets/icons/icon_edit_light.png").resize((16, 16)))
        image_eye = ImageTk.PhotoImage(Image.open("src/assets/icons/icon_eye_light.png").resize((16, 16)))

        self.del_btn = Button(self, image=image_trash, width=32, height=32)
        self.edit_btn = Button(self, image=image_edit, width=32, height=32)
        self.view_btn = Button(self, image=image_eye, width=32, height=32)

        self.del_btn.image = image_trash
        self.edit_btn.image = image_edit
        self.view_btn.image = image_eye

        self.check.grid(row=0, column=0)
        self.del_btn.grid(row=0, column=5, padx=(16, 0))
        self.edit_btn.grid(row=0, column=6, padx=(16, 0))
        self.view_btn.grid(row=0, column=7, padx=(16, 0))

