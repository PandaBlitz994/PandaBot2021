from robot import Robot
from util.gyro import *
from util.line_follow import *

name = "Run 4"
def start():
    #Robot.chassis.settings(straight_speed=170)
    #Robot.chassis.straight(920)
    Robot.arm_right.run_angle(-300, 120)
    drive_until_black(100, Robot.color_right)
    Robot.wheel_right.run_angle(300, 200)
    line_follow(2, 80, 2, Robot.color_right, 'L')
    Robot.wheel_right.run_angle(300, 300)
    Robot.chassis.straight(90)
    Robot.arm_right.run_angle(500, 180)
    line_follow(2.5, 160, 6, Robot.color_right, 'L')
    Robot.gyro.reset_angle(0)
    line_follow(1, 80, 2, Robot.color_right, 'L')
    gyro_follow(2, -150, 1, 0)
    Robot.wheel_left.run_angle(300, 230)
    Robot.chassis.straight(350)
    while True:
        gyro_follow(1.5, 60, 1.5, 90)
        gyro_follow(1.5, -60, 1.5, 90)

    