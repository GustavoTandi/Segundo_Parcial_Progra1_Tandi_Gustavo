import pygame as pg
from .widget import Widget
from modulos.variables import (
    font_daydream, colors
)

class Text(Widget):
    def __init__(self, x, y, text, screen, font_size, color):
        super().__init__(x, y, text, screen, font_size, color)
        self.font = pg.font.Font(font_daydream, self.font_size)
        self.image = self.font.render(text, True, colors[color])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        super().draw()

    def update(self):
        self.draw()