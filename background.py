import os

from hero import Hero
from pico2d import *

class BackGround:
    def __init__(self):
        self.x = 400
        self.y = -150
        self.stage = 1
        self.image = load_image('background.png')
        self.image2 = load_image('stage2.png')
        self.bgm = load_music('21_Track_21.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def update(self):
        if(Hero.right_down):
            self.x -= Hero.speed/2
        elif(Hero.left_down):
            self.x += Hero.speed/2

    def stage3_music(self):
        self.bgm = load_music('쯔바이+환상의+대륙+셀펜티나.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def stage5_music(self):
        self.bgm = load_music('04 - Cats on Mars.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x + 800, self.y)
        self.image.draw(self.x - 800, self.y)
        if(self.stage >= 3):
            self.image2.draw(self.x, self.y + 400)
            self.image2.draw(self.x + 799, self.y + 399)
            self.image2.draw(self.x - 799, self.y + 399)
