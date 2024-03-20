import time


def sort(data, index):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(data)):
            if data[i - 1][index] > data[i][index]:
                data[i - 1][index], data[i][index] = data[i][index], data[i - 1][index]
                swapped = True


if __name__ == '__main__':
    dataM = []

    with open("./testData/sortMedium.txt", "r") as file:
        for line in file:
            dataSet = line.split(",")
            dataSet[-1] = dataSet[-1].replace("\n", "")
            dataM.append(dataSet)

    start = time.time()
    sort(dataM, 1)
    end = time.time()
    print(end - start)
