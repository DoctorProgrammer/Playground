import pyautogui as pt
import keyboard
import random


def MoveWindow():
    x = random.randint(0, 1920)
    y = random.randint(0, 1080)
    pt.moveTo(x, y, 0)
    pt.mouseDown()
    pt.mouseDown()
    pt.mouseUp()


if __name__ == '__main__':
    while True:
        if input("Press enter to start") == "":
            MoveWindow()
            MoveWindow()
            MoveWindow()
            MoveWindow()
            MoveWindow()
            MoveWindow()
        if keyboard.is_pressed("esc"):
            break
    MoveWindow()
    print("Programm beendet")
