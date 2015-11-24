import sys
import os
import random

from hero import Hero
from land import Land
from rabbit import Rabbit
from wood import Wood
from fire import Fire
from torch import Torch
from background import BackGround

from pico2d import *


os.chdir('resource\\image')
running = None

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                Hero.space_down = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
                Hero.left_down = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
                Hero.right_down = True
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
                Hero.left_down = False
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
                Hero.right_down = False

def main():

    open_canvas()

    hero = Hero()
    rabbit = Rabbit()
    rabbit_group = [Rabbit() for i in range(20)]
    land = Land()
    wood = Wood()
    torch = Torch()
    fire = Fire()
    background = BackGround()

    global running
    running = True

    while running:
        handle_events()
        hero.update()
        background.update()
        land.update()
        wood.update()
        fire.update()
        torch.update()

        for rabbit in rabbit_group:
            rabbit.update()

        clear_canvas()
        background.draw()
        fire.draw()
        wood.draw()
        torch.draw()
        hero.draw()
        for rabbit in rabbit_group:
            rabbit.draw()
        land.draw()
        update_canvas()

        delay(0.08)

    close_canvas()


if __name__ == '__main__':
    main()