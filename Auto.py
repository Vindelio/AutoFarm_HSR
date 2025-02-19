import pyautogui as pag
import time
import random as rand

# Run comand with local save location: 
# (Dubbelcheck if correct)
# py C:\Users\LAB\Documents\GitHub\AutoFarm_HSR\Auto.py

def Auto():
    time.sleep(1)

    pag.hotkey("win", "down")
    if withStart == 'y':

        # Open Star Rail    
        # ------------------------------------
        pag.click(1450, 840, duration=0.5) # press start button of game
        time.sleep(2)
        
        done = False
        while done == False:     # First opening click 
            pic = pag.screenshot()
            r, g, b = pic.getpixel((1812, 59))
            if r == 252 and g == 252 and b == 252:
                    pag.click(rand.randint(300, 1500), rand.randint(450, 750), duration= 1)
                    done = True
            time.sleep(2)
            
        done = False
        while done == False:     # Second opening click 
            pic = pag.screenshot()
            r, g, b = pic.getpixel((1829, 471))
            if r == 253 and g == 253 and b == 253:
                    pag.click(rand.randint(300, 1500), rand.randint(450, 750), duration= 1)
                    done = True
            time.sleep(2)
        # ------------------------------------


        # Wait for game loading 
        # -------------------------------------
        done = False
        while done == False:     
            pic = pag.screenshot()
            r, g, b = pic.getpixel((1880, 333))
            if r == 11 and g == 9 and b == 6:
                done = True
            time.sleep(2)
        # -------------------------------------
        # You are in game, and can start acting

    match farmType:
        case 1:     # Set peaces
            # opens farm selector
            # ----------------------------------
            pag.hotkey('esc')
            pag.click(rand.randint(1325, 1335), rand.randint(745, 755), duration=1)
            pag.click(rand.randint(465, 475), rand.randint(205, 215), duration=1)
            pag.click(rand.randint(445, 455), rand.randint(845, 855), duration=1)
            pag.click(rand.randint(1545, 1555), rand.randint(345, 355), duration=1)
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
    
    if withClose == 'y':
        time.sleep(1)
        pag.hotkey('alt', 'f4')

try:
    farmType = int(input("Input a farm type \n1 : Set peaces \n2 : Ornaments \n3 : talent mats \n4 : level up mats \n5 : exp \n0 : Do nothing \n"))
    withStart = input("Want to open the game y/n \n")
    withClose = input("Want to close after script y/n \n")

    Auto()
except:
    print("Error or force exit")
    exit()

print("Done Smoothly")
            

        



