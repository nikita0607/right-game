from widgets import Widget, Button
from window import Window

from utils import oemc, oemw


class Manager:
    def __init__(self, window):
        window.clear_widgets()

        left_arrow = Widget(window, 'left_arrow', *oemc(10, 70), img='left_arrow_game.png')
        right_arrow = Widget(window, 'right_arrow', *oemc(90, 70), img='right_arrow_game.png', width=oemw(5))

        left_arrow.move_center2cords()
        right_arrow.move_center2cords()

        window.add_widget(left_arrow)
        window.add_widget(right_arrow)