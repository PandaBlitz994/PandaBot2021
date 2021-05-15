from robot import Robot
from util.gyro import *
from util.line_follow import *

name = "run 2.1"
def start():
    Robot.gyro.reset_angle(0)
    gyro_follow(3.5, 150, 1, 0)
    line_follow(3, 150, 5.5, Robot.color_left, 'R')
    line_follow(5, 50, 5.5, Robot.color_left, 'R')
    line_follow(2.5, -100, 5.5, Robot.color_left, 'R')
    gyro_turn(-20, 1)
    gyro_follow(3, 100, 1, -20)
    #Robot.wheel_left.run_time(450, 5000)
    #gyro_follow(1, -100, 1, 0)
    #gyro_follow(10, -300, 1, 0)