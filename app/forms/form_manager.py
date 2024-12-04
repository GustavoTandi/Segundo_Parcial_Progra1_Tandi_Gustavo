import pygame as pg
from modulos.variables import music_sound

from .form_main_menu import FormMainMenu
from .form_ranking import FormRanking

class FormManager:

    def __init__(self, screen, ranking = None):
        self.main_screen = screen
        self.ranking = ranking

        self.forms = [
            FormMainMenu(name='form_main_menu', screen=screen, x=0, y=0, active=True, level_num=1, music_path=music_sound),
            FormRanking(name='form_ranking', screen=screen, x=0, y=0, active=True, level_num=1, music_path=music_sound, ranking_list=self.ranking)
        ]

    def forms_update(self, event_list: list):
    
        if self.forms[0].set_active:
            self.forms[0].update()
            self.forms[0].draw()
        
        elif self.forms[1].set_active:
            self.forms[1].update()
            self.forms[1].draw()

    def update(self, event_list: list):
        self.forms_update(event_list)
