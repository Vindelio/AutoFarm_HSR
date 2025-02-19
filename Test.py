import pyautogui as pag
import time
import random as rand

# py C:\Users\LAB\Documents\Projects\python\Auto\Test.py

for i in range(20):
    pic = pag.screenshot()

    r1, g1, b1 = pic.getpixel((1812, 59))
    print(r1, g1, b1)

    if r1 == 252 and g1 == 252 and b1 == 252:
        print("first time to click")

    r2, g2, b2 = pic.getpixel((1829, 471))
    print(r2, g2, b2)

    if r2 == 253 and g2 == 253 and b2 == 253:
        print("second time to click")

    time.sleep(2)






