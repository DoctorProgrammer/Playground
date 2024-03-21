from datetime import datetime


class Algorithm:
    def __init__(self, name, data_small, data_medium, data_big):
        self.name = name
        self.data_small = data_small
        self.data_medium = data_medium
        self.data_big = data_big

    def sort_all(self, column):
        self.sort(self.data_small, column, "small")
        self.sort(self.data_medium, column, "medium")
        self.sort(self.data_big, column, "big")

    def sort(self, data, column, size):
        index = self.get_column_index(column)
        start = datetime.now()
        self.algorithm(data, index)
        end = datetime.now()
        time_taken = (end - start).total_seconds()
        print(f"{self.name} - {size}: {time_taken} s")

    @staticmethod
    def get_column_index(column):
        columns = {"id": 0, "prename": 1, "name": 2, "street": 3, "zip": 4, "birthdate": 5, "balance": 6}
        return columns.get(column, -1)

    def algorithm(self, data, index):
        pass


class BubbleSort(Algorithm):
    def __init__(self, name, data_small, data_medium, data_big):
        super().__init__(name, data_small, data_medium, data_big)

    def algorithm(self, data, index):
        n = len(data)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if data[j][index] > data[j + 1][index]:
                    data[j], data[j + 1] = data[j + 1], data[j]


class QuickSort(Algorithm):
    def __init__(self, name, data_small, data_medium, data_big):
        super().__init__(name, data_small, data_medium, data_big)

    def algorithm(self, data, index):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2][index]
        left = [x for x in data if x[index] < pivot]
        middle = [x for x in data if x[index] == pivot]
        right = [x for x in data if x[index] > pivot]
        return self.algorithm(left, index) + middle + self.algorithm(right, index)


class HeapSort(Algorithm):
    def __init__(self, name, data_small, data_medium, data_big):
        super().__init__(name, data_small, data_medium, data_big)

    def algorithm(self, data, index):
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
    def __init__(self, name, data_small, data_medium, data_big):
        super().__init__(name, data_small, data_medium, data_big)

    def algorithm(self, data, index):
        left = 0
        right = len(data) - 1
        while left <= right:
            for i in range(left, right):
                if data[i][index] > data[i + 1][index]:
                    data[i], data[i + 1] = data[i + 1], data[i]
            right -= 1
            for i in range(right, left, -1):
                if data[i][index] < data[i - 1][index]:
                    data[i], data[i - 1] = data[i - 1], data[i]
            left += 1


if __name__ == '__main__':
    data_small = []
    data_medium = []
    data_big = []

    with open("./testData/sortSmall.txt", "r") as file:
        for line in file:
            data_small.append(line.strip().split(","))

    with open("./testData/sortMedium.txt", "r") as file:
        for line in file:
            data_medium.append(line.strip().split(","))

    with open("./testData/sortBig.txt", "r") as file:
        for line in file:
            data_big.append(line.strip().split(","))

    heapsort = HeapSort("HeapSort", data_small, data_medium, data_big)
    heapsort.sort_all("id")

    shakersort = ShakerSort("ShakerSort", data_small, data_medium, data_big)
    shakersort.sort_all("id")

    quicksort = QuickSort("QuickSort", data_small, data_medium, data_big)
    quicksort.sort_all("id")

    bubblesort = BubbleSort("BubbleSort", data_small, data_medium, data_big)
    bubblesort.sort_all("id")
