import random

def is_left_empty():
    return random.randint(0, 1) < 0.8

def is_right_empty():
    return random.randint(0, 1) < 0.8

def is_front_empty():
    return random.randint(0, 1) < 0.5
