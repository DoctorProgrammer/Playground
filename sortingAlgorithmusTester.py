from datetime import datetime
from random import randint


class Algorithm:
    def __init__(self, name, dataSmall, dataMedium, dataBig):
        self.name = name
        self.dataSmall = dataSmall
        self.dataMedium = dataMedium
        self.dataBig = dataBig

    def sortAll(self, column):
        self.sortSmall(column)

        self.sortMedium(column)

        self.sortBig(column)

    def sortSmall(self, column):
        index = self.getColumnIndex(column)
        start = datetime.now().strftime("%S.%f")
        self.sort(self.dataSmall, index)
        end = datetime.now().strftime("%S.%f")
        time = float(end) - float(start)
        print(self.name + " - small: " + str(time) + "s")

    def sortMedium(self, column):
        index = self.getColumnIndex(column)
        start = datetime.now().strftime("%S.%f")
        self.sort(self.dataMedium, index)
        end = datetime.now().strftime("%S.%f")
        time = float(end) - float(start)
        print(self.name + " - medium: " + str(time) + "s")

    def sortBig(self, column):
        index = self.getColumnIndex(column)
        start = datetime.now().strftime("%S.%f")
        self.sort(self.dataBig, index)
        end = datetime.now().strftime("%S.%f")
        time = float(end) - float(start)
        print(self.name + " - big: " + str(time) + "s")

    @staticmethod
    def getColumnIndex(column):
        if column == "id":
            return 0
        if column == "prename":
            return 1
        if column == "name":
            return 2
        if column == "street":
            return 3
        if column == "zip":
            return 4
        if column == "birthdate":
            return 5
        if column == "balance":
            return 6
        else:
            print("Column not found!")
            return -1

    def sort(self, data, index):
        pass


class BubbleSort(Algorithm):
    def __init__(self, name, dataSmall, dataMedium, dataBig):
        super().__init__(name, dataSmall, dataMedium, dataBig)

    def sort(self, data, index):
        n = len(data)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if data[j][index] > data[j + 1][index]:
                    data[j], data[j + 1] = data[j + 1], data[j]


class QuickSort(Algorithm):
    def __init__(self, name, dataSmall, dataMedium, dataBig):
        super().__init__(name, dataSmall, dataMedium, dataBig)

    def sort(self, data, index):
        for i in range(len(data)):
            pivot = (data[i][index])
            left = []
            right = []
            equal = []

            for element in data:
                if element[index] < pivot:
                    left.append(element)
                elif element[index] > pivot:
                    right.append(element)
                elif element[index] == pivot:
                    equal.append(element)
                data = left + equal + right
            return data


class HeapSort(Algorithm):
    def __init__(self, name, dataSmall, dataMedium, dataBig):
        super().__init__(name, dataSmall, dataMedium, dataBig)

    def sort(self, data, index):
        def heapify(data, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and data[left][index] > data[largest][index]:
                largest = left

            if right < n and data[right][index] > data[largest][index]:
                largest = right

            if largest != i:
                data[i], data[largest] = data[largest], data[i]
                heapify(data, n, largest)

        n = len(data)

        for i in range(n // 2 - 1, -1, -1):
            heapify(data, n, i)

        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            heapify(data, i, 0)


class ShakerSort(Algorithm):
    def __init__(self, name, dataSmall, dataMedium, dataBig):
        super().__init__(name, dataSmall, dataMedium, dataBig)

    def sort(self, data, index):
        left = 0
        right = len(data) - 1
        swapped = True

        while swapped:
            swapped = False

            # von links nach rechts sortieren
            for i in range(left, right):
                if data[i][index] > data[i + 1][index]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    swapped = True

            if not swapped:
                break

            swapped = False
            right -= 1

            # von rechts nach links sortieren
            for i in range(right, left, -1):
                if data[i][index] < data[i - 1][index]:
                    data[i], data[i - 1] = data[i - 1], data[i]
                    swapped = True

            left += 1


if __name__ == '__main__':
    # test data is in ./testData
    # ./testData/sortBig.txt
    # ./testData/sortMedium.txt
    # ./testData/sortSmall.txt
    dataS = []
    dataM = []
    dataB = []

    with open("./testData/sortSmall.txt", "r") as file:
        for line in file:
            # split line by comma and delete "\n" at the end
            dataSet = line.split(",")
            dataSet[-1] = dataSet[-1].replace("\n", "")
            dataS.append(dataSet)

    with open("./testData/sortMedium.txt", "r") as file:
        for line in file:
            dataSet = line.split(",")
            dataSet[-1] = dataSet[-1].replace("\n", "")
            dataM.append(dataSet)

    with open("./testData/sortBig.txt", "r") as file:
        for line in file:
            dataSet = line.split(",")
            dataSet[-1] = dataSet[-1].replace("\n", "")
            dataB.append(dataSet)

    heapsort = HeapSort("HeapSort", dataS, dataM, dataB)
    # heapsort.sortAll("prename")

    shakersort = ShakerSort("ShakerSort", dataS, dataM, dataB)
    # shakersort.sortAll("prename")

    quicksort = QuickSort("QuickSort", dataS, dataM, dataB)
    # quicksort.sortAll("prename")

    bubblesort = BubbleSort("BubbleSort", dataS, dataM, dataB)
    # bubblesort.sortAll("prename")  # possibilities: id, prename, name, street, zip, birthdate, balance

    heapsort.sortSmall("prename")
    shakersort.sortSmall("prename")
    quicksort.sortSmall("prename")
    bubblesort.sortSmall("prename")

    heapsort.sortMedium("prename")
    shakersort.sortMedium("prename")
    quicksort.sortMedium("prename")
    bubblesort.sortMedium("prename")

    heapsort.sortBig("prename")
    shakersort.sortBig("prename")
    quicksort.sortBig("prename")
    bubblesort.sortBig("prename")
