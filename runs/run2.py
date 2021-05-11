from robot import Robot
from util.gyro import *


name = "Run 2"
def start():
    Robot.gyro.reset_angle(0)
    gyro_turn(90, 0.7)
    print(Robot.gyro.angle())
    gyro_follow(9, 200, 1, 90)
    print(Robot.gyro.angle())
    Robot.wheel_left.run_time(500, 4)
    gyro_follow(1, -100, 1, 90)
    gyro_follow(10, -200, 1, 90)
        
        


    


