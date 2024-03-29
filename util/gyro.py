from robot import Robot
import time


def gyro_turn(degrees, kp):
    startPos = Robot.gyro.angle()
    while abs(Robot.gyro.angle() - degrees) > 3:
        error = Robot.gyro.angle() - (degrees + startPos)
        turn_rate = -error*kp

        Robot.chassis.drive(0, turn_rate)
    Robot.brake()

def gyro_follow(sec, vel, kp, target):
    start_time = time.time()
    while time.time() - start_time <= sec:
        currentAngle = Robot.gyro.angle()
        error = -1.5*(currentAngle - target)
        Robot.chassis.drive(vel, error*kp)
    Robot.brake()
