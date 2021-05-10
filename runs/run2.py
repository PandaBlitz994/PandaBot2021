from robot import Robot
from util.gyro import *
from util.line_follow import * 


def start():
    Robot.gyro.reset_angle(0)
    light_avg = light_follow.light_reset()
    gyro.gyro_turn(90, 10, 0.2)
    gyro.gyro_follow(20, 30, 0.2, 90)
    


