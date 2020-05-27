import copy
from copy import deepcopy

from interface import print_error
from convex import IsConvex
from constants import *


def GetNodes(polygon):
    nodes = list()
    for i in range(len(polygon)):
        nodes.append([polygon[i][0], polygon[i][1]])
    return nodes


def FindDirection(line):
    return [line[1][0] - line[0][0], line[1][1] - line[0][1]]


def Find_W(p1, p2):
    return [p1[0] - p2[0], p1[1] - p2[1]]


def ConvertParametric(line, t):
    return [line[0][0] + (line[1][0] - line[0][0]) * t, line[0][1] + (line[1][1] - line[0][1]) * t]


def IsIntersection(ed1, ed2, norm, peak):
    # ed1 - ребро отсекаемого многоугольника.
    # ed2 - ребро отсекателя.
    # Определяем видимость вершин относительно рассматриваемого ребра.
    visiable1 = IsVisiable(ed1[0], ed2[0], ed2[1], norm, peak)
    visiable2 = IsVisiable(ed1[1], ed2[0], ed2[1], norm, peak)

    # Если одна вершина видна, а вторая нет (Есть пересечение).
    # Иначе пересечения нет.
    if not (visiable1 ^ visiable2):
        return False
    # Ищем пересечение
    N = FindNormal(ed2[0], ed2[1], peak)
    D = FindDirection(ed1)
    W = Find_W(ed1[0], ed2[0])

    # Скалярное произведение D на N.
    DScalar = Scalar(D, N)
    # Скалярное произведение W на N.
    WScalar = Scalar(W, N)

    if abs(DScalar) <= EPS:
        return ed1[1]

    t = -WScalar/DScalar

    return ConvertParametric(ed1, t)


def Scalar(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def FindNormal(peak1, peak2, peak3):
    n = [peak2[1] - peak1[1], peak1[0] - peak2[0]]
    # Если скалярное произведение вектора нормали
    # На вектор, который является следующим ребром
    # Многоугольника, дает нам отрицательное значание,
    # То вектор нормали нужно домножить на -1
    # Чтобы он был направлен внутрь многоугольника.
    if Scalar([peak3[0] - peak2[0], peak3[1] - peak2[1]], n) < 0:
        n = [-n[0], -n[1]]
    return n


def IsVisiable(point, peak1, peak2, norm, peak3):
    # Находим нормаль к ребру (peak1, peak2)
    # peak3 нужно, чтобы проверить нормаль (Внутренняя ли она).
    n = FindNormal(peak1, peak2, peak3)
    if Scalar(n, GetVector([peak2, point])) < 0:
        return False
    return True


def GetVector(line):
    # Чтобы найти координаты вектора AB, зная координаты его начальной точки
    # А и конечной точки В, необходимо из координат конечной точки вычесть
    # соответствующие координаты начальной точки.
    return [line[1][0] - line[0][0], line[1][1] - line[0][1]]


def SutherlandHodgman(cutter, polygon, norm):
    # Для удобства работы алгоритма первая вершина
    # отсекателя заносится в массив дважды (В начало и конец.).
    # Т.к. последнее ребро отсекателя образуется
    # последней и первой вершинами многоугольника.
    cutter.append(cutter[0])
    cutter.append(cutter[1])

    s = None
    f = None
    # цикл по вершинам отсекателя
    for i in range(len(cutter) - 2):
        new = []  # новый массив вершин
        # цикл по вершинам многоугольника
        for j in range(len(polygon)):
            # Если первая вершина
            if j == 0:
                # То запоминаем ее.
                f = polygon[j]
            else:
                 # Иначе определяем пересечение. (Если оно есть).
                t = IsIntersection(
                    [s, polygon[j]], [cutter[i], cutter[i + 1]], norm, cutter[i + 2])
                if t:
                    new.append(t)

            s = polygon[j]
            if IsVisiable(s,  cutter[i], cutter[i + 1], norm, cutter[i + 2]):
                new.append(s)

        if len(new):
            t = IsIntersection(
                [s, f], [cutter[i], cutter[i + 1]], norm, cutter[i + 2])
            if t:
                new.append(t)
        # print(new, "\n\n")
        polygon = copy.deepcopy(new)

    if len(polygon) == 0:
        return False
    return polygon


def SolutionWrapper(canvas_class, cutter, polygon):
    if len(cutter) <= 1:
        print_error("Отсекатель не задан!")
        return

    if len(polygon[0]) <= 1:
        print_error("Многоугольник не задан!")
        return

    sign = IsConvex(cutter)
    if sign == False:
        print_error("Отсекатель не выпуклый!")
        return

    polygon = GetNodes(polygon[0])
    cutter = GetNodes(cutter[0])

    result = SutherlandHodgman(cutter, polygon, sign)

    if not result:
        return

    result.append(result[0])
    for i in range(len(result) - 1):
        canvas_class.draw_line(
            [round(result[i][0]), round(result[i][1]),
             round(result[i+1][0]), round(result[i+1][1])], "green", 2)
