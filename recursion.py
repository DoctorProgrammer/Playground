import os


def getStructure(startPath, fileName):
    fileStructureReturn = []

    for root, directories, files in os.walk(startPath):
        for fileData in files:
            # write the path, the name of the file and the size of the file in the file and store each dataset as a list in fileStructureReturn
            fileStructureReturn.append([root + "/" + fileData, getFileName(root + "/" + fileData), os.path.getsize(root + "/" + fileData)])

            with open(fileName, "a") as csvFile:
                csvFile.write(root + "/" + fileData + ";" + getFileName(root + "/" + fileData) + ";" + str(os.path.getsize(root + "/" + fileData)) + "\n")

        for directory in directories:
            # write the path, the name of the directory and the size of the directory in the file and store each dataset as a list in fileStructureReturn
            fileStructureReturn.append([root + "/" + directory, getFileName(root + "/" + directory), os.path.getsize(root + "/" + directory)])

            with open(fileName, "a") as fileData:
                fileData.write(root + "/" + directory + ";" + getFileName(root + "/" + directory) + ";" + str(os.path.getsize(root + "/" + directory)) + "\n")

    return fileStructureReturn


def printFiles(fileName):
    with open(fileName, "r") as fileData:
        for line in fileData:
            # split the line by ";" and use cropToGivenLength to make the output look better
            dataSet = line.strip().split(";")
            print("Path: " + cropToGivenLength(dataSet[0], 100) + "Name: " + cropToGivenLength(dataSet[1], 40) + "Bytes: " + dataSet[2])



def getFileName(string):
    # only return the name of the file
    return string.split("/")[-1]


def cropToGivenLength(string, length):
    # only return the path of the file but not the name
    if len(string) < length:
        return string + " " * (length - len(string))
    else:
        return string[:length - 5] + "...  "


def emptyFile(fileName):
    fileData = open(fileName, "w")
    fileData.write("")
    fileData.close()


def sortStructure(dataset, index):
    # shakersort algorithm for a list (structure) of lists. The index is the index of the value that should be sorted
    left = 0
    right = len(dataset) - 1
    while left <= right:
        for i in range(right, left, -1):
            if dataset[i][index] < dataset[i - 1][index]:
                dataset[i], dataset[i - 1] = dataset[i - 1], dataset[i]
        left += 1

        for i in range(left, right):
            if dataset[i][index] > dataset[i + 1][index]:
                dataset[i], dataset[i + 1] = dataset[i + 1], dataset[i]
        right -= 1

    return dataset


def filterStructure(ending, dataset):
    # filter the structure by the given ending
    filteredDataset = []
    for data in dataset:
        if data[0].endswith(ending):
            filteredDataset.append(data)

    return filteredDataset


def writeStructure(dataset, fileName):
    # write the sorted structure in the file
    emptyFile(fileName)
    for data in dataset:
        with open(fileName, "a") as fileData:
            fileData.writelines(data[0] + ";" + data[1] + ";" + str(data[2]) + "\n")


if __name__ == '__main__':
    path = "C:/Programming/PYTHON-projects"
    file = "dateiStruktur.csv"

    emptyFile(file)

    structure = getStructure(path, file)

    sortedStructure = sortStructure(structure, 2)

    filteredStructure = filterStructure(".py", sortedStructure)

    writeStructure(filteredStructure, file)

    printFiles(file)
