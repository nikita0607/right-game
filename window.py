import pygame as pg


class Window:
    def __init__(self, width, height):
        self.window = pg.display.set_mode((width, height))

