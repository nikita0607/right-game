import pygame
import utils
import window

from typing import Union


class Widget:
    def __init__(self, window: window.Window, id: str, x: int, y: int, width: int = 0, height: int = 0, color=(0, 0, 0), img=None, callback=None):
        self.x = x
        self.y = y
        self.id = id

        if img:
            if isinstance(img, str):
                self.img = utils.open_model(img, width=width)
            else:
                self.img = img
        else:
            self.img = pygame.Surface((width, height))

        self.width = width or self.img.get_width()
        self.height = height or self.img.get_height()

        self.color = color

        self.window = window

        self.callback = callback

    def draw(self):
        self.window.win.blit(self.img, (self.x, self.y))

    def update(self):
        pass

    def move_center(self, x, y):
        self.x = int(x-(self.width/2))
        self.y = int(y-(self.height/2))

    def move_center2cords(self):
        self.move_center(self.x, self.y)

    def get_center(self):
        return self.x+(self.width//2), self.y+(self.height//2)

    def is_clicked(self, xmouse, ymouse):
        return (self.x <= xmouse <= self.x+self.width) and (self.y <= ymouse <= self.y + self.height)

    def click(self):
        if self.callback:
            self.callback(self)


class TextWidget(Widget):
    def __init__(self, window, id, x: int, y: int, height, text: str, color=(0, 0, 0), callback=None):
        super().__init__(window, id, x, y, height//2, height, color, img=None, callback=callback)
        self.text = text

        font = pygame.font.SysFont(None, self.height)
        self.img = font.render(self.text, True, self.color)

        self.width = self.img.get_width()
        self.height = self.img.get_height()
