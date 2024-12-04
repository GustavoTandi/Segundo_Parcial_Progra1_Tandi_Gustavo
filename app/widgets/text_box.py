import pygame as pg
from .widget import Widget
from .variables import (
    colors, font_daydream, item_sound
)

class TextBox(Widget):

    def __init__(self, x, y, text, screen, font_size, color, on_click = None, on_click_param = None):
        super().__init__(x, y, text, screen, font_size)
        self.font = pf.font.Font(font_daydream, font_size)
        self.image = self.font.render(self.text, True, colors[color])

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.click.option.sfx = pg.mixer.Sound(item_sound)

        self.on_click = self.on_click
        self.on_click_param = on_click_param

        self.write_on = True
        self.writing = ''
        self.image_writing = self.font.render(self.writing, True, colors[color])
        self.rect_writing = self.image_writing.get_rect()
        self.rect_writing.center = (x, y)

    def write_on_box(self, event_list: list):
        
        for event in event_list:
            if event.type == pg.KEYDOWN and self.write_on:
                if event.key == pg.K_BACKSPACE:
                    self.writing = self.writing[:-1]
                else:
                    self.writing += event.unicode

    def draw(self):
        super().draw()
        self.image.blit(self.screen, (self.rect_writing.x, self.rect_writing.y))

    def update(self):
        self.draw()
        self.write_on_box()