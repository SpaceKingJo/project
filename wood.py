import os

from hero import Hero
from pico2d import *

class Wood:

    def __init__(self):
        self.x = 400
        self.y = 135
        self.image = load_image('wood2.png')

    def get_bb(self):
        return self.x - 30, self.y - 50, self.x + 30, self.y + 50

    def update(self):
        if(Hero.right_down):
            self.x -= Hero.speed
        elif(Hero.left_down):
            self.x += Hero.speed
    def draw(self):
        self.image.draw(self.x, self.y)