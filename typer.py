
import time as t
import keyboard as keykey

s = t.sleep



s(2)
print('cozmic typer has started press the "=" button on your keyboard to start and the "-" button to cancel. \n Have a good time (:')
while True:
    if keykey.is_pressed('='):
        for x in range(0, 50):
            if keykey.is_pressed("-"):

                exit()
            
            s(0.45)
            keykey.write("qwertyuiopasdfughjklzxcvbnm,.'; QWERTYUIOPASDGHJKLZXCVBNM")
#####


