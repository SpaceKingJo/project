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
from mainback import Mainback
from eskimo import Eskimo

from pico2d import *


os.chdir('resource\\image')
running = None
hero = None
wood = None
fire = None
ui = None
torch = None
start = None
mainback = None
#키보드 입력
def handle_events():
    global hero
    global wood
    global running
    global fire
    global ui
    global torch
    global start
    global mainback
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            start = True
            running = False
            if(mainback.hero_die):
                    mainback.hero_die = False
            if(mainback.eskimo_die):
                    mainback.eskimo_die = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                start = True
                if(mainback.hero_die):
                    mainback.hero_die = False
                if(mainback.eskimo_die):
                    mainback.eskimo_die = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
                Hero.left_down = True
                Hero.right_down = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
                Hero.right_down = True
                Hero.left_down = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a and start == True:
            if(hero.ability == 0):
                pass
            elif(torch.die == False):
                hero.attack_num += 1
                hero.ability -= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_c and start == True:
            if(fire.collide):
                ui.firewood_num -= 1
                fire.life += 100
        elif event.type == SDL_KEYDOWN and event.key == SDLK_x and start == True:
            if(fire.collide and fire.die == False):
                torch.die = False
                torch.life += 100
                fire.life -= 100
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z and start == True:
            if(fire.collide and fire.die == False):
                hero.ability += 1
                fire.life -= 100
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
                Hero.left_down = False
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
                Hero.right_down = False


