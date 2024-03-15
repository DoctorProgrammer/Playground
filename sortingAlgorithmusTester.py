from datetime import datetime
import threading


class Algorithm:
    def __init__(self, name):
        self.name = name

    def test(self, data):
        pass

    def sort(self, data):
        pass


class BubbleSort(Algorithm):
    def __init__(self, name):
        super().__init__(name)

    def test(self, data):
        # startTime in microseconds
        startTime = datetime.now().strftime("%H:%M:%S.%f")
        thread = threading.Thread(target=self.sort, args=(data,))
        thread.start()
        listResult = thread.join()

        endTime = datetime.now().strftime("%H:%M:%S.%f")
        startTime = float(startTime.split(":")[2])
        endTime = float(endTime.split(":")[2])
        print(f"Start: {startTime}\tEnd: {endTime}")
        return {
            "algorithm": "BubbleSort",
            "result": listResult[0],
            "time": endTime - startTime,
            "iterations": listResult[1]
        }

    def sort(self, data):
        iterations = 0
        swaps = 0
        for i in range(len(data) - 1):
            for j in range(len(data) - 1):
                iterations += 1
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swaps += 1
        sortedList = [data, iterations]
        return sortedList


if __name__ == '__main__':
    zahlenreihe = [12, 3, 0, 18, 22, 44]
    bubbleSort = BubbleSort("BubbleSort")
    result = bubbleSort.test(zahlenreihe)

    print(f"Name: {result['algorithm']}\tResult: {result['result']}\tTime: {result['time']}\tIterations: {result['iterations']}")
