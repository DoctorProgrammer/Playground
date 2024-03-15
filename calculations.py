"""
import sys

sys.setrecursionlimit(none)
"""


def add(addend1: float, addend2: float):
    return addend1 + addend2


def sub(minuend: float, subtrahend: float):
    return minuend - subtrahend


def mul(factor1: float, factor2: float):
    return factor1 * factor2


def div(dividend: float, divisor: float):
    return dividend / divisor


def pow(base: float, exponent: float):
    return base ** exponent


def root(number: float, dimension=2.0):
    return number ** (1 / dimension)


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
    print(add(5, 2))

    print(sub(5, 2))

    print(mul(5, 2))

    print(div(5, 2))

    print(pow(5, 2))

    print(root(25))
    print(root(27, 3))

    print(factorial(5))

    print(sigma(1, 10))
    print(sigma(1, 10, lambda x: x ** 2))
    print(sigma(1, 10, lambda n: (-1) ** n))

    print(sin(radians(90)))
    print(sin(radians(90), 85))

    print(radians(180))  # resultat = 3.141592653589793 = pi
    print(radians(90))  # resultat = 1.5707963267948966 = pi/2
