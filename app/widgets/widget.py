import pygame as pg

class Widget:

    def __init__(self, x: int , y: int, text:str, screen: pg.Surface, font_size:int, color: str):
        self.x = x
        self.y = y
        self.text = text
        self.screen = screen
        self.font_size = font_size

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))