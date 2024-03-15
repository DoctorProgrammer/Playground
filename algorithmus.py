i = 0
max = 100000
primZahlen = []

for i in range(0, max):
    primZahlen.append(True)

for i in range(1, max):
    if primZahlen[i]:
        for j in range(i + 1, max):
            if (j + 1) % (i + 1) == 0:
                primZahlen[j] = False

for i in range(1, max):
    if primZahlen[i]:
        print(i + 1)
