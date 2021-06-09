from robot import Robot
from util.gyro import *
from util.line_follow import *
import time

name = "run 1"


def start():
    Robot.gyro.reset_angle(0)
    Robot.chassis.straight(860)
    drive_until_black(25, Robot.color_left)
    gyro_follow(4, -90, 2, 30)
    drive_until_black(-100, Robot.color_right)
    gyro_follow(0.5, -70, 1, 0)
    line_follow(2, 130, 5, Robot.color_right, 'L')
    line_follow(3, 130, 4, Robot.color_right, 'L')
    line_follow(4, 130, 4, Robot.color_right, 'L')
    gyro_follow(1.06, 150, 1, -1)
    time.sleep(0.5)
    Robot.wheel_right.run_time(200, 9000)
    gyro_follow(1.5, -150, 1, 2)
    gyro_turn(10, 5)
    gyro_follow(4, -400, 6, 20)
    gyro_follow(4, -400, 2, 0)
    #Robot.arm_right.run_time(-200, 1000)
    #gyro_follow(1.6, -120, 1, -90)
    #gyro_turn(-180, 40)
    #gyro_follow(4, 200, 1, -180)
    Robot.brake()
