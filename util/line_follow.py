from robot import Robot
from util import buttons
from pybricks.parameters import Button
import time

target = 18

def light_reset():
    buttons.wait_for_press(Button.CENTER)
    Black = Robot.color_left.reflection()
    print("BLACK:", Black)
    buttons.wait_for_press(Button.CENTER)
    White = Robot.color_left.reflection()
    print("White:", White)
    target = (White + Black) /2
    print("target", target)
    return target

def line_follow(sec, vel, kp, sensor, side):
    start_time = time.time()
    while time.time() - start_time < sec:
        error = sensor.reflection() - target
        print(sensor.reflection())
        print(error)
        if side == 'L':
            Robot.chassis.drive(vel, error*kp)
        elif side == 'R':
            Robot.chassis.drive(vel, -error*kp)
    Robot.chassis.stop()








"""
WHITE = 100
BLACK = 0
target = (WHITE + BLACK) / 2
    


def left(vel, time, a, side, kp, avg):
    TurnRate = 0
    settings(vel, a, TurnRate, 1)
    run = True
    while run:
        Black = Robot.color_left.reflection()
        White = Robot.color_left.reflection()
        current_avg = (Black + White)/2
        if current_avg > avg:
            if side == "Right":
                TurnRate += kp
            else:
                TurnRate -= kp
        elif current_avg < avg:
            if side == "Right":
                TurnRate -= kp
            else:
                TurnRate += kp



def right():
    '''
    בייסיקלי אותו הדבר
    '''
"""