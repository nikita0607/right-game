import pygame


def init():
    global width
    global height

    width = pygame.display.get_surface().get_width()
    height = pygame.display.get_surface().get_height()


def open_model(file_name: str, width=None, height=None) -> pygame.Surface:
    surface = pygame.image.load(f'models/{file_name}')
    s = (width or surface.get_width(), height or surface.get_height())
    surface = pygame.transform.scale(surface, s)
    return surface


def oemc(a, b):
    return int(width * a / 100), int(height * b / 100)


def oemw(a):
    return int(width * a / 100)


def oemh(b):
    return int(height * b / 100)
