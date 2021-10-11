from pynput.mouse import Controller as mouse1, Button
from pynput.keyboard import Controller, Key, Listener
import time
import random

sense = Listener()
mouse = mouse1()
KB = Controller()
num = 5
numtime = random.randint(5, 20,) / 100

def typ(str):
    for i in str:
        if i == ' ':
            KB.press(Key.space)
            time.sleep(numtime)
        else:
            KB.press(i)
            KB.release(i)
            time.sleep(numtime)


#for i in range(num):
    #KB.type('Hello')
    #KB.press(Key.enter)
    #KB.release(Key.enter)
    #time.sleep(1)

txt = input('text:')
mouse.position = (793, 1825)
mouse.click(Button.left, 1)
typ(txt)
time.sleep(6)
for i in txt:
    KB.press(Key.backspace)
    KB.release(Key.backspace)
    time.sleep(0.2)
typ('Tu pues')
KB.press(Key.enter)
KB.release(Key.enter)




