import pygame.mixer as mixer

class Sound:

    def __init__(self):
        mixer.init()

    def play_sound(self, route_snd: str):
        sound = mixer.Sound(route_snd)
        sound.set_volume(0.8)
        sound.play()
    
    def play_music(self, route_music: str):
        mixer.music.load(route_music)
        mixer.music.set_volume(0.1)
        mixer.music.play()

    def stop_music(self):
        mixer.music.fadeout(500)
