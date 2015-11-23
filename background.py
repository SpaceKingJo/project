import os

from hero import Hero
from pico2d import *

class BackGround:
    def __init__(self):
        self.x = 400
        self.y = -150
        self.image = load_image('background.png')

    def update(self):
        if(Hero.right_down):
            self.x -= Hero.speed/2
        elif(Hero.left_down):
            self.x += Hero.speed/2

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x + 800, self.y)
        self.image.draw(self.x - 800, self.y)