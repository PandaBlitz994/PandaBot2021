from robot import Robot
from util.gyro import *
from util.line_follow import *


name = "Run 2"
def start():
    Robot.gyro.reset_angle(0)
    gyro_follow(2.4, 150, 1, 0)
    line_follow(10, 150, 5.5, Robot.color_right, 'R')
    Robot.wheel_left.run_time(450, 5000)
    gyro_follow(1, -100, 1, 0)
    gyro_follow(10, -300, 1, 0)
        
        


    


