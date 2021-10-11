from pynput.mouse import Controller
import time

mouse = Controller()

while True:
    print('The current pointer position is {0}'.format(mouse.position))
    time.sleep(0.3)
