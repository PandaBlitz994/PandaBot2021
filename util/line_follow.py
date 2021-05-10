from robot import Robot
from util import buttons
from pybricks.parameters import Button
import time

def light_reset():
    buttons.wait_for_press(Button.CENTER)
    Black = Robot.color_left.reflection()
    buttons.wait_for_press(Button.CENTER)
    White = Robot.color_left.reflection()
    avg = White * Black /2
    return avg
    


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

