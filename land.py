import os

from hero import Hero
from pico2d import *

class Land:

    def __init__(self):
        self.x = 400
        self.y = 45
        self.image = load_image('land.png')

    def update(self):
        if(Hero.right_down):
            self.x -= Hero.speed
        elif(Hero.left_down):
            self.x += Hero.speed
    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x + 800, self.y)
        self.image.draw(self.x - 800, self.y)