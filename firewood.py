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
        self.die = False
    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def update(self):
        if(self.die == False):
            if(Hero.right_down):
                self.x -= Hero.speed
            elif(Hero.left_down):
                self.x += Hero.speed
    def draw(self):
        if(self.die == False):
            self.image.draw(self.x, self.y)