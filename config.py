
CATEGORY_COLORS = [
    "red",
    "green",
    "yellow",
    "blue",
    "orange",
    "pink",
    "purple"
]

class ColorConfig:
    def __init__(self):
        self.neutral_100 = None
        self.neutral_900 = None

        self.yellow = "yellow"
        self.red = "red"

        self.set_light()

    def set_dark(self):
        self.neutral_100 = "#000000"
        self.neutral_900 = "#FFFFFF"

    def set_light(self):
        self.neutral_100 = "#FFFFFF"
        self.neutral_900 = "#000000"


colors = ColorConfig()