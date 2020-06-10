from numpy import arange
from math import *

from draw import *
from reflection import *


def brezenham_circle(center, r):
    list_points = list()

    x = 0
    y = r
    list_points.append([x + center[0], y + center[1]])
    delta = 2 - r - r

    while x < y:
        if delta <= 0:
            d1 = delta + delta + y + y - 1
            x += 1
            if d1 >= 0:
                y -= 1
                delta += 2 * (x - y + 1)
            else:
                delta += x + x + 1

        else:
            d2 = 2 * (delta - x) - 1
            y -= 1
            if d2 < 0:
                x += 1
                delta += 2 * (x - y + 1)
            else:
                delta -= y + y - 1
        list_points.append([x + center[0], y + center[1]])

    return list_points


def middle_point_circle(center, r):

    list_points = list()
    x = r
    y = 0

    list_points.append([center[0] + x, center[1] + y])

    f = 1 - r

    while x > y:
        y += 1

        if f >= 0:
            x -= 1
            f -= x + x

        f += y + y + 1

        list_points.append([center[0] + x, center[1] + y])

    return list_points


def parametric_circle(center, radius):
    list_points = list()

    step = 1 / radius
    for t in arange(0, pi/4 + step, step):
        x = radius * cos(t) + center[0]
        y = radius * sin(t) + center[1]
        list_points.append([x, y])

    return list_points


def canonical_circle(center, radius):
    list_points = list()
    R = radius * radius

    for x in range(center[0], round(center[0] + radius / sqrt(2) + 1)):
        y = center[1] + sqrt(R - (x - center[0]) ** 2)
        list_points.append([x, y])

    return list_points


def draw_circle(canvas_class, method, center, radius):
    list_points = list()

    if method == 0:
        # print("Канонический")
        list_points = canonical_circle(center, radius)
    elif method == 1:
        # print("Параметрический")
        list_points = parametric_circle(center, radius)
    elif method == 2:
        list_points = brezenham_circle(center, radius)
    elif method == 3:
        list_points = middle_point_circle(center, radius)
        pass
    elif method == 4:
        # print("Библиотечный")
        canvas_class.draw_oval(
            center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius)
    else:
        print("Нет данного метода.")

    symmetrical_reflection(list_points, center)
    canvas_class.draw_figure(list_points)


def draw_concentric_circle(canvas_class, center, method, r1, r2, step):
    for i in range(r1, r2, step):
        # canvas_class, method, center, radius
        draw_circle(canvas_class, method, center, i)
