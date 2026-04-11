from tkinter import Tk
from src.controllers.app import AppController

root = Tk()
root.title("ToDo List App")
root.geometry("1024x500")

app = AppController(root)

root.mainloop()