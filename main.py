import sys
import os

os.chdir('resource\\image')
import random
from pico2d import *

running = None

class Land:
    x = 0
    y = 0

    def __init__(self):
        Land.x = 400
        Land.y = 45
        self.image = load_image('land.png')

    def draw(self):
        self.image.draw(Land.x, Land.y)
        self.image.draw(Land.x + 800, Land.y)
        self.image.draw(Land.x - 800, Land.y)

class BackGround:
    x = 0
    y = 0

    def __init__(self):
        BackGround.x = 400
        BackGround.y = -150
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(BackGround.x, BackGround.y)
        self.image.draw(BackGround.x + 800, BackGround.y)
        self.image.draw(BackGround.x - 800, BackGround.y)

class Dark:
    image = None
    x, y = 0, 0

    def __init__(self):
        Dark.x, Dark.y = 100, 140
        if Dark.image == None:
            Dark.image = load_image('character4.png')

    def draw(self):
        self.image.clip_draw(0, 0, 60, 120, Dark.x, Dark.y)

class Boy:
    image = None
    space_down = False
    left_down = False
    right_down = False




    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND, LEFT_DASH, RIGHT_DASH = 1, 0, 2, 3, 4, 5


    def handle_left_run(self): # 왼쪽 걷기
        if(self.left_down == False):
            self.state = self.LEFT_STAND
        else:
            Dark.x += 5
            BackGround.x += 2
            Land.x += 5



    def handle_left_dash(self): # 왼쪽 뛰기
        self.x -= 10

    def handle_right_run(self): # 오른쪽 걷기
        if(self.right_down == False):
            self.state = self.RIGHT_STAND
        else:
            Dark.x -= 5
            BackGround.x -= 2
            Land.x -= 5

    def handle_right_dash(self): # 오른쪽 뛰기
        self.x += 10

    def handle_right_stand(self):
        if(self.right_down):
            self.state = self.RIGHT_RUN
        elif(self.left_down):
            self.state = self.LEFT_RUN
    def handle_left_stand(self):
        if(self.right_down):
            self.state = self.RIGHT_RUN
        elif(self.left_down):
            self.state = self.LEFT_RUN





    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand,
        LEFT_DASH: handle_left_dash,
        RIGHT_DASH: handle_right_dash
    }


    def update(self):
        self.frame = (self.frame+1) % 4
        self.handle_state[self.state](self)




    def __init__(self):
        self.x, self.y = 400, 145
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.RIGHT_STAND
        if Boy.image == None:
            Boy.image = load_image('main_character3.png')

    def draw(self):
        if(self.state == self.RIGHT_STAND):
            self.image.clip_draw(0, 0, 60, 120, self.x, self.y)
        elif(self.state == self.RIGHT_RUN):
            self.image.clip_draw(self.frame * 60, 0, 60, 120, self.x, self.y)
        elif(self.state == self.LEFT_STAND) :
            self.image.clip_draw(180, 120, 60, 120, self.x, self.y)
        elif(self.state == self.LEFT_RUN):
            self.image.clip_draw(self.frame * 60, 120, 60, 120, self.x, self.y)
        # if(self.state == 4):
        #     self.image.clip_draw(self.frame * 100, 0 * 100, 100, 100, self.x, self.y)
        # elif(self.state == 5):
        #     self.image.clip_draw(self.frame * 100, 1 * 100, 100, 100, self.x, self.y)
        # elif(True):
        #     self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            Boy.space_down = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            Boy.left_down = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            Boy.right_down = True
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            Boy.left_down = False
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            Boy.right_down = False

def main():

    open_canvas()

    boy = Boy()
    dark = Dark()
    land = Land()
    background = BackGround()

    global running
    running = True

    while running:
        handle_events()

        boy.update()

        clear_canvas()
        background.draw()
        boy.draw()
        dark.draw()
        land.draw()
        update_canvas()

        delay(0.08)

    close_canvas()


if __name__ == '__main__':
    main()