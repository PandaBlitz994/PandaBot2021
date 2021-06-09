from robot import Robot
name = "light_reset"

def start():
    while True:
        print(Robot.gyro.angle())