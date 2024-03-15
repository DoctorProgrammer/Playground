def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def sigma(k, n, function=lambda x: x):
    result = 0.0
    while k <= n:
        result += function(k)
        k += 1
    return result


def sin(x: float, precision=85):
    if precision > 85:
        print("Precision is too high, setting to 85")
        precision = 85
    return round(sigma(1, precision, lambda i: ((-1) ** (i - 1)) * (x ** (2 * i - 1)) / factorial(2 * i - 1)), 15)


def radians(degrees: float):
    return degrees / 180 * 3.141592653589793


if __name__ == '__main__':
    # 85 is the maximum precision
    print(sin(radians(180), 85))  # resultat = 3.3280566969799443e-16 (weil nicht 100% genau; 0.0)
    print(sin(radians(90), 85))  # resultat = 1.0
    print(sin(radians(22), 85))  # resultat = 0.374606593415912
    print(sin(radians(22), 1))  # resultat = 0.383972435438752

    print(sigma(1, 10, lambda x: x ** 2))
