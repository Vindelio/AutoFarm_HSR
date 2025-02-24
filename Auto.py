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


def drag(x, y, dur, press):
    pag.dragTo(x, y, dur, button=press)


def Open():
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


def TeamSelect():       # Make sure the farming team is at team 7, and the strongest support character is at the top of the list
    # Select farm team
    # ----------------------------------
    click(1290, 70, 1)  # Select team 7

    click(1720, 730, 1) # Select suport character
    click(1650, 980, 1)
    # ----------------------------------


def Combat():
    # start combat and auto fight 
    # -----------------------------------
    click(1650, 980, 1)
    waitForPixel(318, 972, 50, 255, 248)    # checks if healthbar 1 is on screen, to check if combat is started
    
    pic = pag.screenshot()      # Checks if autoplay is on
    r, g, b = pic.getpixel((1761, 63))
    if r != 241:
        click(1760, 50, 1)
    # -----------------------------------


    # press play again and exit
    # -----------------------------------
    empty = False
    while empty == False:
        waitForPixel(1053, 944, 255, 255, 248)      # Play again
        click(1053, 944, 1)
        wait(2)
        pic = pag.screenshot()      # Checks if still have energy
        r, g, b = pic.getpixel((710, 730))
        if r == 12 and g == 11 and b == 7:
            empty = True
        
    click(830, 730, 2)      # Exit the combat
    click(770, 940, 1)
    # ------------------------------------


def Farm(farmType):
    match farmType:
        case 1:     # Set peaces

            # Opens set peace farming
            # ----------------------------------
            press('esc')
            click(1730, 620, 1)
            click(470, 210, 1)
            click(450, 850, 1)
            click(1550, 350, 1)
            click(1650, 980, 1)
            # ----------------------------------

            # Selects farm team and sup character
            # ----------------------------------
            TeamSelect()
            # ----------------------------------

            # Start, replay, and exit combat
            # ----------------------------------
            Combat()
            # ----------------------------------
            wait(2)
            press('esc')
            wait(2)
            press('esc')


        case 2:     # Ornaments

            press('c')
            wait(1)
            click(1560, 65, 1)
            print("work in progress")


        case 3:     # Talent mats

            # Navigate and click into talent mat farming
            # ----------------------------------
            press('c')
            wait(1)
            click(1560, 65, 1)
            click(980, 500, 1)      
            pag.moveTo(1490, 440, duration=1)
            pag.dragTo(1490, 900, 1)
            click(1050, 570, 1)
            wait(1)
            for i in range(5):      # Choose 6 rounds
                click(1850, 900, 0.5)
            click(1620, 980, 1)
            # ----------------------------------

            # Selects farm team and sup character
            # ----------------------------------
            TeamSelect()
            # ----------------------------------

            # Start, replay, and exit combat
            # ----------------------------------
            Combat()
            # ----------------------------------
            wait(2)
            press('esc')


        case 4:     # Level up mats
            # Navigate and click into level mats
            # ----------------------------------
            press('c')
            wait(1)
            click(1560, 65, 1)
            click(960, 790, 1)
            click(1860, 250, 1)
            click(580, 520, 1)
            click(800, 530, 1)
            wait(1)
            for i in range(5):
                pag.scroll(-1000)
                wait(0.2)
            click(1080, 640, 1)
            click(1600, 980, 1)
            # ----------------------------------

            # Selects farm team and sup character
            # ----------------------------------
            TeamSelect()
            # ----------------------------------

            # Start, replay, and exit combat
            # ----------------------------------
            Combat()
            # ----------------------------------
            wait(2)
            press('esc')


        case 5:     # Exp
            # Navigate and click into exp farming
            # ----------------------------------
            press('c')
            wait(1)
            click(1560, 65, 1)
            click(980, 430, 1)      
            pag.moveTo(1490, 440, duration=1)
            pag.dragTo(1490, 900, 1)
            click(1100, 630, 1)
            wait(1)
            for i in range(5):      # Choose 6 rounds
                click(1850, 900, 0.5)
            click(1620, 980, 1)
            # ----------------------------------
            
            # Selects farm team and sup character
            # ----------------------------------
            TeamSelect()
            # ----------------------------------

            # Start, replay, and exit combat
            # ----------------------------------
            Combat()
            # ----------------------------------
            wait(2)
            press('esc')
            


def Daily():
    wait(1)
    press('esc')
    # Grab assignments
    # ------------------------------------
    click(1730, 350, 1)
    click(470, 910, 2)
    click(1200, 970, 2)
    wait(2)
    press('esc')
    wait(1)
    press('esc')
    # ------------------------------------


    # Grab interastrial guide daily reward
    # ------------------------------------
    wait(1)
    pag.keyDown('tab')
    click(1200, 330, 0.5)
    pag.keyUp('tab')
    click(380, 210, 1)
    for i in range(4):
        click(420, 830, 0.5)
    wait(2)
    click(1610, 310, 1)
    click(1610, 310, 2)
    wait(0.5)
    press('esc')
    # ------------------------------------


    # Grab Nameless Honor daily reward
    # ------------------------------------      # Not currently available
    # click(1470, 610, 1)
    # click(960, 70, 1)
    # click(1670, 920, 1)
    # click(860, 70, 3)
    # click(1440, 910, 1)
    # click(1440, 910, 1)
    # press('esc')
    # wait(0.5)
    # press('esc')
    # ------------------------------------


def Auto():
    wait(1)
    pag.hotkey("win", "down")
    wait(1)

    if withStart == 'y':
        Open()
        wait(1)

    if farmType != 0:
        Farm(farmType)
        wait(1)
    
    if grabDaily == 'y':
        Daily()
        wait(1)
    
    if withClose == 'y':
        wait(1)
        pag.hotkey('alt', 'f4')


farmType = int(input("Input a farm type \n1 : Set peaces \n2 : Ornaments \n3 : talent mats \n4 : level up mats \n5 : exp \n0 : Do nothing \n"))
withStart = input("Want to open the game y/n \n")
grabDaily = input("Want to grab daily rewards y/n \n")
withClose = input("Want to close after script y/n \n")

Auto()
print("Done Smoothly")
            

        



