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
    return [round(line[0][0] + (line[1][0] - line[0][0]) * t), round(line[0][1] + (line[1][1] - line[0][1]) * t)]


def IsIntersection(ed1, ed2, peak):
    # ed1 - ребро отсекаемого многоугольника.
    # ed2 - ребро отсекателя.
    # peak - след. вершина отсекателя, нужна для
    # корректного определения нормали
    # Определяем видимость вершин относительно рассматриваемого ребра.
    visiable1 = IsVisiable(ed1[0], ed2[0], ed2[1], peak)
    visiable2 = IsVisiable(ed1[1], ed2[0], ed2[1], peak)
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
    # DScalar может быть равен нулю в двух случаях:
    # 1. Если ребро отсекателя вырождается в точку
    # Т.е. p1 == p2. В интерфейсе обработан данный случай
    # (Пользователь не может ввести ребро у которого начало и конец совпадают)
    # 2. Если текущее ребро отсекаемого многоугольника параллельно
    # Ребру отсекателя. Такие ребра не дойдут до этого момента -
    # Они будут обработаны выше. Т.к. в этом случае нет пересечения
    # Обе вершины отсекаемого многоугольника будут либо по видимую сторону
    # Отсекателя, либо по невидимую.
    t = -WScalar/DScalar
    return ConvertParametric(ed1, t)


def Scalar(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def FindNormal(peak1, peak2, peak3):
    n = [peak2[1] - peak1[1], peak1[0] - peak2[0]]
    # Если скалярное произведение вектора нормали
    # На вектор, который является следующим ребром
    # Многоугольника, дает нам отрицательное значение,
    # То вектор нормали нужно домножить на -1
    # Чтобы он был направлен внутрь многоугольника.
    if Scalar([peak3[0] - peak2[0], peak3[1] - peak2[1]], n) < 0:
        n = [-n[0], -n[1]]
    return n


def IsVisiable(point, peak1, peak2, peak3):
    # Находим нормаль к ребру (peak1, peak2)
    # peak3 нужно, чтобы проверить нормаль (Внутренняя ли она).
    n = FindNormal(peak1, peak2, peak3)
    if Scalar(n, GetVector([peak2, point])) < 0:
        return False
    return True


def GetVector(line):
    return [line[1][0] - line[0][0], line[1][1] - line[0][1]]


def SutherlandHodgman(cutter, polygon):
    # Для удобства работы алгоритма первая вершина
    # отсекателя заносится в массив дважды (В начало и конец).
    # Т.к. последнее ребро отсекателя образуется
    # последней и первой вершинами многоугольника.
    cutter.append(cutter[0])
    # Также, т.к. для поиска нормали для ребра i и i+1
    # Мне нужна вершина i+2. Поэтому я дублирую еще вторую вершину.
    # (Чтобы могла в цикле отправлять i+2).
    cutter.append(cutter[1])
    # Цикл по вершинам отсекателя.
    for i in range(len(cutter) - 2):
        new = []  # новый массив вершин
        # Особым образом нужно обрабатывать первую
        # точку многоугольника: для нее требуется определить
        # только видимость. Если точка видима, то она заносится
        # В результирующий список и становится начальной точкой первого ребра.
        # Если же она невидима, то она просто становится начальной точкой ребра
        # И в результирующий список не заносится.
        f = polygon[0]  # Запоминаем первую вершину.
        if IsVisiable(f,  cutter[i], cutter[i + 1], cutter[i + 2]):
            new.append(f)
        s = polygon[0]
        # Цикл по вершинам многоугольника
        for j in range(1, len(polygon)):
            # Определяем пересечение текущего ребра отсекателя (cutter[i], cutter[i + 1])
            # И рассматриваемого ребра отсекаемого многоугольника (s, polygon[j]),
            # Где s = polygon[j - 1]. cutter[i + 2] нам нужно, чтобы корректно найти нормаль.
            t = IsIntersection([s, polygon[j]], [cutter[i],
                                                 cutter[i + 1]], cutter[i + 2])
            # Если есть пересечение, то заносим его в новый массив вершин.
            if t:
                new.append(t)
            # Запоминаем в s текущую вершину. (Чтобы на следующем шаге
            # Искать пересечение polygon[j - 1] и polygon[j])
            s = polygon[j]
            # Проверяем, видна ли текущая вершина
            if IsVisiable(s, cutter[i], cutter[i + 1], cutter[i + 2]):
                # Если видна, то заносим ее в новый массив вершин.
                new.append(s)
        # Можно убедиться в полной невидимости многоугольника,
        # относительно текущей границы отсекателя. При анализе
        # последнего замыкающего ребра отсутствие результата означает невидимость
        # многоугольника относительно текущей границы отсекателя, а значит многоугольник невидимый.
        if not len(new):
            return False
        t = IsIntersection([s, f], [cutter[i], cutter[i + 1]], cutter[i + 2])
        if t:
            new.append(t)
        polygon = deepcopy(new)
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

    result = SutherlandHodgman(cutter, polygon)

    if not result:
        return

    result.append(result[0])
    for i in range(len(result) - 1):
        canvas_class.draw_line(
            [round(result[i][0]), round(result[i][1]),
             round(result[i+1][0]), round(result[i+1][1])], "green", 2)
