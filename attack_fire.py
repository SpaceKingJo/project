import os

from hero import Hero
from pico2d import *

class Attack_fire:

    frame_switch = False
    def __init__(self):
        self.x = 400
        self.y = 142
        self.speed = 7
        self.frame_x = 0
        self.frame_y = 0
        self.image = load_image('attack_fire.png')

    def init_direction(self):
        if(Hero.state == Hero.RIGHT_STAND or Hero.state == Hero.RIGHT_RUN):
            self.direction = 1 #오른쪽
        elif(Hero.state == Hero.LEFT_STAND or Hero.state == Hero.LEFT_RUN):
            self.direction = 0 #왼쪽

    def update(self):
        if(Hero.right_down):
            self.x -= Hero.speed
        elif(Hero.left_down):
            self.x += Hero.speed

        if(self.direction == 0):
            self.x -= self.speed
        else:
            self.x += self.speed
        if(self.frame_x == 3):
            self.frame_x = 0
            self.frame_y += 1
        else:
            self.frame_x += 1
        if(self.frame_y == 3):
            self.frame_y = 1

    def draw(self):
        self.image.clip_draw(self.frame_x * 70, self.frame_y * 80, 70, 80, self.x, self.y)