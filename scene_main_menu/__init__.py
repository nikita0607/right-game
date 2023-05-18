from widgets import Widget, Button
from window import Window

from utils import oemc


class Manager:
    def __init__(self, window: Window):
        self.window = window

        start_button = Button(window, 'start_button', *oemc(400, 200), img='start_button.png', callback=self.start_game)

        window.add_widget(start_button)

    def start_game(self):
        self.window.load_scene('game')