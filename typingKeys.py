import pyautogui as pt
import time


if __name__ == '__main__':
    # a programm that repeats following steps:
    # 1. press F5
    # 2. press ctrl + tab
    # this should be repeated
    time.sleep(5)
    for i in range(100):
        pt.press("F5")
        pt.keyDown("ctrl")
        pt.press("tab")
        pt.keyUp("ctrl")
