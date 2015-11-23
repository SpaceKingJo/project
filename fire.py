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
        self.image = load_image('fire3.png')

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
            self.frame_y = 0

    def draw(self):
        self.image.clip_draw(self.frame_x * 90, self.frame_y * 80, 90, 80, self.x, self.y)