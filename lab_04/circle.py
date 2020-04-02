from numpy import arange
from math import *

from draw import *

# def canonical_circle(canvas, center, radius, color_line):
# pass


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


def draw_circle(canvas, method, center, radius, color_line):
    # print("method = ", method)
    # print("center = ", center)
    # print("radius = ", radius)
    print("color_line = ", color_line)

    list_points = list()

    if method == 0:
        print("Канонический")
        # canonical_circle(canvas, center, radius, color_line)
    elif method == 1:
        print("Параметрический")
        list_points = parametric_circle(center, radius)
    elif method == 2:
        pass
    elif method == 3:
        pass
    elif method == 4:
        print("Библиотечный")
        canvas.create_oval(center[0] - radius, center[1] - radius,
                           center[0] + radius, center[1] + radius, outline=color_line[1])

    draw_figure(canvas, color_line, list_points)
