from util.gyro import *
from robot import Robot
from util.line_follow import *

name = "run 2"
def start():
    Robot.gyro.reset_angle(0)
    gyro_follow(2.8, 170, 2, 0)
    gyro_turn(-20, 10)
    gyro_follow(0.7, -130, 1, -10)
    gyro_follow(3, -180, 5, 20)

    Robot.brake()

    
    