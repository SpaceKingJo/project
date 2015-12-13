import os

from hero import Hero
from pico2d import *

class Fire:

    frame_switch = False
    def __init__(self):
        self.frame_x = 0
        self.frame_y = 0
        self.x = 400
        self.y = 200
        self.life = 1000
        self.die = False
        self.image = load_image('fire4.png')
        self.font = load_font("ConsolaMalgun.TTF", 17)

    def update(self):
        if(Hero.right_down):
            self.x -= Hero.speed
        elif(Hero.left_down):
            self.x += Hero.speed
        if(self.frame_x == 3):
            self.frame_x = 0
            self.frame_y += 1
        else:
            self.frame_x += 1
        if(self.frame_y == 3):
            self.frame_y = 1

        if(self.life == 0):
            self.die = True
        else:
            self.life -= 1


    def draw(self):
        self.font.draw(self.x - 40, self.y+40, "수명 : %d" % self.life, (1000, 1000, 1000))
        self.font.draw(self.x - 60, self.y+70, "장작 넣기 : z (능력-1 수명+10초)", (1000, 1000, 1000))
        self.font.draw(self.x - 60, self.y+90, "불 붙이기 : x (능력+3 수명-10초)", (1000, 1000, 1000))
        if(self.die != True):
            self.image.clip_draw(self.frame_x * 90, self.frame_y * 100, 90, 100, self.x, self.y)