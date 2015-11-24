import os

from hero import Hero
from pico2d import *

class Torch:

    frame_switch = False
    def __init__(self):
        self.frame_x = 0
        self.frame_y = 0
        self.x = 365
        self.y = 160
        self.image2 = load_image('stick.png')
        self.image = load_image('hero_fire.png')

    def update(self):
        if(self.frame_x == 3):
            self.frame_x = 0
            self.frame_y += 1
        else:
            self.frame_x += 1
        if(self.frame_y == 3):
            self.frame_y = 0

    def draw(self):
        self.image2.draw(self.x, self.y)
        self.image.clip_draw(self.frame_x * 50, self.frame_y * 70, 50, 70, self.x-15, self.y+15)
