import pyautogui as pug
import time


def activate_hotspot():     # works only on 1920x1080 res TODO: using .size() make it relative
    pug.moveTo(1880, 1079)
    time.sleep(2)
    pug.moveTo(1880, 1050)
    pug.click()
    pug.moveTo(1880, 850)
    time.sleep(2)
    pug.click()
    pug.moveTo(960, 539)
