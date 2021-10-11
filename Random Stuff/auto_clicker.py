from pynput.mouse import Controller, Button
import time

mouse = Controller()
mouse.position = (341, 1474)
t_end = time.time() + 60


while t_end > time.time():
    mouse.click(Button.left, 1)
    time.sleep(0.01)

else:
    quit()

