import pyautogui as pag
import time
import random as rand

# Run comand with local save location: 
# (Dubbelcheck if correct)
# py C:\Users\LAB\Documents\GitHub\AutoFarm_HSR\Auto.py

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

def Auto():
    wait(1)
    pag.hotkey("win", "down")
    if withStart == 'y':

        # Open Star Rail    
        # ------------------------------------
        click(1450, 840, 1) # press start button of game
        wait(2)

        waitForPixel(1812, 59, 252, 252, 252)
        click(rand.randint(300, 1500), rand.randint(450, 750), 1) # first opening click
        
        waitForPixel(1829, 471, 253, 253, 253)
        click(rand.randint(300, 1500), rand.randint(450, 750), 1) # Second opening click 
        # ------------------------------------


        # Wait for game loading 
        # -------------------------------------
        waitForPixel(1880, 333, 11, 9, 6)
        # -------------------------------------
        # You are in game, and can start acting


    match farmType:
        case 1:     # Set peaces
            # opens farm selector
            # ----------------------------------
            press('esc')
            click(1330, 750, 1)
            click(470, 210, 1)
            click(450, 850, 1)
            click(1550, 350, 1)
            # ----------------------------------


            # start combat and auto fight 
            # -----------------------------------
            # pag.click(rand.randint(1645, 1655), rand.randint(975, 985), duration=1.5)
            # time.sleep(1.5)
            # pag.click()
            # time.sleep(5)
            # pag.click(rand.randint(1755, 1765), rand.randint(45, 55), duration=5)
            # ------------------------------------


            # click play again
            # ------------------------------------
            # for i in range(4):
            #     time.sleep(150)
            #     pag.click(rand.randint(1195, 1205), rand.randint(945, 955), duration=0.5)
            # ------------------------------------
            

        case 2:     # Ornaments
            pag.hotkey('c')
            print("work in progress")

        case 3:
            pag.hotkey('c')
            print("work in progress")

        case 4:
            pag.hotkey('c')
            print("work in progress")

        case 5:
            pag.hotkey('c')
            print("work in progress")

        case 0:
            print("Nothing was done")

    if grabDaily == 'y':
        # Grab assignments
        # ------------------------------------
        press('esc')
        click(1730, 350, 1)
        click(470, 910, 2)
        click(1200, 950, 1)
        wait(2)
        press('esc')
        # ------------------------------------


        # Grab interastrial guide daily reward
        # ------------------------------------
        click(1330, 750, 1)
        done = False
        while done == False:
            pic = pag.screenshot()
            r, g, b = pic.getpixel((356, 844))
            if r != 209:
                done = True
            else:
                click(420, 830, 0.2)
            wait(2)
        click(1610, 310, 0.5)
        click(1610, 310, 1)
        press('esc')
        # ------------------------------------


        # Grab Nameless Honor daily reward
        click(1470, 610, 1)

        # 356, 844, 209
        # ------------------------------------
        print("work in progress")
    
    if withClose == 'y':
        time.sleep(1)
        pag.hotkey('alt', 'f4')

try:
    farmType = int(input("Input a farm type \n1 : Set peaces \n2 : Ornaments \n3 : talent mats \n4 : level up mats \n5 : exp \n0 : Do nothing \n"))
    withStart = input("Want to open the game y/n \n")
    grabDaily = input("Want to grab daily rewards y/n \n")
    withClose = input("Want to close after script y/n \n")
    
    Auto()
except:
    print("Error or force exit")
    exit()

print("Done Smoothly")
            

        



