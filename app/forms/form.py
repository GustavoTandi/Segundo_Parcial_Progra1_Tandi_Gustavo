import pygame as pg

class Form:

    form_dict = {}

    def __init__(self, name: str, screen, x: int, y: int, active: bool, level_num: int, music_path: str):
        self.form_dict[name] = self
        self.screen = screen
        self.x = x
        self.y = y
        self.level_num = level_num
        self.music_path = music_path

    def set_active(self, name: str):
        for aux_form in self.form_dict.values():
            aux_form.active = False
        self.form_dict[name].active = True

    def music_update(self):
        pg.mixer.music.stop()
        pg.mixer.music.load(f'{self.music_path}')
        pg.mixer.music.set_volume(0.1)
        pg.mixer.music.play(-1, 0, 7000)

    def draw(self):
        self.screen.blit(self.surface, self.slave_rect)