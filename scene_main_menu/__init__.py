from widgets import Widget, Button
from window import Window

from utils import oemc


class Manager:
    def __init__(self, window: Window):
        self.window = window

        start_button = Button(window, 'start_button', *oemc(50, 50), img='start_button.png', callback=self.start_game)
        start_button.move_center2cords()

        window.add_widget(start_button)

    def start_game(self):
        self.window.load_scene('game')

    def 