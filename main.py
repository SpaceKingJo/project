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
from firewood import Firewood

from pico2d import *


os.chdir('resource\\image')
running = None
hero = None
wood = None
fire = None
ui = None
torch = None
#키보드 입력
def handle_events():
    global hero
    global wood
    global running
    global fire
    global ui
    global torch
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
            if(hero.ability == 0):
                pass
            elif(torch.die == False):
                hero.attack_num += 1
                hero.ability -= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            if(fire.collide):
                ui.firewood_num -= 1
                fire.life += 100
        elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
            if(fire.collide):
                torch.die = False
                torch.life += 100
                fire.life -= 100
        elif event.type == SDL_KEYDOWN and event.key == SDLK_c:
            if(fire.collide):
                hero.ability += 1
                fire.life -= 100
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
                Hero.left_down = False
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
                Hero.right_down = False


def main():


    open_canvas()


    #클래스 선언
    global hero
    hero = Hero()
    rabbit = Rabbit()
    rabbit_group = [Rabbit() for i in range(20)]
    land = Land()
    wood = Wood()
    global torch
    torch = Torch()
    global fire
    fire = Fire()
    attack_fire = Attack_fire()
    attack_fire_group = [Attack_fire() for i in range(100)]
    background = BackGround()
    global ui
    ui = Ui()
    firewood = Firewood()
    firewood_group = [Firewood() for i in range(20)]

    #변수 선언
    rabbit_group_counter = 0
    rabbit_group_collision_counter = 0
    attack_group_counter = 0
    attack_group_update_counter = 0
    attack_group_collision_counter = 0
    rabbit_alive_counter = 0
    attack_group_alive_check = False
    attack_group_alive_counter = 0
    attack_group_limit = 20


    global running
    running = True



    while running:
        #핸들 이벤트
        handle_events()

        #업데이트
        hero.update()
        background.update()
        land.update()
        wood.update()
        fire.update()
        torch.update()
        ui.update(hero.x, hero.y, hero.ability)
        for rabbit in rabbit_group: # 토끼 업데이트
            if(rabbit_group_counter == rabbit.num):
                rabbit_group_counter = 0
                break
            if(rabbit.alive):
                rabbit.update()
            rabbit_group_counter += 1
        for attack_fire in attack_fire_group: # 공격불 업데이트
            if(attack_group_update_counter == hero.attack_num):
                attack_fire.init_direction()
                attack_fire.alive = True # 공격불이 활성화 됨
                attack_fire.init_fire()
                attack_group_update_counter = 0
                break
            if(attack_fire.alive):
                attack_fire.update()
            attack_group_update_counter += 1

        for firewood in firewood_group: # 장작불 업데이트
            firewood.update()

        #함수
        for rabbit in rabbit_group: #토끼와 히어로의 충돌체크
            if(rabbit_group_collision_counter == rabbit.num):
                rabbit_group_collision_counter = 0
                break
            if(collision(rabbit, hero)):
                rabbit.y += 50
            rabbit_group_collision_counter += 1

        for rabbit in rabbit_group: # 토끼와 공격불의 충돌체크
            for attack_fire in attack_fire_group:
                if(attack_group_collision_counter == hero.attack_num):
                    attack_group_collision_counter = 0
                    break
                if(collision(rabbit, attack_fire) and rabbit.alive and attack_fire.alive):
                    attack_fire.alive = False
                    rabbit.alive = False
                attack_fire.die = False
                attack_group_collision_counter += 1

        if(collision(wood, hero)): # 나무와 주인공 충돌체크
            fire.collide = True
        else:
            fire.collide = False

        for firewood in firewood_group: # 장작불 주인공 충돌체크
            if(collision(firewood, hero) and firewood.die == False):
                ui.firewood_num += 1
                firewood.die = True

        for rabbit in rabbit_group: # 토끼 출현!
            if(rabbit_alive_counter == rabbit.num):
                break
            rabbit.alive = True
            print("%d %d" % (rabbit.num, rabbit_alive_counter))
            rabbit_alive_counter += 1

        for attack_fire in attack_fire_group: # 불 스킬 존재 유무
            if(attack_fire.alive):
                attack_group_alive_counter = 0
                break
            attack_group_alive_counter += 1
            if(attack_group_alive_counter == hero.attack_num):
                hero.attack_num = 0


        for attack_fire in attack_fire_group: # 화면 밖을 벗어나면 불 스킬 사망 판정
            if(attack_fire.x >= 900 or attack_fire.x <= -100):
                attack_fire.alive = False

        print("%d" % hero.attack_num)
        clear_canvas()


        #그리기
        background.draw()
        fire.draw()
        wood.draw()
        torch.draw()
        hero.draw()
        # hero.draw_bb()
        for rabbit in rabbit_group: # 적토끼 출력
            if(rabbit.alive):
                rabbit.draw()
            # rabbit.draw_bb()
        for attack_fire in attack_fire_group: # 공격 불 출력
            if(attack_group_counter == hero.attack_num):
                attack_group_counter = 0
                break
            if(attack_fire.alive):
                attack_fire.draw()
            # attack_fire.draw_bb()
            attack_group_counter += 1
        for firewood in firewood_group: # 장작불 출력
            firewood.draw()
        land.draw()
        ui.draw()


        update_canvas()

        delay(0.08)

    close_canvas()


if __name__ == '__main__':
    main()