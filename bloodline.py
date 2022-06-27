import pyautogui
import time

badRolls = ["crystal.png", "explosion.png", "ice.png", "mud.png", "nature.png", "steam.png"]

def compare():
    for i in badRolls:
        coords = pyautogui.locateCenterOnScreen(i)
        if coords != None:
            spin()

def spin():
    pyautogui.click(1246, 363)
    time.sleep(18)
    compare()

time.sleep(4)
spin()