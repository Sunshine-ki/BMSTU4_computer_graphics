from define import *
from math import fabs, sqrt


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

def length(a, b):
    return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def perpendicular_triangles(a, b, c):
    ab = length(a, b)
    ac = length(a, c)
    bc = length(b, c)
    eps = 1e-3
    # print("AB = ", ab, "AC = ", ac, "BC = ", bc)
    # print("ab * ab + bc * bc = ", ab * ab + bc * bc,  ac * ac)
    # print("ab * ab + ac * ac = ", ab * ab + ac * ac, bc * bc)
    # print("ac * ac + bc * bc = ", ac * ac + bc * bc, ab * ab)
    if (ab * ab + bc * bc - ac * ac < eps):
        return b
    if (ab * ab + ac * ac - bc * bc < eps):
        return a
    if (ac * ac + bc * bc - ab * ab < eps):
        return c 

    # print("Ab = ", ab, ac, bc)
    return False, False