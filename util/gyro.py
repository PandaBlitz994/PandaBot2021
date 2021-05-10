from robot import Robot
import time

def gyro_turn(degrees, vel, side):
    Robot.reset_gyro()
    start_angle = Robot.gyro.angle()
    if side == 'left':
        vel = -vel
    while True:
        drive(0, vel)
        current_angle = Robot.gyro.angle()
        if abs(start_angle - current_angle) == degrees:
            Robot.chassis.stop()
            break

def gyro_follow(time, vel, kp):
    run = True
    angle = Robot.gyro.angle()
    start_time = time.time()
    Robot.chassis.drive(vel, 0)
    while run:
        current_time = time.time()
        if current_angle > angle:
            #
            pass

        if current_angle < 0:
            turn_rate = -kp
        
        if current_time - start_time >= time:
            Robot.chassis.stop()
            run = False
        

