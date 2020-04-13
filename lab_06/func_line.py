from tkinter import *
from math import fabs

from functions_answer import get_two_answer
from interface import print_error
from constants import *


def sign(a):
    if a == 0:
        return 0
    return a / abs(a)


def bresenham_int(canvas_class, start, stop):
    dx = stop[0] - start[0]
    dy = stop[1] - start[1]
    x, y = start[0], start[1]
    sx, sy = sign(dx), sign(dy)
    dx = fabs(dx)
    dy = fabs(dy)

    swap = 0

    if dy > dx:
        swap = 1
        dx, dy = dy, dx

    e = 2 * dy - dx

    for _ in range(int(dx + 1)):
        canvas_class.print_pixel(int(x), int(y))
        if e >= 0:
            if swap == 0:
                y += sy
            else:
                x += sx
            e -= (2 * dx)

        if e < 0:
            if swap == 0:
                x += sx
            else:
                y += sy
            e += (2 * dy)


def lock(points_list, canvas_class, list_box):
    if len(points_list[-1]) > 1:
        start = points_list[-1][-1]
        stop = points_list[-1][0]

        bresenham_int(canvas_class, start, stop)

        points_list.append(list())
        list_box.insert(END, "_" * 8)


def add_point(points_list, point, canvas_class, list_box):
    if point in points_list[-1]:
        print_error("Такая точка уже имеется в данном многоугольнике!")
        return
    points_list[-1].append(point)

    list_box.insert(END, point)

    if len(points_list[-1]) > 1:
        start = points_list[-1][-2]
        stop = points_list[-1][-1]

        bresenham_int(canvas_class, stop, start)
    elif len(points_list[-1]) == 1:
        canvas_class.print_pixel(points_list[-1][0][0], points_list[-1][0][1])


def add_point_click(event, canvas_class, list_box, points_list):
    add_point(points_list, [event.x, event.y], canvas_class, list_box)


def add_point_entry(point_coordinates, list_box, canvas_class, points_list):
    point = list(get_two_answer(point_coordinates.get()))
    if point[0] == FALSE:
        return
    add_point(points_list, point, canvas_class, list_box)
