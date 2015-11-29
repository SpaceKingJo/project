import os

from hero import Hero
from pico2d import *

class Torch:

    frame_switch = False
    def __init__(self):
        self.direction = 1 # 0은 왼쪽 1은 오른쪽
        self.frame_x = 0
        self.frame_y = 0
        self.x = 365
        self.y = 160
        self.image2 = load_image('stick.png')
        self.image = load_image('hero_fire.png')

    def update(self):
        if(Hero.right_down):
            self.direction = 1
        elif(Hero.left_down):
            self.direction = 0

        if(self.frame_x == 3):
            self.frame_x = 0
            self.frame_y += 1
        else:
            self.frame_x += 1
        if(self.frame_y == 3):
            self.frame_y = 0

    def draw(self):
        if(self.direction == 0):
            self.image2.clip_draw(0, 0, 35, 35, self.x+7, self.y-5)
            self.image.clip_draw(self.frame_x * 50, self.frame_y * 70, 50, 70, self.x-8, self.y+15)
        elif(self.direction == 1):
            self.image2.clip_draw(35, 0, 35, 35, self.x+60, self.y-5)
            self.image.clip_draw(self.frame_x * 50, self.frame_y * 70, 50, 70, self.x+75, self.y+15)