def main():


    open_canvas()
    global mainback
    mainback = Mainback()
    global start
    start = False

    while(start == False):
        handle_events()
        clear_canvas()
        mainback.draw()
        update_canvas()
        delay(0.08)

    #클래스 선언
    global hero
    hero = Hero()
    rabbit = Rabbit()
    rabbit_group = [Rabbit() for i in range(600)]
    land = Land()
    wood = Wood()
    global torch
    torch = Torch()
    global fire
    fire = Fire()
    eskimo = Eskimo()
    attack_fire = Attack_fire()
    attack_fire_group = [Attack_fire() for i in range(100)]
    background = BackGround()
    global ui
    ui = Ui()
    firewood = Firewood()
    firewood_group = [Firewood() for i in range(600)]

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
    rabbit_group_draw_counter = 0
    firewood_num_counter = 0
    firewood_num_update_counter = 0
    firewood_collide_counter = 0
    rabbit_group_counter2 = 0
    rabbit_jump = False
    rabbit_num = 10
    firewood_num = 10
    rack_block = 0
    eskimo_counter = 0


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
        eskimo.update()
        ui.update(hero.x, hero.y, hero.ability)
        for rabbit in rabbit_group: # 토끼 업데이트
            if(rabbit_group_counter == rabbit_num):
                rabbit_group_counter = 0
                break
            if(rabbit.alive):
                rabbit.update()
            rabbit_group_counter += 1

        # for rabbit in rabbit_group: # 토끼 업데이트
        #     if(rabbit_group_counter2 == 1):
        #         print("%d" % rabbit.x)
        #         break
        #     rabbit_group_counter2 += 1

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

        for firewood in firewood_group: # 장작 업데이트
            if(firewood_num_update_counter == firewood_num):
                firewood_num_update_counter = 0
                break
            firewood.update()
            firewood_num_update_counter += 1

        #함수
        for rabbit in rabbit_group: #토끼와 히어로의 충돌체크
            if(rabbit_group_collision_counter == rabbit_num):
                rabbit_group_collision_counter = 0
                break
            if(collision(rabbit, hero)):
                rabbit.y += 50
                mainback.hero_die = True
                mainback.die_sound()
                running = False
            rabbit_group_collision_counter += 1

        for rabbit in rabbit_group: # 토끼와 공격불의 충돌체크
            if(rack_block == rabbit_num):
                rack_block = 0
                break
            for attack_fire in attack_fire_group:
                if(attack_group_collision_counter == hero.attack_num):
                    attack_group_collision_counter = 0
                    break
                if(collision(rabbit, attack_fire) and rabbit.alive and attack_fire.alive):
                    attack_fire.alive = False
                    rabbit.alive = False
                    rabbit.die = True
                    hero.kill += 1
                attack_fire.die = False
                attack_group_collision_counter += 1
            rack_block += 1

        for attack_fire in attack_fire_group:
            if(eskimo_counter == hero.attack_num):
                eskimo_counter = 0
                break
            if(collision(eskimo, attack_fire)):
                 attack_fire.alive = False
                 eskimo.x -= 10
                 eskimo.hp -= 1
                 if(eskimo.hp == 0):
                    mainback.eskimo_die = True
                    running = False
                    mainback.win_sound()
            attack_fire.die = False
            eskimo_counter += 1
        if(collision(wood, hero)): # 나무와 주인공 충돌체크
            fire.collide = True
            if(ui.firewood_num != 0):
                fire.life += ui.firewood_num*250
                ui.firewood_num = 0
        else:
            fire.collide = False


        if(collision(eskimo, hero)): # 주인공과 에스키모 충돌체크
            mainback.hero_die = True
            running = False
            mainback.die_sound()

        for firewood in firewood_group: # 장작과 주인공 충돌체크
            if(firewood_collide_counter == firewood_num):
                firewood_collide_counter = 0
                break
            if(collision(firewood, hero) and firewood.die == False):
                ui.firewood_num += 1
                firewood.die = True
            firewood_collide_counter += 1

        for rabbit in rabbit_group: # 토끼 출현!
            if(rabbit_alive_counter == rabbit_num):
                break
            if(rabbit.die == False):
                rabbit.alive = True
                rabbit_alive_counter += 1

        if(fire.die): # 불이 꺼지면 토끼들이 마구마구 몰려온다.
            rabbit_num = 500

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
        print("stage = %d" % background.stage)
        #스테이지
        if(hero.kill == 10 and background.stage == 1):
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            rabbit_num += 20
            hero.ability += 10
            firewood_num += 5
            background.stage = 2
        if(hero.kill == 30 and background.stage == 2):
            rabbit_num += 30
            firewood_num += 10
            hero.ability += 10
            background.stage = 3
            background.stage3_music()
        if(hero.kill == 60 and background.stage == 3):
            rabbit_num += 40
            firewood_num += 15
            hero.ability += 10
            background.stage = 4
        if(hero.kill == 80 and background.stage == 4):
            rabbit_num += 50
            firewood_num += 20
            hero.ability += 10
            background.stage = 5
            eskimo.alive = True
            background.stage5_music()
        if(background.stage == 5):
            rabbit_jump = True

        if(rabbit_jump):
             for rabbit in rabbit_group:
                 rabbit.y += 5

        # print("%d" % hero.attack_num)
        print("킬 수 : %d num : %d" % (hero.kill, rabbit_num))
        clear_canvas()


        #그리기
        background.draw()
        fire.draw()
        wood.draw()
        torch.draw()
        hero.draw()
        eskimo.draw()
        # eskimo.draw_bb()
        # hero.draw_bb()
        for rabbit in rabbit_group: # 적토끼 출력
            if(rabbit_group_draw_counter == rabbit_num):
                rabbit_group_draw_counter = 0
                break
            if(rabbit.alive):
                rabbit.draw()
            rabbit_group_draw_counter += 1
            # rabbit.draw_bb()
        for attack_fire in attack_fire_group: # 공격 불 출력
            if(attack_group_counter == hero.attack_num):
                attack_group_counter = 0
                break
            if(attack_fire.alive):
                attack_fire.draw()
            # attack_fire.draw_bb()
            attack_group_counter += 1
        for firewood in firewood_group: # 장작 출력
            if(firewood_num_counter == firewood_num):
                firewood_num_counter = 0
                break
            firewood.draw()
            firewood_num_counter += 1
        land.draw()
        ui.draw()



        update_canvas()

        delay(0.06)

    while(mainback.hero_die or mainback.eskimo_die):
        handle_events()
        clear_canvas()
        mainback.draw()
        update_canvas()
        delay(0.08)



    close_canvas()


if __name__ == '__main__':
    main()