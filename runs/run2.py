from robot import Robot
from util.gyro import *
import time


name = "gyro test"
def start():
    Robot.gyro.reset_angle(0)
    gyro_turn(90, 0.6)
    print(Robot.gyro.angle())
    gyro_follow(8, 200, 1, 90)
    print(Robot.gyro.angle())
    Robot.wheel_right.run(500)
    time.sleep(6)
    Robot.wheel_right.stop()
    gyro_follow(1, -100, 1, 90)
    gyro_follow(10, -200, 1, 90)
        
        


    


