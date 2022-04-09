from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
keys = ['a', 'w', 's', 'd']
i = 0
while True:
    keyboard.press(keys[i])
    time.sleep(1)
    keyboard.release(keys[i])
    time.sleep(5)
    i+=1
    if (i>=len(keys)):
        i=0
