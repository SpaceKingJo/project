from hero import Hero
import random
from pico2d import *
class Firewood:

    num = 20

    def __init__(self):
        if(random.randint(0, 2)):
            self.x, self.y = random.randint(-800, 400), 140
        else:
            self.x, self.y = random.randint(400, 1200), 140
        self.image = load_image('firewood.png')

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def update(self):
        if(Hero.right_down):
            self.x -= Hero.speed
        elif(Hero.left_down):
            self.x += Hero.speed
    def draw(self):
        self.image.draw(self.x, self.y)