from robot import Robot
from util.gyro import *
from util.line_follow import *
import time

name = "run 2.1"
def start():
    Robot.gyro.reset_angle(0)
    Robot.arm_right.run_time(100, 700)
    gyro_follow(4.3, 200, 0.7, 3)
    gyro_follow(8.5, 25, 0.5, 3)
    gyro_follow(0.6, -100, 4, 20)
    gyro_follow(1.7, -170, 8, 40)
    drive_until_black(-100, Robot.color_right)
    gyro_follow(0.5, 50, 1, 30)
    gyro_follow(0.8, 40, 6, 0)
    line_follow(1, 120, 3 , Robot.color_right, 'L')
    line_follow(3, 170, 4, Robot.color_right, 'L')
    line_follow(2.2, 90, 2, Robot.color_right, 'L')
    gyro_follow(2, 10, 10, 10)
    gyro_follow(1.4, 130, 10, 15)
    time.sleep(0.5)
    Robot.wheel_left.run_time(200, 7777)
    gyro_follow(2, -120, 1, 5)
    gyro_follow(8, -180, 2, 5)

    #Robot.arm_right.run_time(-200, 1000)
    #gyro_follow(1.6, -120, 1, -90)
    #gyro_turn(-180, 40)
    #gyro_follow(4, 200, 1, -180)
