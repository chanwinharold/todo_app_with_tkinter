from src.views.app import AppView

class AppController:
    def __init__(self, root_):
        self.root = root_

        self.view = AppView(self.root)