import pyautogui as pag
import time
import random as rand

# open hoyo launcher, then admin cmd and use: py C:\Users\LAB\Documents\Projects\python\Auto\Auto.py

def Auto():
    time.sleep(1)

    pag.hotkey("win", "down")
    if withStart == 'y':
        # opens Star Rail    
        pag.click(1450, 840, duration=0.5) # press start button of game
        time.sleep(2)
        
        clicked = False
        while clicked == False:     # First opening click 
            pic = pag.screenshot()
            r, g, b = pic.getpixel((1812, 59))
            if r == 252 and g == 252 and b == 252:
                    pag.click(rand.randint(300, 1500), rand.randint(450, 750), duration= 1)
                    clicked = True
            time.sleep(2)
            
        clicked = False
        while clicked == False:     # Second opening click 
            pic = pag.screenshot()
            r, g, b = pic.getpixel((1829, 471))
            if r == 253 and g == 253 and b == 253:
                    pag.click(rand.randint(300, 1500), rand.randint(450, 750), duration= 1)
                    clicked = True
            time.sleep(2)

    # time.sleep(10)

    # # opens farm selector
    # pag.hotkey('esc')
    # pag.click(rand.randint(1325, 1335), rand.randint(745, 755), duration=1)
    # pag.click(rand.randint(465, 475), rand.randint(205, 215), duration=1)

    # match farmType:
    #     case 1:     # Set peaces
    #         # start combat and auto fight
    #         pag.click(rand.randint(445, 455), rand.randint(845, 855), duration=1.5)
    #         pag.click(rand.randint(1545, 1555), rand.randint(345, 355), duration=1.5)
    #         pag.click(rand.randint(1645, 1655), rand.randint(975, 985), duration=1.5)
    #         time.sleep(1.5)
    #         pag.click()
    #         time.sleep(5)
    #         pag.click(rand.randint(1755, 1765), rand.randint(45, 55), duration=5)
            
    #         # click play again
    #         for i in range(4):
    #             time.sleep(150)
    #             pag.click(rand.randint(1195, 1205), rand.randint(945, 955), duration=0.5)
            
    #     case 2:     # Ornaments
    #         pag.hotkey('c')

    #         print("work in progress")

    #     case 3:
    #         pag.hotkey('c')
    #         print("work in progress")

    #     case 4:
    #         pag.hotkey('c')
    #         print("work in progress")

    #     case 5:
    #         pag.hotkey('c')
    #         print("work in progress")
    
    # if withClose == 'y':
    #     time.sleep(1)
    #     pag.hotkey('alt', 'f4')

try:
    farmType = int(input("Input a farm type \n1 : Set peaces \n2 : Ornaments \n3 : talent mats \n4 : level up mats \n5 : exp \n"))
    withStart = input("Want to open the game y/n \n")
    withClose = input("Want to close after script y/n \n")

    Auto()
except:
    print("Error or force exit")
    exit()

print("Done Smoothly")
            

        



