import pygame

BASE_WIDTH = 1000
BASE_HEIGHT = 500

widthk = 0
heightk = 0


def init():
    global widthk
    global heightk

    widthk = pygame.display.get_surface().get_width()/BASE_WIDTH
    heightk = pygame.display.get_surface().get_height()/BASE_HEIGHT


def open_model(file_name: str) -> pygame.Surface:
    return pygame.image.load(f'models/{file_name}')


def oemc(a, b):
    return int(widthk * a), int(heightk * b)


def oemw(a):
    return int(widthk * a)


def oemh(b):
    return int(heightk * b)
