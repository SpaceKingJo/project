import os
import random

from hero import Hero

from pico2d import *


class Rabbit:
    image = None
    space_down = False
    left_down = False
    right_down = False
    frame_switch = False
    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND, LEFT_DASH, RIGHT_DASH = 1, 0, 2, 3, 4, 5

    def __init__(self):
        if(random.randint(0, 1)):
            self.x, self.y = random.randint(-800, -200), 140
        else:
            self.x, self.y = random.randint(1000, 1600), 140
        self.frame = 0
        self.run_frames = 0
        self.stand_frames = 0
        self.alive = False
        self.die = False
        self.state = self.RIGHT_RUN
        if Rabbit.image == None:
            Rabbit.image = load_image('rabbit4.png')

    def handle_left_run(self): # 왼쪽 걷기
        if(self.x <= Hero.x):
            self.state = self.RIGHT_RUN
        else:
            self.x -= Hero.speed/2

    def handle_left_dash(self): # 왼쪽 뛰기
        pass

    def handle_right_run(self): # 오른쪽 걷기
        if(self.x >= Hero.x):
            self.state = self.LEFT_RUN
        else:
            self.x += Hero.speed/2

    def handle_right_dash(self): # 오른쪽 뛰기
        pass

    def handle_right_stand(self): # 오른쪽 서기
        pass

    def handle_left_stand(self): # 왼쪽 서기
        pass

    handle_state = { # 핸들 상태
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand,
        LEFT_DASH: handle_left_dash,
        RIGHT_DASH: handle_right_dash
    }

    def get_bb(self):
        return self.x - 10, self.y - 50, self.x + 10, self.y + 50

    def update(self):
        if(self.frame == 2):
            self.frame_switch = True
        elif(self.frame == 0):
            self.frame_switch = False
        if(self.frame_switch == True):
            self.frame -= 1
        else:
            self.frame += 1
        self.handle_state[self.state](self)
        if(Hero.right_down):
            self.x -= Hero.speed
        elif(Hero.left_down):
            self.x += Hero.speed

    def draw(self):
        #if(self.state == self.RIGHT_STAND):
        # self.image.clip_draw(60, 0, 60, 100, self.x, self.y)
        if(self.state == self.RIGHT_RUN):
             self.image.clip_draw(self.frame * 60, 100, 60, 100, self.x, self.y)
        elif(self.state == self.LEFT_RUN):
             self.image.clip_draw(self.frame * 60, 200, 60, 100, self.x, self.y)
        # if(self.state == 4):
        #     self.image.clip_draw(self.frame * 100, 0 * 100, 100, 100, self.x, self.y)
        # elif(self.state == 5):
        #     self.image.clip_draw(self.frame * 100, 1 * 100, 100, 100, self.x, self.y)
        # elif(True):
        #     self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

