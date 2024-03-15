def Summendreieck(n):
    if n == 1:
        return 1
    else:
        return n + Summendreieck(n-1)


if __name__ == '__main__':
    print(Summendreieck(5))
