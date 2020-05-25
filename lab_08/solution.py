from math import *

from interface import print_error
from constants import *
from convex import IsConvex


def GetVector(line):
    # Чтобы найти координаты вектора AB, зная координаты его начальной точки
    # А и конечной точки В, необходимо из координат конечной точки вычесть
    # соответствующие координаты начальной точки.
    return [line[2] - line[0], line[3] - line[1]]


def Dot(line1, line2):
    vector1 = GetVector(line1)
    vector2 = GetVector(line2)

    result = float()
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result


def scalar(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def FindDirection(line):
    return [line[2] - line[0], line[3] - line[1]]


def Find_W(line1, line2):
    return [line1[0] - line2[0], line1[1] - line2[1]]


def FindNormal(edge, sing, inc_edge):  # edge
    # n = [edge[3] - edge[1], edge[2] - edge[0]]

    n = [edge[3] - edge[1], edge[0] - edge[2]]
    if scalar(n, GetVector(inc_edge)) < 0:
        n = [-n[0], -n[1]]

    result = [-sing * (edge[3] - edge[1]), sing *
              (edge[2] - edge[0])]
    print("n = ", n)
    print("Result n (+ sing) = ", result)

    return result
    # print(line[3], line[1])
    # print(line[2], line[0])
    # n = [line[3] - line[1], line[2] - line[0]]
    # # print(scalar(n, GetVector(edge)))
    # if scalar(n, GetVector(edge)) < 0:
    #     print("scalar(n, GetVector(edge)) < 0")
    #     n = [-n[0], n[1]]

    # return n


# [[62, 54, 71, 761], [71, 761, 746, 762], [746, 762, 738, 35], [738, 35, 62, 54]]
# [180, 25, 573, 782]

def ConvertParametric(line, t):
    return [line[0] + (line[2] - line[0]) * t, line[1] + (line[3] - line[1]) * t]


def CyrusBeck(rectangle, line, sing):
    # Изначально считаем, что отрезок полностью видимый.
    t_down, t_up = 0, 1
    # Находим директрису отрезка (Определяем направление).
    D = FindDirection(line)
    # print("D = ", D)
    # print("sing = ", sing)

    # Цикл отсечения отрезка.
    for i in range(len(rectangle)):
        # Находим W (fi - верширны многоугольника).
        W = Find_W(line, rectangle[i])
        # Находим вектор внутренней нормали.
        if i == len(rectangle) - 1:
            N = FindNormal(rectangle[i], sing, rectangle[0])
        else:
            N = FindNormal(rectangle[i], sing, rectangle[i + 1])
        # print("W = ", W)
        # print("N = ", N)
        # Скалярное произведение D на N.
        Dscalar = scalar(D, N)
        # Скалярное произведение W на N.
        Wscalar = scalar(W, N)

        # print("rectangle[i] = ", rectangle[i])
        # print("Dscalar = ", Dscalar)
        # print("Wscalar = ", Wscalar)

        # Если отрезок расположен параллельно i-ой стороне отсекателя
        # И находятся снаружи отсекателя, то отрезок невидимый.
        if Dscalar == 0 and Wscalar < 0:
            return - 1

        t = -Wscalar / Dscalar

        # Если Dск > 0 - то точку пересечения
        # нужно отнести к группе, определяющей начало видимой части.
        if Dscalar > 0:
            # Если т. пересечения вне отрезка,
            # Значит отрезок невидим.
            if t > 1:
                return - 1
            else:
                # Иначе нужно из точек, определяющих
                # начало, выбрать максимальное.
                t_down = max(t_down, t)
        # Если Dск < 0 - то точку пересечения нужно отнести к
        # группе, определяющей конец видимой части.
        if Dscalar < 0:
            # Если т. пересечения вне отрезка,
            # Значит отрезок невидим.
            if t < 0:
                return - 1
            else:
                t_up = min(t_up, t)

    if t_up < t_down:
        return - 1

    return [ConvertParametric(line, t_down), ConvertParametric(line, t_up)]


def FindSolution(line_list, rectangle, sing):
    result_list = list()

    # print("sing = ", sing)
    # print("rectangle = ", rectangle)
    # print("line_list", line_list)

    for i in range(len(line_list)):
        temp = CyrusBeck(rectangle[0], line_list[i], sing)
        if temp != -1:
            result_list.append(temp)

    return result_list


def SolutionWrapper(canvas_class, line_list, polygon):
    sing = IsConvex(polygon)
    if not sing:
        print_error("Многоугольник невыпуклый!")
        return

    result_list = FindSolution(line_list, polygon, sing)

    for i in range(len(result_list)):
        canvas_class.draw_line([result_list[i][0][0], result_list[i]
                                [0][1], result_list[i][1][0], result_list[i][1][1]], "green")
