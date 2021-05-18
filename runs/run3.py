from robot import Robot
from util.gyro import *
from util.line_follow import *

name = "Run 3"
def start():
    Robot.arm_left.run_time(-120, 300)
    Robot.gyro.reset_angle(0)
    drive_until_black(170, Robot.color_right)
    line_follow(0.6, 20, 7, Robot.color_right, 'L')
    line_follow(2.5, 190, 5.5, Robot.color_right, 'L')
    gyro_turn(-84, 8)
    line_follow(1.5, 40, 7, Robot.color_right, 'L')
    line_follow(2.9, 140, 2.5, Robot.color_right, 'L')
    gyro_follow(2.4, 150, 10, -90)
    Robot.arm_left.run_time(500, 1000)
    gyro_follow(1,-250,10,-90)
    gyro_turn(-145,7)
    gyro_follow(2.6,160,10,-145)    
    while True:
        gyro_follow(0.5, 30, 1, 90)
        gyro_follow(0.5, -30, 1, 90)