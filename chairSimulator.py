import pyautogui as pg


def Type(text: str):
    for i in text:
        pg.keyDown(i)
        pg.keyUp(i)


def PictureVisible(path: str):
    if pg.locateOnScreen(path, confidence=0.7) is not None:
        # drücke taste "e"
        pg.keyDown("e")
        pg.keyUp("e")
        pg.sleep(2)
        pg.keyDown("e")
        pg.keyUp("e")
        return "ChairSimulator is visible"
    else:
        return "ChairSimulator is not visible"


if __name__ == '__main__':
    while True:
        print(PictureVisible("pictures/chairSimulator.png"))
