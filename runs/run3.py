from robot import Robot
from util.gyro import *

name = "Run 3"
def start():
    Robot.gyro.reset_angle(0)
    gyro_turn(90, 0.8)
    gyro_follow(2, 200, 0.7, 90) # check sensor above the line
    #line_follow(3, 200, 0.6, Robot.color_right)
    #gyro_turn(0, 0.7)
    #line_follow(2, 200, 0.6, Robot.color_right)
    #Robot.arm_left.run_angle(40, 55)
    gyro_follow(0.99, -150, 0.7, 0)
    gyro_turn(90, 0.8)
    gyro_follow(0.7, 120, 0.5, 90)
    gyro_turn(-20, 0.8)
    gyro_follow(0.3, 100, 0.4, -20)
    