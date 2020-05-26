from interface import print_error
from convex import IsConvex
from constants import *

import copy
from copy import deepcopy


def get_nodes(polygon):
    nodes = list()
    for i in range(len(polygon)):
        nodes.append([polygon[i][0], polygon[i][1]])
    return nodes

# (Отсекатель)cutter = [
#     [[663, 230, 532, 516], [532, 516, 198, 508], [198, 508, 193, 351], [193, 351, 663, 230]],
#     [[354, 410, 405, 475], [405, 475, 463, 379], [463, 379, 333, 351], [333, 351, 354, 410]],
#     [[286, 436, 124, 314], [124, 314, 165, 210], [165, 210, 251, 242], [251, 242, 286, 436]], []]
# contour = [
#     [[165, 54, 175, 296], [175, 296, 417, 312], [417, 312, 414, 89], [414, 89, 165, 54]],
#     [[138, 89, 114, 386], [114, 386, 501, 429], [501, 429, 459, 39], [459, 39, 138, 89]],
#     [[229, 160, 246, 259], [246, 259, 332, 233], [332, 233, 280, 125], [280, 125, 229, 160]],
#     []]


def is_intersection(ed1, ed2, norm):
    vis1 = is_visiable(ed1[0], ed2[0], ed2[1], norm)
    vis2 = is_visiable(ed1[1], ed2[0], ed2[1], norm)
    if (vis1 and not vis2) or (not vis1 and vis2):
        # ищем пересечение

        p1 = ed1[0]
        p2 = ed1[1]

        q1 = ed2[0]
        q2 = ed2[1]

        delta = (p2[0] - p1[0]) * (q1[1] - q2[1]) - \
            (q1[0] - q2[0]) * (p2[1] - p1[1])
        delta_t = (q1[0] - p1[0]) * (q1[1] - q2[1]) - \
            (q1[0] - q2[0]) * (q1[1] - p1[1])

        if abs(delta) <= 1e-6:
            return p2

        t = delta_t / delta

        return [ed1[0][0] + (ed1[1][0] - ed1[0][0]) * t, ed1[0][1] + (ed1[1][1] - ed1[0][1]) * t]
    else:
        return False


def is_visiable(point, peak1, peak2, norm):

    # print(point, peak1, peak2, norm)
    # print(norm)

    v = vector([point, peak1], [peak2, peak1])
    if norm * v < 0:
        return True
    return False


def vector(v1, v2):
    x1 = v1[0][0] - v1[1][0]
    y1 = v1[0][1] - v1[1][1]

    x2 = v2[0][0] - v2[1][0]
    y2 = v2[0][1] - v2[1][1]

    return x1 * y2 - x2 * y1


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
            if is_visiable(s,  cutter[i], cutter[i + 1], norm):
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
