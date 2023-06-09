import time as t
import mouse
import keyboard

s = t.sleep
s(2)
print('cozmic clicker has started press the "=" button on your keyboard to start and the "-" button to cancel. \n Have a good time (:')
while True:
    if keyboard.is_pressed('='):
        for x in range(0, 300):
            if keyboard.is_pressed("-"):

                exit()
            s(0.01)
            mouse.click('left')
            


###