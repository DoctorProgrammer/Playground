import os
from datetime import datetime

if __name__ == '__main__':
    logfile = open("C:/Programming/PYTHON-projects/Playground/logfiles/logfile1", "a")

    while True:
        now = datetime.now()
        logfile.write(f'[{now}] : logeintrag' + "\n")










