from src.views.app import AppView

class AppController:
    def __init__(self, root_):
        self.root = root_

        self.view = AppView(self.root)
        self.current_user = None
        self.token = None

    def set_user(self, user, token):
        self.current_user = user
        self.token = token