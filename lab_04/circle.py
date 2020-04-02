from numpy import arange
from math import *

from draw import *


def parametric_circle(center, radius):
    list_points = list()

    if radius == 0:
        list_points.append([center[0], center[1]])
        return

    for t in arange(0, 2 * pi, 1/radius):
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

    canvas_class.draw_figure(list_points)
