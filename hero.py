import os
import random

from pico2d import *


class Hero:
    image = None
    space_down = False
    left_down = False
    right_down = False
    frame_switch = False
    speed = 5

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND, LEFT_DASH, RIGHT_DASH = 1, 0, 2, 3, 4, 5

    def handle_left_run(self): # 왼쪽 걷기
        if(self.right_down):
            self.state = self.RIGHT_RUN
        elif(self.left_down == False):
            self.state = self.LEFT_STAND

    def handle_left_dash(self): # 왼쪽 뛰기
        self.x -= 10

    def handle_right_run(self): # 오른쪽 걷기
        if(self.left_down):
            self.state = self.LEFT_RUN
        elif(self.right_down == False):
            self.state = self.RIGHT_STAND

    def handle_right_dash(self): # 오른쪽 뛰기
        self.x += 10

    def handle_right_stand(self): # 오른쪽 서기
        if(self.right_down):
            self.frame = 0
            self.state = self.RIGHT_RUN
        elif(self.left_down):
            self.frame = 0
            self.state = self.LEFT_RUN


    def handle_left_stand(self): # 왼쪽 서기
        if(self.right_down):
            self.frame = 0
            self.state = self.RIGHT_RUN
            self.frame = 0
        elif(self.left_down):
            self.frame = 0
            self.state = self.LEFT_RUN
            self.frame = 0

    handle_state = { # 핸들 상태
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand,
        LEFT_DASH: handle_left_dash,
        RIGHT_DASH: handle_right_dash
    }


    def update(self):
        self.handle_state[self.state](self)
        if(self.frame == 2):
            self.frame_switch = True
        if(self.frame == 0):
            self.frame_switch = False

        if(self.frame_switch):
            self.frame -= 1
        else:
            self.frame += 1


        Hero.x = self.x
        Hero.y = self.y



    def __init__(self):
        self.x, self.y = 400, 145
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.RIGHT_STAND
        if Hero.image == None:
            Hero.image = load_image('Hero_character.png')


    def draw(self):
        if(self.state == self.RIGHT_STAND):
            self.image.clip_draw(240, 120, 60, 120, self.x, self.y)
        if(self.state == self.RIGHT_RUN):
            self.image.clip_draw((self.frame * 60) +180, 120, 60, 120, self.x, self.y)
        if(self.state == self.LEFT_STAND):
            self.image.clip_draw(240, 240, 60, 120, self.x, self.y)
        if(self.state == self.LEFT_RUN):
            self.image.clip_draw((self.frame * 60) + 180, 240, 60, 120, self.x, self.y)
        # if(self.state == 4):
        #     self.image.clip_draw(self.frame * 100, 0 * 100, 100, 100, self.x, self.y)
        # elif(self.state == 5):
        #     self.image.clip_draw(self.frame * 100, 1 * 100, 100, 100, self.x, self.y)
        # elif(True):
        #     self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)
