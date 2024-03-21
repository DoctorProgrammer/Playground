import time
from os import system, name


def bruteforceString(endString):
    output = ""
    for letter in endString:
        for i in range(32, 127):
            output += chr(i)
            # clear the console
            clear()
            print(output)
            if letter == chr(i):
                break
            else:
                output = output[:-1]

            time.sleep(0.01)


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == "__main__":
    finalString = "Hallo. Das ist eine Nachricht, welche noch zuerst per Brute Force Methode entschlüsselt werden muss."
    bruteforceString(finalString)
