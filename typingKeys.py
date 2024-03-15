import pyautogui as pt
import time


def Type(text: str):
    for i in text:
        pt.keyDown(i)
        pt.keyUp(i)


if __name__ == '__main__':
    time.sleep(5)
    Type("Hallo Welt Hallo Welt Hallo Welt Hallo Welt Hallo Welt Hallo Welt Hallo Welt Hallo Welt ")
# Ein Programm, dass mir cmd öffnet und dann das Fenster von cmd dauerhaft an einen zufälligen Ort bewegt.

