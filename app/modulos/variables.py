import pygame as pg 

pg.init()

SIZE_SCREEN = (800, 600)
PREGUNTA_CONSTANTE = 'Que prefieres?'

tittle_game = 'this_or_that.py'
answer_blue = [
    'Python',
    'Funciones como args de funciones',
    'Programación orientada a objetos',
    'Desarrollo en la terminal',
    'Aprender a programar en Python',
    'Código limpio desde el principio',
    'Documentar a medida que escribes',
    'Escribir tus propios algoritmos',
    'Programación en equipo',
    'Usar funciones lambda'
]

answer_yellow = [
    'JavaScript',
    'Trabajar con funciones independientes',
    'Programación funcional',
    'Desarrollo con un entorno gráfico',
    'Aprender a programar en C',
    'Escribir rápido y luego refactorizar',
    'Documentar el código cuando finalizas',
    'Usar librerías existentes',
    'Trabajo autónomo',
    'Usar funciones definidas con def'
]

colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'purple': (255, 0, 255)
}

font = pg.font.SysFont('Arial', 22)
text_score = font.render('Score', True, colors['black'])
score = 0
score_font = pg.font.SysFont('Arial', 60)
score_pos = (685, 264)

main_stand = pg.image.load('./app/resources/img/main_stand.png')
logo_py = pg.image.load('./app/resources/img/logo_py.png')
questions_poster = pg.image.load('./app/resources/img/questions_poster.png')
score_poster = pg.image.load('./app/resources/img/score_poster.png')
option_blue = pg.image.load('./app/resources/img/option_blue.png')
option_yellow = pg.image.load('./app/resources/img/option_yellow.png')
player = pg.image.load('./app/resources/img/player.png')
voter_m = pg.image.load('./app/resources/img/voter_m.png')
voter_f = pg.image.load('./app/resources/img/voter_f.png')
podium = pg.image.load('./app/resources/img/podium.png')
tribune = pg.image.load('./app/resources/img/tribune.jpg')
main_menu = pg.image.load('./app/resources/img/main_menu.png')

main_stand_route = './app/resources/img/main_stand.png'
logo_py_route = './app/resources/img/logo_py.png'
questions_poster_route = './app/resources/img/questions_poster.png'
score_poster_route = './app/resources/img/score_poster.png'
option_blue_route = './app/resources/img/option_blue.png'
option_yellow_route = './app/resources/img/option_yellow.png'
player_route = './app/resources/img/player.png'
voter_m_route = './app/resources/img/voter_m.png'
voter_f_route = './app/resources/img/voter_f.png'
podium_route = './app/resources/img/podium.png'
tribune_route = './app/resources/img/tribune.jpg'
main_menu_route = './app/resources/img/main_menu.png'
ranking_image_route = './app/resources/img/ranking.png'

item_sound = './app/resources/snd/collision_sound.mp3'
music_sound = './app/resources/snd/music.mp3'

font_daydream = './app/resources/fnt/Daydream.ttf'

RANKING_ROUTE = './app/ranking.csv'

images = {
    'podiums':{
        'low': pg.transform.scale(podium, (90, 90)),
        'mid': pg.transform.scale(podium, (80, 80)),
        'high': pg.transform.scale(podium, (70, 70))
    },
    'people':{
        'player': pg.transform.scale(player, (370, 370)),
        'voter_f': pg.transform.scale(voter_f, (200, 200)),
        'voter_m': pg.transform.scale(voter_m, (200, 200))
    },
    'options':{
        'blue': pg.transform.scale(option_blue, (200, 40)),
        'yellow': pg.transform.scale(option_yellow, (265, 150))
    },
    'posters':{
        'questions': pg.transform.scale(questions_poster, (700, 200)),
        'score': pg.transform.scale(score_poster, (200, 200))
    },
    'scenery':{
        'tribune': pg.transform.scale(tribune, (800, 900)),
        'logo_py': pg.transform.scale(logo_py, (100, 100)),
        'main_stand': pg.transform.scale(main_stand, (150, 200))
    }
}
triangles = [
    [(209, 410),(230, 410),(220, 395)],
    [(328, 410),(349, 410),(339, 395)],
    [(446, 410),(467, 410),(457, 395)],
    [(556, 410),(577, 410),(567, 395)],
    [(267, 330),(287, 330),(277, 315)],
    [(387, 330),(407, 330),(397, 315)],
    [(502, 330),(522, 330),(512, 315)],
    [(327, 260),(345, 260),(336, 245)],
    [(447, 260),(465, 260),(456, 245)]
]

current_color_voter = [
    colors['black'],
    colors['black'],
    colors['black'],
    colors['black'],
    colors['black'],
    colors['black'],
    colors['black'],
    colors['black'],
    colors['black']
]