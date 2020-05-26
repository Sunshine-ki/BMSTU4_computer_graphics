import copy
from copy import deepcopy

from interface import print_error
from convex import IsConvex
from constants import *

EPS = 1e-6


def get_nodes(polygon):
    nodes = list()
    for i in range(len(polygon)):
        nodes.append([polygon[i][0], polygon[i][1]])
    return nodes


def is_intersection(ed1, ed2, norm):
    # Определяем видимость вершин относительно рассматриваемого ребра.
    visiable1 = IsVisiable(ed1[0], ed2[0], ed2[1], norm)
    visiable2 = IsVisiable(ed1[1], ed2[0], ed2[1], norm)

    # Если одна вершина видна, а вторая нет (Есть пересечение).
    # Иначе пересечения нет.
    if not (visiable1 ^ visiable2):
        return False

    # ищем пересечение
    p1 = ed1[0]
    p2 = ed1[1]

    q1 = ed2[0]
    q2 = ed2[1]

    delta = (p2[0] - p1[0]) * (q1[1] - q2[1]) - \
        (q1[0] - q2[0]) * (p2[1] - p1[1])
    delta_t = (q1[0] - p1[0]) * (q1[1] - q2[1]) - \
        (q1[0] - q2[0]) * (q1[1] - p1[1])

    if abs(delta) <= EPS:
        return p2

    t = delta_t / delta

    return [ed1[0][0] + (ed1[1][0] - ed1[0][0]) * t, ed1[0][1] + (ed1[1][1] - ed1[0][1]) * t]


def IsVisiable(point, peak1, peak2, norm):
    v = vector([peak1, point], [peak1, peak2])
    if norm * v < 0:
        return True
    return False


def GetVector(line):
    # Чтобы найти координаты вектора AB, зная координаты его начальной точки
    # А и конечной точки В, необходимо из координат конечной точки вычесть
    # соответствующие координаты начальной точки.
    return [line[1][0] - line[0][0], line[1][1] - line[0][1]]


def vector(line1, line2):
    vector1 = GetVector(line1)
    vector2 = GetVector(line2)
    return vector1[0] * vector2[1] - vector2[0] * vector1[1]


def sutherland_hodgman(cutter, polygon, norm):
    # Для удобства работы алгоритма первая вершина
    # отсекателя заносится в массив дважды (В начало и конец.).
    # Т.к. последнее ребро отсекателя образуется
    # последней и первой вершинами многоугольника.
    cutter.append(cutter[0])

    s = None
    f = None
    # цикл по вершинам отсекателя
    for i in range(len(cutter) - 1):
        new = []  # новый массив вершин
        # цикл по вершинам многоугольника
        for j in range(len(polygon)):
            # Если первая вершина
            if j == 0:
                # То запоминаем ее.
                f = polygon[j]
            else:
                 # Иначе определяем пересечение. (Если оно есть).
                t = is_intersection(
                    [s, polygon[j]], [cutter[i], cutter[i + 1]], norm)
                if t:
                    new.append(t)

            s = polygon[j]
            if IsVisiable(s,  cutter[i], cutter[i + 1], norm):
                new.append(s)

        if len(new):
            t = is_intersection([s, f], [cutter[i], cutter[i + 1]], norm)
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

    polygon = get_nodes(polygon[0])
    cutter = get_nodes(cutter[0])

    result = sutherland_hodgman(cutter, polygon, sign)

    if not result:
        return

    result.append(result[0])
    for i in range(len(result) - 1):
        canvas_class.draw_line(
            [round(result[i][0]), round(result[i][1]),
             round(result[i+1][0]), round(result[i+1][1])], "green", 2)


# def GetVector(line):
#     # Чтобы найти координаты вектора AB, зная координаты его начальной точки
#     # А и конечной точки В, необходимо из координат конечной точки вычесть
#     # соответствующие координаты начальной точки.
#     return [line[2] - line[0], line[3] - line[1]]

    #    if i == len(edges) - 1:
#     #         N = FindNormal(edges[i], edges[0])
#     #     else:
#     #         N = FindNormal(edges[i], edges[i + 1])


# def FindNormal(edge, inc_edge):
#     n = [edge[3] - edge[1], edge[0] - edge[2]]
#     if scalar(n, GetVector(inc_edge)) < 0:
#         n = [-n[0], -n[1]]
#     return n

# def scalar(v1, v2):
#     return v1[0] * v2[0] + v1[1] * v2[1]
