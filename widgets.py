import pygame
import utils
import window

from typing import Union



class Widget:
    def __init__(self, window: window.Window, id: str, x: int, y: int, width: int=None, height: int=None, color=(0, 0, 0), img=None):
        self.x = x
        self.y = y
        self.id = id

        if img:
            if isinstance(img, str):
                self.img = utils.open_model(img)
            else:
                self.img = img
        else:
            self.img = pygame.Surface((width, height))

        self.width = width or self.img.get_width()
        self.height = height or self.img.get_height()

        self.color = color

        self.window = window

    def draw(self):
        self.window.win.blit(self.img, (self.x, self.y))

    def update(self):
        pass

    def is_clicked(self, xmouse, ymouse):
        return (self.x <= xmouse <= self.x+self.width) and (self.y <= ymouse <= self.y + self.height)

    def click(self):
        pass


class Button(Widget):
    def __init__(self, window, id, x: int, y: int, width=None, height=None, color=(0, 0, 0), img: Union[pygame.Surface, str]=None, callback=None):
        super().__init__(window, id, x, y, width, height, color, img)
        self.callback = callback or (lambda: None)

    def click(self):
        self.callback()
