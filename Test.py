import pyautogui as pag
import time
import random as rand

# Run comand with local save location: 
# (Dubbelcheck if correct)
# py C:\Users\LAB\Documents\GitHub\AutoFarm_HSR\Test.py

def wait(num):
    time.sleep(num)

def waitForPixel(x, y, rc, gc, bc) :     # xy cords of pixel checked, rgb value to check for
    done = False
    while done == False:
        pic = pag.screenshot()
        r, g, b = pic.getpixel((x, y))
        if r == rc and g == gc and b == bc:
                done = True
        wait(2)

def ca(num):
    return rand.randint(num-5, num+5)

def click(x, y, dur):
    if x == None and y == None and dur == None:
        pag.click()
    else:
        pag.click(ca(x), ca(y), duration=dur)

def press(button):
    pag.hotkey(button)

def drag(x, y, dur, press):
    pag.dragTo(x, y, dur, button=press)

wait(1)
pag.hotkey("win", "down")
wait(1)
press('esc')

# Test stuff beneath here









