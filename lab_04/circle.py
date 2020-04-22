from numpy import arange
from math import *

from draw import *


def symmetrical_reflection(list_points, center):
    # complete the figure.
    # n = len(list_points)
    # for i in range(n - 1, 0, -1):
    #     list_points.append([list_points[i][1], list_points[i][0]])

    # n = len(list_points)
    # for i in range(n):
    #     list_points.append([list_points[i][0], HEIGHT - list_points[i][1]])

    # n = len(list_points)
    # for i in range(n):
    #     list_points.append([WIDTH - list_points[i][0], list_points[i][1]])

    n = len(list_points)

    for i in range(n):
        x = list_points[i][0]
        x -= center[0]
        y = list_points[i][1]
        y -= center[1]
        x, y = y, x
        x += center[0]
        y += center[1]
        list_points.append([x, y])


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


def draw_circle(canvas_class, method, center, radius):
    # print("method = ", method)
    # print("center = ", center)
    # print("radius = ", radius)
    print("color_line = ", canvas_class.color_line)

    list_points = list()

    if method == 0:
        print("Канонический")
        # canonical_circle(center, radius)
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
