from util.gyro import *
from robot import Robot
from util.line_follow import *

name = "run1"
def start():
    Robot.gyro.reset_angle(0)
    gyro_follow(2.7, 180, 1, 0)
    gyro_follow(3, -180, 1, 0)
    gyro_turn(20, 10)

    
    