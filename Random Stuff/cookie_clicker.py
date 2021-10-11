from pynput.mouse import Controller, Button
import time

mouse = Controller()
start_time = time.time()
elapsed_time = time.time() - start_time
number = 0

#mouse.position = (320, 470)

#while elapsed_time < 5:
    #mouse.press(Button.left)
    #mouuse.release(Button.left)
    #time.sleep(0.01)
   
time.sleep(3)
while number < 500:
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.1)
    number += 1
    
#if elapsed_time > 5:
    #quit()