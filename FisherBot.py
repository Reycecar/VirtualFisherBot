'''
@Author Reyce Salisbury
3/4/2022
'''

from pynput.keyboard import Controller, Key, Listener
import os
import time
keyboard = Controller()

RUNS = 50
COOLDOWN = 2.7
BAIT = "Fish"
BAITNUM = 50
RODS = ["Plastic", "Improved", "Steel", "Fiberglass", "Heavy", "Alloy", "Lava", "Magma"]
ROD_CURR = "Heavy"

def go_fish():
    for i in range(RUNS):
        txt = "%f"
        for i in txt:
            keyboard.press(i)
            keyboard.release(i)
            time.sleep(0.1)
        enter()
        time.sleep(COOLDOWN)

def get_bait():
    txt = "%buy " + BAIT + " " + BAITNUM
    for i in txt:
        keyboard.press(i)
        keyboard.release(i)
        time.sleep(0.1)
    enter()
    time.sleep(COOLDOWN)

def rod_up():
    #Changes Current rod to the next best rod
    return

def rod_down():
    #Changes Current rod to the next rod down
    
    return

def sell():
    txt = "%sell all"
    for i in txt:
        keyboard.press(i)
        keyboard.release(i)
        time.sleep(0.1)
    time.sleep(COOLDOWN)
    enter()
    
def end():
    end_txt = "%sell all"
    for i in end_txt:
        keyboard.press(i)
        keyboard.release(i)
        time.sleep(0.1)
    enter()
    os.system('taskkill /IM "Python.exe" /F')

def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def on_press(key):
    if key == Key.num_lock:
        go_fish()
    elif key == Key.insert:
        sell()
    elif key == Key.end:
        get_bait()
    elif key == Key.esc:
        end()
    
with Listener(on_press=on_press, on_release=None) as listener:
        listener.run()