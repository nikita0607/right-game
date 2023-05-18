import pygame as pg
import os


class SceneManager:
    def __init__(self):
        self.scenes = {}

        for name in os.listdir():
            if name.startswith('scene_'):
                self.scenes[name.replace('scene_', '')] = __import__(name)
        print(self.scenes)

    def get_scene(self, window: 'Window', name):
        return self.scenes[name].Manager


class Window:
    def __init__(self, width, height):
        self.win: pg.Surface = pg.display.set_mode((width, height))

        self.widgets = []
        self.run = True

        self.scene = None

    def add_widget(self, widget):
        self.widgets.append(widget)

    def add_widgets(self, widgets):
        for w in widgets:
            self.add_widget(w)

    def clear_widgets(self):
        self.widgets = []

    def load_scene(self, scene_name):
        self.scene = SceneManager().get_scene(self, scene_name)
        self.scene(self)

    def mainloop(self, start_scene='main_menu'):
        clock = pg.time.Clock()
        self.scene = SceneManager().get_scene(self, start_scene)
        self.scene(self)

        click_time = 0

        mouse_x = mouse_y = -1

        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False

            self.win.fill((255, 255, 255))

            if pg.mouse.get_pressed(3)[0]:
                click_time += 1
                mouse_x, mouse_y = pg.mouse.get_pos()
            else:
                click_time = 0

            for w in self.widgets:
                w.update()
                w.draw()

                if click_time == 1 and w.is_clicked(mouse_x, mouse_y):
                    w.click()

            pg.display.update()
            clock.tick(60)

        pg.quit()
