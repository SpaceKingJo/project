import sys
import os
import random

from hero import Hero
from land import Land
from rabbit import Rabbit
from wood import Wood
from fire import Fire
from torch import Torch
from attack_fire import Attack_fire
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
                Hero.right_down = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
                Hero.right_down = True
                Hero.left_down = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
                Hero.attack_num += 1
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
    attack_fire = Attack_fire()
    attack_fire_group = [Attack_fire() for i in range(20)]
    background = BackGround()

    rabbit_group_counter = 0
    attack_group_counter = 0
    attack_group_update_counter = 0

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
        for attack_fire in attack_fire_group:
            if(attack_group_update_counter == Hero.attack_num):
                attack_fire.init_direction()
                attack_group_update_counter = 0
                break
            attack_fire.update()
            attack_group_update_counter += 1

        clear_canvas()
        background.draw()
        fire.draw()
        wood.draw()
        torch.draw()
        hero.draw()
        for rabbit in rabbit_group:
            rabbit.draw()
        for attack_fire in attack_fire_group:
            if(attack_group_counter == Hero.attack_num):
                attack_group_counter = 0
                break
            attack_fire.draw()
            attack_group_counter += 1
        land.draw()
        update_canvas()

        delay(0.08)

    close_canvas()


if __name__ == '__main__':
    main()