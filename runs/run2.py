from robot import Robot
from util.gyro import *
from util.line_follow import * 


def start():
    light_avg = light_follow.light_reset()
    gyro.gyro_follow(10, 50, 2)
    


