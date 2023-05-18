from typing import Union

import pygame


class Widget:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

    def update(self):
        pass

    def is_clicked(self, xmouse, ymouse):
        return (self.x <= xmouse <= self.x+self.width) and (self.y >= ymouse >= self.y - self.height)

    def click(self):
        pass


class Button(Widget):
    def __init__(self, x: int, y: int, img: Union[pygame.Surface, str], width=None, height=None, callback=None):
        super().__init__(x, y)
        self.callback = callback

        if isinstance(img, str):
            self.img = pygame.image.load(img)
        else:
            self.img = img

        self.width = width or img.get_width()
        self.height = height or img.get_height()

    def click(self):
        self.callback()
