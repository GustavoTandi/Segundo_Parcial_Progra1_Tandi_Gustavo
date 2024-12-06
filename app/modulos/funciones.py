import json
import pygame as pg
import random
from .variables import (
    PREGUNTA_CONSTANTE, answer_blue, answer_yellow, RANKING_ROUTE, colors
)
from .auxiliares import(
    draw_options, draw_people, draw_posters, draw_scenery, show_text, draw_scores, draw_podiums
)

def generate_answers(PREGUNTA_CONSTANTE, answer_blue, answer_yellow, name_archive = 'questions_and_options'):
    dates = {
        'question': PREGUNTA_CONSTANTE,
        'answers':[]
    }
    for i in range(len(answer_blue)):
        dates['answers'].append({
            'option_blue': answer_blue[i],
            'option_yellow': answer_yellow[i]
        })
    with open(name_archive, 'w') as archive:
        json.dump(dates, archive, indent=4)

def draw_screen(screen: pg.surface, score: int, score_font, colors,current_question_index, score_pos, current_color_voter, triangles):
    '''
    Dibuja la pantalla con todos los elementos
    '''
    with open('./app/questions_and_options', 'r') as file:
        data = json.load(file)
    answers = data['answers']

    draw_scenery(screen)

    draw_people(screen)

    draw_posters(screen)

    show_text(screen, PREGUNTA_CONSTANTE, 45, 'white',(280, 17))

    show_text(screen, 'SCORE', 19, 'black', (670,250))

    draw_scores(screen, score, score_font, score_pos, colors)

    draw_options(screen)

    current_answer = answers[current_question_index]
    option_blue = current_answer['option_blue']
    option_yellow = current_answer['option_yellow']
    show_text(screen, option_blue, 13, 'white', (170, 105))
    show_text(screen, option_yellow, 13, 'black', (449, 105))

    draw_podiums(screen)

    for voter in range(9):
        pg.draw.polygon(screen, current_color_voter[voter], triangles[voter])

def load_ranking():
    ranking = []
    with open(RANKING_ROUTE, 'r') as rkng:
        lineas = rkng.read()
        for linea in lineas.split('\n'):
            ranking.append(linea.split(','))
    sort_matrix(ranking)

    return ranking

def sort_matrix(matrix: list[list]):

    for i in range(len(matrix)-1):
        for j in range(i+1, len(matrix)):
            if int(matrix[i][1]) < int(matrix[j][1]):
                matrix[i], matrix[j] = matrix[j], matrix[i]

def color_selection(color_uno, color_dos) -> tuple[int, int]:
    '''
    Elige un color de dos posibles de forma aleatoria 
    '''
    color = random.choice([color_uno, color_dos])
    return colors[color]
