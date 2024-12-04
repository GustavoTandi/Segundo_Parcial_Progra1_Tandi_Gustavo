from .widget import Widget
import pygame as pg
from modulos.variables import (
    font_daydream, colors, item_sound
)

class Button(Widget):

    def __init__(self, x, y, text, screen, font_size = 25, color = str, on_click = None, on_click_param = None):
        super().__init__(x, y, text, screen, font_size, color)
        self.font = pg.font.Font(font_daydream, self.font_size)
        self.image = self.font.render(text, True , colors['red'])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.click_option_sfx = pg.mixer.Sound(item_sound)
        self.on_click = on_click
        self.on_click_param = on_click_param


    def button_pressed(self):
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1:
                pg.time.delay(300)
                self.on_click(self.on_click_param)
                self.click_option_sfx.set_volume(0.1)
                self.click_option_sfx.play()
    def draw(self):
        super().draw()

    def update(self):
        self.draw()
        self.button_pressed()
