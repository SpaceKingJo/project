import os

from pico2d import *

def collision(a, b):
    left_a, right_a = a.get_bb()
    left_b, right_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False

    return True

