from numpy import arange
from math import *

from draw import *
from reflection import *


def ellipse_canonical(center, a, b):
    list_points = list()

    for x in range(0, a + 1, 1):
        y = round(sqrt(1 - (x/a)**2) * b)
        list_points.append([center[0] + x, center[1] + y])

    for y in range(0, b + 1, 1):
        x = round(sqrt(1 - (y / b)**2) * a)
        list_points.append([center[0] + x, center[1] + y])

    return list_points


def parametric_ellipse(center, axis):
    list_points = list()

    step = 1 / max(axis[0], axis[1])
    for t in arange(0, pi/2 + step, step):
        x = axis[0] * cos(t) + center[0]
        y = axis[1] * sin(t) + center[1]
        list_points.append([x, y])

    return list_points


def brezenham_ellipse(center, a, b):
    list_points = list()
    x = 0
    y = b
    sqr_b = b * b
    sqr_a = a * a
    list_points.append([x + center[0], y + center[1]])
    delta = sqr_b - sqr_a * (2 * b + 1)

    while y > 0:
        if delta <= 0:
            d1 = 2 * delta + sqr_a * (2 * y - 1)
            x += 1
            delta += sqr_b * (2 * x + 1)
            if d1 >= 0:
                y -= 1
                delta += sqr_a * (-2 * y + 1)

        else:
            d2 = 2 * delta + sqr_b * (-2 * x - 1)
            y -= 1
            delta += sqr_a * (-2 * y + 1)
            if d2 < 0:
                x += 1
                delta += sqr_b * (2 * x + 1)
        list_points.append([x + center[0], y + center[1]])

    return list_points


def middle_point_ellipse(center, a, b):
    list_points = list()

    sqr_a, sqr_b = a * a, b * b
    limit = round(a / sqrt(1 + sqr_b / sqr_a))
    x, y = 0, b

    list_points.append([x + center[0], y + center[1]])

    f = sqr_b - round(sqr_a * (b - 1 / 4))
    while x < limit:
        if f > 0:
            y -= 1
            f -= 2 * sqr_a * y
        x += 1
        f += sqr_b * (2 * x + 1)
        list_points.append([x + center[0], y + center[1]])

    limit = round(b / sqrt(1 + sqr_a / sqr_b))

    y, x = 0, a
    list_points.append([x + center[0], y + center[1]])
    f = sqr_a - round(sqr_b * (a - 1 / 4))
    while y < limit:
        if f > 0:
            x -= 1
            f -= 2 * sqr_b * x
        y += 1
        f += sqr_a * (2 * y + 1)
        list_points.append([x + center[0], y + center[1]])

    return list_points


def draw_ellipse(canvas_class, method, center, axis):
    # print("method = ", method)
    # print("center, axis", center, axis)
    # print("color_line = ", canvas_class.color_line)

    list_points = list()

    if method == 0:
        # print("Канонический")
        list_points = ellipse_canonical(center, axis[0], axis[1])
        # canonical_circle(center, radius)
    elif method == 1:
        # print("Параметрический")
        list_points = parametric_ellipse(center, axis)
    elif method == 2:
        list_points = brezenham_ellipse(center, axis[0], axis[1])
    elif method == 3:
        # print("middle point")
        list_points = middle_point_ellipse(center, axis[0], axis[1])
    elif method == 4:
        # print("Библиотечный")
        canvas_class.draw_oval(
            center[0] - axis[0], center[1] - axis[1], center[0] + axis[0], center[1] + axis[1])
        # canvas_class.draw_oval(
        # center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius)

    # symmetrical_reflection(list_points, center)
    reflection_x(list_points, center)
    reflection_y(list_points, center)
    canvas_class.draw_figure(list_points)


def draw_concentric_ellipse(canvas_class, center, method, r1, r2, count, step):
    i = 0
    while i < count:
        # draw_ellipse(canvas_class, method, center, axis)
        draw_ellipse(canvas_class, method, center, [r1, r2])
        r1 += step
        r2 += step
        i += 1
