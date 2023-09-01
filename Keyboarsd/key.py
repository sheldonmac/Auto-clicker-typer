import keyboard as key
import time as ti
import tkinter as tk

root = tk.Tk()
root.title("coztyper")


print('Welcome to CozTyper \nMade by Cozmo \nPress "=" to start brute forcing typer games and the "-" key to exit the app or press "]" for the afk mode')


while True:
    
        if key.is_pressed("="):
                for x in range(30):
                        key.write("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM.,';: ")

       
        if key.is_pressed("-"):
               exit()
        if key.is_pressed("]"):
                while True:
                        if key.is_pressed("-"):
                                exit()
                        
                        
                        key.write("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM.,';: ")
                        
#