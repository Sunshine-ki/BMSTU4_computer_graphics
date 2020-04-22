from numpy import arange
from math import *

from draw import *
from reflection import *


# def parametric_circle(center, radius):
def parametric_ellipse(center, axis):
    list_points = list()

    if axis[0] == axis[1] == 0:
        list_points.append([center[0], center[1]])
        return

    # step = 1 / radius
    step = 1 / axis[0] if axis[0] > axis[1] else 1 / axis[1]
    for t in arange(0, pi/4 + step, step):
        x = axis[0] * cos(t) + center[0]
        y = axis[1] * sin(t) + center[1]
        list_points.append([x, y])

    return list_points


def draw_ellipse(canvas_class, method, center, axis):
    print("method = ", method)
    print("center, axis", center, axis)
    print("color_line = ", canvas_class.color_line)

    list_points = list()

    if method == 0:
        print("Канонический")
        # canonical_circle(center, radius)
    elif method == 1:
        print("Параметрический")
        list_points = parametric_ellipse(center, axis)
    elif method == 2:
        pass
    elif method == 3:
        pass
    elif method == 4:
        print("Библиотечный")
        canvas_class.draw_oval(
            center[0] - axis[0], center[1] - axis[1], center[0] + axis[0], center[1] + axis[1])
        # canvas_class.draw_oval(
        # center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius)

    symmetrical_reflection(list_points, center)
    canvas_class.draw_figure(list_points)
