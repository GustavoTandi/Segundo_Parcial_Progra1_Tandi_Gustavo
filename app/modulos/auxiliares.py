import pygame as pg
from .variables import(
    images, colors, score_font, score_font
)

def draw_podiums(screen: pg.Surface):
    '''
    Dibuja los podios en sus respectivas posiciones

    screen: Superficie en la cual van a ser dibujados
    '''
    podium_position_low = [(174, 373), (292 , 373), (410, 373), (520, 373)]
    podium_position_mid = [(235, 295), (355, 295), (470, 295)]
    podium_position_high = [(300, 228), (420, 228)]
    main_stand_position = (10, 400)


    for i in podium_position_low:
        screen.blit(images['podiums']['low'], i)
    for i in podium_position_mid:
        screen.blit(images['podiums']['mid'], i)
    for i in podium_position_high:
        screen.blit(images['podiums']['high'], i)
    screen.blit(images['scenery']['main_stand'], main_stand_position)


def draw_people(screen: pg.surface):
    '''
    Dibuja las personas en sus respectivas posiciones

    screen: Superficie en la cual van a ser dibujados
    '''
    player_position = (-86, 255)
    voterf_position = [(238, 284), (467, 284), (179, 197), (411, 197), (358, 120)]
    voterm_position = [(121, 285), (355, 285), (295, 197), (236, 124)]

    screen.blit(images['people']['player'], player_position)
    for i in voterf_position:
        screen.blit(images['people']['voter_f'], i)
    for i in voterm_position:
        screen.blit(images['people']['voter_m'], i)

def draw_options(screen: pg.surface):
    '''
    Dibuja las opciones en sus respectivas posiciones

    screen: Superficie en la cual van a ser dibujados
    '''
    option_blue_position = (160, 95)
    option_yellow_position = (409, 39)

    screen.blit(images['options']['blue'], option_blue_position)
    screen.blit(images['options']['yellow'], option_yellow_position)

def draw_posters(screen: pg.surface):
    '''
    Dibuja los carteles en sus respectivas posiciones
    
    screen: Superficie en la cual van a ser dibujados
    '''
    questions_poster_position = (30, -12)
    score_poster_position = (600, 200)

    screen.blit(images['posters']['questions'], questions_poster_position)
    screen.blit(images['posters']['score'], score_poster_position)

def draw_scenery(screen: pg.surface):
    '''
    Dibuja el escenario en la pantalla
    
    screen: Superficie en la cual van a ser dibujado
    '''
    tribune_position = (0, -200)
    logo_py_position = (350, 65)

    screen.blit(images['scenery']['tribune'], tribune_position)
    screen.blit(images['scenery']['logo_py'], logo_py_position)

def show_text(screen: pg.Surface,text: str, size: int, color: str, position: tuple[int, int]) -> str:
    '''
    Muestra texto en la pantalla

    Args:
    screen (pg.Surface): Superficie donde se mostrará la pregunta
    text (str): Texto a mostrar
    size (int): Tamaño del texto
    color (str): Color del texto
    position (tuple(int, int)): Coordenadas de la pantalla donde se mostrará el texto
    '''
    font = pg.font.SysFont('Arial', size)
    text = font.render(text, True, colors[color])
    screen.blit(text, position)

def draw_scores(screen: pg.Surface, score: int, score_font, score_pos: tuple, colors: list):
    '''
    Dibuja los puntajes en la pantalla
    '''
    score_view = score_font.render(f'{score}', True, colors['black'])
    screen.blit(score_view, score_pos)



