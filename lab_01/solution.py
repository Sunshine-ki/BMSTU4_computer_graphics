from define import *
from math import fabs


def find_coefficients(a, b):
    # Проверка на прямую,парал. оси у
    try:
        k = (a[1] - b[1]) / (a[0] - b[0])
        b = a[1] - (a[0] * k)
    except ZeroDivisionError:
        return inf, inf
    # print(a[0], "- ( ",a[1], "*", k, ")" )
    return k, b


def perpendicular_lines(k1):
    # Перпендикулярность прямых к1*к2=-1.
    return -1 / k1


def find_coefficients_b(a, k):
    return a[1] - (a[0] * k)


# Точка пересечения прямых a и b.
def find_intersection_point(a, b):
    # print("-1 * (", a[1], "-", b[1],") / (", a[0], "-", b[0], ")")
    x = -1 * (a[1] - b[1]) / (a[0] - b[0])
    # print(a[0], "*", x, "+", a[1])
    y = a[0] * x + a[1]
    return x, y


def distance(a):
    # print("Точка: ", a)
    return fabs(a[0]) + fabs(a[1])