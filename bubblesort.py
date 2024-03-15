import os

os.system("cls")


def bubbleSortWhileFor(row):
    whileIterations = 0
    iterations = 0
    swaps = 0
    unsorted = True
    while unsorted:
        whileIterations += 1
        print(f"\u001b[48;1m\u001b[33;1mIterations (while): \u001b[37;1m{whileIterations}")
        unsorted = False
        for i in range(len(row) - 1):
            iterations += 1
            print(f"\u001b[34;1m\tIterations (for): \u001b[37;1m{iterations}\u001b[34;1m\tSwaps: \u001b[37;1m{swaps}\t" + str(row))
            if row[i] > row[i + 1]:
                row[i], row[i + 1] = row[i + 1], row[i]
                swaps += 1
                unsorted = True
    return row


def bubbleSortForFor(row):
    iterations = 0
    swaps = 0
    for i in range(len(row) - 1):
        for j in range(len(row) - 1):
            iterations += 1
            print(f"\u001b[48;1m\u001b[34;1m\tIterations (for): \u001b[37;1m{iterations}\u001b[34;1m\tSwaps: \u001b[37;1m{swaps}\t" + str(row))
            if row[j] > row[j + 1]:
                row[j], row[j + 1] = row[j + 1], row[j]
                swaps += 1
    return row


if __name__ == '__main__':
    zahlenreihe = [12, 3, 0, 18, 22, 44]
    print("\u001b[40;1m\u001b[39;1mResult: \t" + str(bubbleSortForFor(zahlenreihe)))
    zahlenreihe = [12, 3, 0, 18, 22, 44]
    print("\u001b[40;1m\u001b[39;1mResult: \t" + str(bubbleSortWhileFor(zahlenreihe)))
