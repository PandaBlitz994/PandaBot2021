from robot import Robot
from util.gyro import *
from util.line_follow import *
import time

name = "Run 3"
def start():
    Robot.gyro.reset_angle(0)
    gyro_follow(5.5, 200, 6, 0)
    gyro_follow(6, -200, 6, 0)
