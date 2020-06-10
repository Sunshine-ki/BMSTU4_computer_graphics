from math import *

from interface import print_error
from constants import *
from convex import IsConvex


def scalar(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def FindDirection(line):
    return [line[2] - line[0], line[3] - line[1]]


def Find_W(line1, p):
    return [line1[0] - p[0], line1[1] - p[1]]


def GetVector(line):
    # Чтобы найти координаты вектора AB, зная координаты его начальной точки
    # А и конечной точки В, необходимо из координат конечной точки вычесть
    # соответствующие координаты начальной точки.
    return [line[2] - line[0], line[3] - line[1]]


def FindNormal(edge, inc_edge):
    n = [edge[3] - edge[1], edge[0] - edge[2]]
    if scalar(n, GetVector(inc_edge)) < 0:
        n = [-n[0], -n[1]]
    return n


def ConvertParametric(line, t):
    return [line[0] + (line[2] - line[0]) * t, line[1] + (line[3] - line[1]) * t]


def CyrusBeck(edges, line):
    # Изначально считаем, что отрезок полностью видимый.
    t_b, t_e = 0, 1  # begin, end.
    # Находим директрису отрезка (Определяем направление).
    D = FindDirection(line)
    # Цикл отсечения отрезка.
    for i in range(len(edges)):
        # Находим W (fi - верширны многоугольника).
        W = Find_W(line, edges[i])
        # Находим вектор внутренней нормали.
        if i == len(edges) - 1:
            N = FindNormal(edges[i], edges[0])
        else:
            N = FindNormal(edges[i], edges[i + 1])
        # Скалярное произведение D на N.
        Dscalar = scalar(D, N)
        # Скалярное произведение W на N.
        Wscalar = scalar(W, N)
        # Если отрезок расположен параллельно i-ой стороне отсекателя
        if Dscalar == 0:
            # И находятся снаружи отсекателя
            if Wscalar < 0:
                # то отрезок невидимый.
                return
        else:
            t = -Wscalar / Dscalar
            # Если Dск > 0 - то точку пересечения
            # нужно отнести к группе, определяющей начало видимой части.
            if Dscalar > 0:
                # Если т. пересечения вне отрезка,
                # Значит отрезок невидим.
                if t > 1:
                    return
                else:
                    # Иначе нужно из точек, определяющих
                    # начало, выбрать максимальное.
                    t_b = max(t_b, t)
            # Если Dск < 0 - то точку пересечения нужно отнести к
            # группе, определяющей конец видимой части.
            elif Dscalar < 0:
                # Если т. пересечения вне отрезка,
                # Значит отрезок невидим.
                if t < 0:
                    return
                else:
                    # Иначе нужно из точек, определяющих
                    # конец, выбрать минимальное.
                    t_e = min(t_e, t)
    # Проверка видимости отрезка
    if t_e < t_b:
        return
    # Возвращаем начало и конец видимого отрезка.
    return [ConvertParametric(line, t_b), ConvertParametric(line, t_e)]


def FindSolution(line_list, edges):
    result_list = list()

    for i in range(len(line_list)):
        temp = CyrusBeck(edges[0], line_list[i])
        if temp:
            result_list.append(temp)

    return result_list


def SolutionWrapper(canvas_class, line_list, polygon):
    sing = IsConvex(polygon)
    if not sing:
        print_error("Многоугольник невыпуклый!")
        return

    result_list = FindSolution(line_list, polygon)

    for i in range(len(result_list)):
        canvas_class.draw_line([result_list[i][0][0], result_list[i]
                                [0][1], result_list[i][1][0], result_list[i][1][1]], "green")
