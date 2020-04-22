from numpy import arange
from math import *

from draw import *
from reflection import *


def parametric_circle(center, radius):
    list_points = list()

    if radius == 0:
        list_points.append([center[0], center[1]])
        return

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
        print("Канонический")
        list_points = canonical_circle(center, radius)
    elif method == 1:
        print("Параметрический")
        list_points = parametric_circle(center, radius)
    elif method == 2:
        pass
    elif method == 3:
        pass
    elif method == 4:
        print("Библиотечный")
        canvas_class.draw_oval(
            center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius)

    symmetrical_reflection(list_points, center)
    canvas_class.draw_figure(list_points)
