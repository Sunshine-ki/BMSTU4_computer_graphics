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


# def main():
#     A = np.matrix('1 2 3; 4 5 6')
#     B = np.matrix('7 8; 9 1; 2 3')
#     C = A.dot(B)
#     print(C)

    # point_lst = [(5.0, -1.0), (4.0, -8.0), (-4.0, -4.0)]
    # # print(point_lst)

    # # Ищем АС.
    # line_one = find_coefficients(point_lst[0], point_lst[2])
    # # print(line_one)

    # # Ищем BQ. (Высота)
    # k = perpendicular_lines(line_one[0])
    # line_perpendicular_one = (k, find_coefficients_b(point_lst[1], k))
    # # print("BQ = ", line_perpendicular_one)

    # # Ищем BC.
    # line_two = find_coefficients(point_lst[1], point_lst[2])
    # # print(line_two)

    # # Ищем AP. (Вторая высота).
    # k = perpendicular_lines(line_two[0])
    # line_perpendicular_two = (k, find_coefficients_b(point_lst[0],k))
    # # print("AP = ", line_perpendicular_two)

    # # Ищем точку пересечения высот.
    # print(find_intersection_point(line_perpendicular_one, line_perpendicular_two))


# if __name__ == "__main__":
#     main()
