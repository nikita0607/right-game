from widgets import Widget, Button
from window import Window

from utils import oemc


class Manager:
    def __init__(self, window):
        window.clear_widgets()

        left_arrow = Widget(window, 'left_arrow', *oemc(200, 300), img='left_arrow_game.png')
        window.add_widget(left_arrow)

    def update(self):
        pass