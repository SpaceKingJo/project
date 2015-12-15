from hero import Hero
import random
from pico2d import *
class Firewood:

    image = None
    def __init__(self):
        if(random.randint(0, 1)):
            self.x, self.y = random.randint(0, 400), 140
        else:
            self.x, self.y = random.randint(400, 800), 140
        if(Firewood.image == None):
            Firewood.image = load_image('firewood.png')
        self.die = False
        self.alive = False
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