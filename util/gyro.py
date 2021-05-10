from robot import Robot
import time


def gyro_turn(degrees, kp):
    startPos = Robot.gyro.angle()
    while abs(Robot.gyro.angle() - degrees) > 1:
        error = Robot.gyro.angle() - (degrees + startPos)
        Robot.chassis.drive(0, error*kp)
    Robot.chassis.stop()

def gyro_follow(sec, vel, kp, target):
    start_time = time.time()
    while time.time() - start_time <= sec:
        currentAngle = Robot.gyro.angle()
        error = currentAngle - target
        Robot.chassis.drive(vel, error*kp)
    Robot.chassis.stop()
