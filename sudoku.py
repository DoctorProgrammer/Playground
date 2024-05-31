import time
import pyautogui as pt


def printInConsole(field):
    print("┌──────────┬──────────┬──────────┐")
    for i in range(9):
        for j in range(9):
            if j % 3 == 0:
                print("│", end=" ")
            print(" " + str(field[i][j]) + " ", end="")
            if j == 8:
                print("│")
        if i % 3 == 2 and i != 8:
            print("├──────────┼──────────┼──────────┤")
    print("└──────────┴──────────┴──────────┘")


def fillSudoku(field):
    numbers = [(766, 1900),
               (906, 1900),
               (1063, 1900),
               (1234, 1900),
               (1373, 1900),
               (1544, 1900),
               (1685, 1900),
               (1844, 1900),
               (1989, 1900), ]
    sudokuColumnXCoodinates = [759, 913, 1059, 1219, 1377, 1530, 1693, 1838, 1996]
    sudokuRowYCoodinates = [442, 598, 742, 911, 1059, 1211, 1370, 1524, 1679]

    lastField = ()
    for i in range(9):
        for j in range(9):
            if lastField != numbers[field[i][j] - 1]:
                pt.click(numbers[field[i][j] - 1])
                lastField = numbers[field[i][j] - 1]
            pt.click(sudokuColumnXCoodinates[j], sudokuRowYCoodinates[i])


def solve(list):
    empty = findEmpty(list)
    if not empty:
        return True
    row, col = empty
    for i in range(1, 10):
        if isValid(list, row, col, i):
            list[row][col] = i
            if solve(list):
                return True
            list[row][col] = 0
    return False


def findEmpty(list):
    for i in range(9):
        for j in range(9):
            if list[i][j] == 0:
                return i, j
    return None


def isValid(list, row, col, num):
    for i in range(9):
        if list[row][i] == num:
            return False
        if list[i][col] == num:
            return False
        if list[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False
    return True


def askSudoku(list):
    string: str = input(
        "Enter the Sudoku: ")
    for i in range(9):
        for j in range(9):
            list[i][j] = int(string[i * 9 + j])
    return list


if __name__ == '__main__':
    sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    sudoku = askSudoku(sudoku)

    printInConsole(sudoku)

    solve(sudoku)

    printInConsole(sudoku)

    enter = input("Press enter to start filling the Sudoku. You will have 5 seconds to switch to the Sudoku window.")
    time.sleep(5)

    fillSudoku(sudoku)
