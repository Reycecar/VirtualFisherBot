'''
@Author Reyce Salisbury
3/4/2022
'''

from multiprocessing import Event
from pynput.keyboard import *
import os
import time

keyboard = Controller()

RUNS = 5
COOLDOWN = 2.8
BAIT = "Fish"
BAITNUM = 50
                    

#Types %f (fishing), is interrupted by pressing end
def go_fish():
    for _ in range(RUNS):
        txt = "%f"
        typer(txt)
        time.sleep(COOLDOWN)

#buys BAITNUM of BAIT when end is pressed after program is run
def get_bait():
    txt = "%buy " + BAIT + " " + str(BAITNUM)
    typer(txt)

#called when insert key is pressed after program is run
def sell():
    txt = "%sell all"
    typer(txt)

#function for pressing enter
def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

#Types text to wherever your curser is
def typer(text):
    for i in text:
        keyboard.press(i)
        keyboard.release(i)
        time.sleep(0.1)
    enter()

#Runs funtions based on Key Pressed
def on_press(key):
    if key == Key.num_lock:
        go_fish()
    elif key == Key.insert:
        sell()
    elif key == Key.end:
        get_bait()
    elif key == Key.esc:
        os.system('taskkill /IM "Python.exe" /F')

#Main, Starts the listener
def main():
    with Listener(on_press=on_press, on_release=None) as listener:
        while True:
            listener.run()

if __name__ == "__main__":
    main()
