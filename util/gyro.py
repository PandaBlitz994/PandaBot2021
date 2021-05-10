from robot import Robot
import time


def gyro_turn(degrees, vel, kp):
    startPos = Robot.gyro.angle()
    while Robot.gyro.angle() != degrees:
        error = Robot.gyro.angle() - (degrees + startPos)
        Robot.chassis.drive(vel, error*kp)
    Robot.chassis.stop()

def gyro_follow(time, vel, kp, target):
    start_time = time.time()
    while time.time() - start_time <= time:
        currentAngle = Robot.gyro.angle()
        error = currentAngle - target
        Robot.chassis.drive(vel, error*kp)
    Robot.chassis.stop()
