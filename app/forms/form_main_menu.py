import pygame as pg
from .form import Form
from widgets import (
    Button, Text
)
from modulos.variables import (
    SIZE_SCREEN, colors, tittle_game, main_menu_route
)


class FormMainMenu(Form):

    def __init__(self, name, screen, x, y, active, level_num, music_path):
        super().__init__(name, screen, x, y, active, level_num, music_path)

        self.star_first_level = False

        self.surface = pg.image.load(main_menu_route).convert_alpha()
        self.surface = pg.transform.scale(self.surface, SIZE_SCREEN)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

        self.main_menu_tittle = Text(x = SIZE_SCREEN[0] // 2, y = SIZE_SCREEN[1] // 2 - 250, text = tittle_game, screen = screen, font_size = 40, color = 'white')
        self.main_menu_subtittle = Text(x = SIZE_SCREEN[0] // 2, y = SIZE_SCREEN[1] // 2 - 200, text = '', screen = screen, font_size = 50, color = 'white')

        self.button_start = Button(x = SIZE_SCREEN[0] // 2, y = SIZE_SCREEN[1] // 2 - 160, text = 'PLAY', screen = screen, color = 'red', on_click = self.click_start)
        self.button_ranking = Button(x = SIZE_SCREEN[0] // 2 + 40, y = SIZE_SCREEN[1] // 2 - 30, text = 'RANKING', screen = screen, color = 'red', on_click = self.click_ranking, on_click_param = 'form_ranking')
        self.button_settings = Button(x = SIZE_SCREEN[0] // 2 + 45, y = SIZE_SCREEN[1] // 2 + 75, text = 'SETTINGS', screen = screen, color = 'red', on_click = self.click_settings, on_click_param = 'form_settings')
        self.button_exit = Button(x = SIZE_SCREEN[0] // 2, y = SIZE_SCREEN[1] // 2 + 185, text = 'EXIT', screen = screen, color = 'red', on_click = self.click_exit)

        self.widget_list = [
            self.main_menu_tittle, self.main_menu_subtittle, self.button_exit, self.button_ranking, self.button_settings, self.button_start
        ]

    def click_start(self, parametro):
        self.star_first_level = True

    def click_ranking(self, parametro):
        self.set_active(parametro)

    def click_settings(self, parametro):
        self.set_active(parametro)

    def click_exit(self, parametro):
        self.set_active(parametro)

    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()
        
    def update(self):
        self.draw()
        for widget in self.widget_list:
            widget.update()

