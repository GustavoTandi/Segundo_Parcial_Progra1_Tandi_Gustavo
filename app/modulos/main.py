import pygame as pg
import sys
import json
from .variables import (
    SIZE_SCREEN, tittle_game, colors, triangles, current_color_voter, item_sound, music_sound
)
from .funciones import (
    load_ranking, draw_screen, color_selection
)
from forms.form_manager import(
    FormManager
)
from .sonidos import Sound

def run_game():
    pg.init()
    sound_game = Sound()
    sound_game.play_music(music_sound)

    screen = pg.display.set_mode(SIZE_SCREEN)
    pg.display.set_caption(tittle_game)

    ranking = load_ranking()

    forms = FormManager(screen, ranking)
    forms_mm = forms.forms[0]

    current_question_index = 0
    score = 0
    score_font = pg.font.SysFont('Arial', 60)
    score_pos = (685, 264)
    rect_option_blue = pg.Rect(160, 93, 195, 40)
    rect_option_yellow = pg.Rect(445, 93, 195, 40)

    game_running = True
    while game_running:
        event_list = pg.event.get()

        for event in event_list:
            if event.type == pg.QUIT:
                game_running = False

        forms.update(event_list)

        if forms_mm.star_first_level:
            counter_yellow = 0
            counter_blue = 0

            for event in event_list:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if rect_option_blue.collidepoint(event.pos) or rect_option_yellow.collidepoint(event.pos):
                        sound_game.play_sound(item_sound)
                        for voter in range(9):
                            current_color_voter[voter] = color_selection('blue', 'yellow')
                            if current_color_voter[voter] == colors['blue']:
                                counter_blue += 1
                            else:
                                counter_yellow += 1

                    if rect_option_blue.collidepoint(event.pos):
                        print('boton azul')
                        if counter_blue > counter_yellow:
                            score += 1
                            current_question_index += 1
                        else:
                            score = 0
                            current_question_index = 0

                    if rect_option_yellow.collidepoint(event.pos):
                        print('boton amarillo')
                        if counter_yellow > counter_blue:
                            score += 1
                            current_question_index += 1
                        else:
                            score = 0
                            current_question_index = 0
                                
            if score == 10:
                score_pos = (671, 264)

            draw_screen(screen, score, score_font, colors, current_question_index, score_pos, current_color_voter, triangles)

        pg.display.flip()

