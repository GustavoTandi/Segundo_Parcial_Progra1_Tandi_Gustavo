import pygame as pg
from .form import Form
from widgets import (
    Button, Text
)
from modulos.variables import SIZE_SCREEN, ranking_image_route, colors


class FormRanking(Form):
    def __init__(self, name, screen, x, y, active, level_num, music_path, ranking_list):
        super().__init__(name, screen, x, y, active, level_num, music_path)

        self.surface = pg.image.load(ranking_image_route).convert_alpha()
        self.surface = pg.transform.scale(self.surface, SIZE_SCREEN)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.confirm_name = True

        self.ranking_on_screen = []
        self.ranking_list = []



        self.title = Text(x = SIZE_SCREEN[0] // 2, y = SIZE_SCREEN[1] // 2 - 200, text = 'RANKING', screen = screen, font_size = 75, color='black')
        self.subtitle = Text(x = SIZE_SCREEN[0] // 2, y = SIZE_SCREEN[1] // 2 - 100, text = 'TOP 5', screen = screen, font_size = 50, color= 'white')
        self.button_return_menu = Button(x = SIZE_SCREEN[0] // 2, y = SIZE_SCREEN[1] // 2 + 250, text = 'x', screen = screen, on_click = self.click_return_menu, on_click_param = 'form_main_menu')

        self.init_ranking()

        self.widget_list = [
            self.title, self.subtitle, self.button_return_menu
        ]
    def init_ranking(self):
        for i in range(len(self.ranking_list)):
            self.ranking_on_screen.append(
                Text(x=SIZE_SCREEN[0]//2-150, y=SIZE_SCREEN[1]//2.5+i*30, text=f'{i+1}', screen=self.screen, font_size=20, color='white')
            )
            self.ranking_on_screen.append(
                Text(x=SIZE_SCREEN[0]//2-100, y=SIZE_SCREEN[1]//2.5+i*25, text=f'{self.ranking_list[i][0]}', screen=self.screen, font_size=10, color='white')
            )
            self.ranking_on_screen.append(
                Text(x=SIZE_SCREEN[0]//2-100, y=SIZE_SCREEN[1]//2.5+i*25, text=f'{self.ranking_list[i][1]}', screen=self.screen, font_size=10, color='white')
            )

    def click_return_menu(self, parametro):
        self.set_active(parametro)

    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()
        for ranking in self.ranking_on_screen:
            ranking.draw()
        
    def update(self):
        super().draw()
        for widget in self.widget_list:
            widget.update()
