import os

from hero import Hero
from pico2d import *

class Mainback:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.image = load_image('mainback.png')
        self.image2 = load_image('classic_game_overl.png')
        self.image3 = load_image('win.png')
        self.bgm = load_music('The Last of Us OST - Track 11 - The Choice.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.hero_die = False
        self.eskimo_die = False

    def update(self):
        pass
    def win_sound(self):
        self.bgm = load_music('LC_mp_victory_soviet.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        pass
    def die_sound(self):
        self.bgm = load_music('17 - Memory.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        pass
    def draw(self):
        if(self.hero_die):
            self.image2.draw(self.x, self.y)
        elif(self.eskimo_die):
            self.image3.draw(self.x, self.y)
        else:
            self.image.draw(self.x, self.y)