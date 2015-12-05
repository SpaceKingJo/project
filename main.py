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
from collision import *
from background import BackGround
from ui import Ui

from pico2d import *


os.chdir('resource\\image')
running = None


#키보드 입력
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


    #클래스 선언
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
    ui = Ui()


    #변수 선언
    rabbit_group_counter = 0
    rabbit_group_collision_counter = 0
    attack_group_counter = 0
    attack_group_update_counter = 0
    attack_group_collision_counter = 0



    global running
    running = True



    while running:
        handle_events()

        #업데이트
        hero.update()
        background.update()
        land.update()
        wood.update()
        fire.update()
        torch.update()
        ui.update(hero.x, hero.y)
        for rabbit in rabbit_group:
            rabbit.update()
        for attack_fire in attack_fire_group:
            if(attack_group_update_counter == Hero.attack_num):
                attack_fire.init_direction()
                attack_group_update_counter = 0
                break
            attack_fire.update()
            attack_group_update_counter += 1

        #함수
        for rabbit in rabbit_group:
            if(rabbit_group_collision_counter == rabbit.num):
                rabbit_group_collision_counter = 0
                break
            if(collision(rabbit, hero)):
                rabbit.y += 50
            rabbit_group_collision_counter += 1

        for rabbit in rabbit_group:
            for attack_fire in attack_fire_group:
                if(attack_group_collision_counter == Hero.attack_num):
                    attack_group_collision_counter = 0
                    break
                if(collision(rabbit, attack_fire)):
                    rabbit.y += 400
                    attack_fire.y += 400
                attack_group_collision_counter += 1

        clear_canvas()


        #그리기
        background.draw()
        fire.draw()
        wood.draw()
        torch.draw()
        hero.draw()
        # hero.draw_bb()
        for rabbit in rabbit_group:
            rabbit.draw()
            # rabbit.draw_bb()
        for attack_fire in attack_fire_group:
            if(attack_group_counter == Hero.attack_num):
                attack_group_counter = 0
                break
            attack_fire.draw()
            # attack_fire.draw_bb()
            attack_group_counter += 1
        land.draw()
        ui.draw()


        update_canvas()

        delay(0.08)

    close_canvas()


if __name__ == '__main__':
    main()