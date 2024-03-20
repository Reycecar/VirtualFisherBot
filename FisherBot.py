'''
@Author Reyce Salisbury
12/29/2023

TODO:
Fix other commands outside of go_fish_click()
Add multiprocessing or multithreading to detect multiple user inputs
    - might work by adding second controller??
    - Thread Queue?

'''

from multiprocessing import Event
import pynput
import os
import time
import random

keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()

RUNS = 1000000
COOLDOWN = 3
BAIT = "Magic Bait"
BAITNUM = 50

#Types %f (fishing)
def go_fish_type():
    for _ in range(RUNS):
        txt = "%f"
        typer(txt)
        # Sleep for cooldown time, but subtract the time it takes to type
        time.sleep(COOLDOWN - (len(txt)*.1))

# Clicks Fishing button, avoids captcha failure clause
def go_fish_click():
    while True:
        clicker()
        # Add variance (up to 1 second) in time between clicks, helps avoid captcha detection
        time.sleep(COOLDOWN + round(random.random(), 1) + 1.5) # Add buffer time to cooldown timer to counteract lag

# **BROKEN BY UPDATE** called when insert key is pressed after program is run
def sell():
    txt = "/sell all"
    typer(txt)

# Function for pressing enter
def enter():
    keyboard.press(pynput.keyboard.Key.enter)
    keyboard.release(pynput.keyboard.Key.enter)

# Types text to wherever your curser is
def typer(text):
    for i in text:
        keyboard.press(i)
        keyboard.release(i)
        time.sleep(0.1)
    enter()

# User must hover mouse over button
def clicker():
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)

#Runs funtions based on Key Pressed
def on_press(key):
    if key == pynput.keyboard.Key.alt_l:  # clicker fishing
        go_fish_click()
    elif key == pynput.keyboard.Key.esc:
        os.system('taskkill /IM "Python.exe" /F')

#Main, Starts the listener
def main():
    with pynput.keyboard.Listener(on_press=on_press, on_release=None) as listener:
        while True:
            listener.run()

if __name__ == "__main__":
    main()