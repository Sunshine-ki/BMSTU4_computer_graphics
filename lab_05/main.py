#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from math import fabs

from functions_answer import *
from interface import *
from constants import *
from draw import *


def sign(a):
    if a == 0:
        return 0
    return a / abs(a)


def bresenham_int(canvas_class, start, stop, lst):
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
        lst.append([int(x), int(y)])
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


def lock(points_list, canvas_class, list_box, lst):
    if len(points_list[-1]) > 1:
        start = points_list[-1][0]
        stop = points_list[-1][-1]
        # canvas_class.canvas.create_line(round(start[0]), round(start[1]), round(
        # stop[0]), round(stop[1]), width=1, fill="black")
        bresenham_int(canvas_class, start, stop, lst)

        points_list.append(list())
        list_box.insert(END, "_" * 8)
        # print(lst)


def fill(canvas_class, lst):
    lst = list(lst)
    # for i in range(len(lst[0])):
    #     y = lst[i][1]
    #     for x in range(lst[i][0], WIDTH):
    #         # canvas_class.reverse_color(y, x)
    #         print(y, x)

    # reverse_color()
    for i in range(10):
        canvas_class.reverse_color(400, 400)
    # for i in range(len(lst)):
    #     # for j in range(lst[i][0], WIDTH):
    #     start = lst[i]
    #     stop = [WIDTH, lst[i][1]]
    #     canvas_class.canvas.create_line(round(start[0]), round(
    #         start[1]), round(stop[0]), round(stop[1]), width=1, fill="black")
    #     # canvas_class.print_pixel(j, lst[i][1])


def delayed_fill(canvas_class):
    pass


def add_point(points_list, point, canvas_class, list_box, lst):
    if point in points_list[-1]:
        print_error("Такая точка уже имеется в данном многоугольнике!")
        return
    points_list[-1].append(point)

    list_box.insert(END, point)

    # print(points_list[-1])

    if len(points_list[-1]) > 1:
        start = points_list[-1][-1]
        stop = points_list[-1][-2]
        # canvas_class.canvas.create_line(round(start[0]), round(start[1]), round(
        # stop[0]), round(stop[1]), width=1, fill="black")
        bresenham_int(canvas_class, stop, start, lst)
    elif len(points_list[-1]) == 1:
        canvas_class.print_pixel(points_list[-1][0][0], points_list[-1][0][1])
        lst.append([points_list[-1][0][0], points_list[-1][0][1]])

    print(lst)


def add_point_click(event, canvas_class, list_box, points_list, lst):
    add_point(points_list, [event.x, event.y], canvas_class, list_box, lst)


def add_point_entry(point_coordinates, list_box, canvas_class, points_list, lst):
    point = list(get_two_answer(point_coordinates.get()))
    if point[0] == FALSE:
        return
    add_point(points_list, point, canvas_class, list_box, lst)


def clear(canvas_class, list_box, points_list, lst):
    canvas_class.clear_all()

    list_box.delete(1, list_box.size())

    for i in range(len(points_list) - 1, -1, -1):
        del points_list[i]

    for i in range(len(lst) - 1, -1, -1):
        del lst[i]

    points_list.append([])
    # print(points_list)


def main():
    root = Tk()
    # Список для всех точек.
    lst = list()
    points_list = [[]]
    # Лабораторная работа №5.
    settings_interface(root, "1200x800", "Растровое заполнение областей")

    canvas_class = paint_class(root)
    list_box = create_list_box(root, [800, 325])

    create_button("Выбрать цвет заполнения",
                  canvas_class.choose_color_line, [1000, 25])
    # create_button("Заполнять фоновым цветом",
    #   canvas_class.draw_color_background, [1000, 60])

    create_label(root, "Координаты точки:", [1000, 100])
    entry_point_coordinates = create_entry(root, [1000, 125])

    create_button("Добавить точку", lambda arg1=entry_point_coordinates, arg2=list_box, arg3=canvas_class,
                  arg4=points_list, arg5=lst: add_point_entry(arg1, arg2, arg3, arg4, arg5), [1000, 165])

    create_button("Замкнуть", lambda arg1=points_list,
                  arg2=canvas_class, arg3=list_box, arg4=lst: lock(arg1, arg2, arg3, arg4), [1000, 200])

    create_button(
        "Заполнить", lambda arg1=canvas_class, arg2=lst: fill(arg1, arg2), [1000, 675])

    create_button(
        "Заполнить с задержкой", lambda arg1=canvas_class: delayed_fill(arg1), [1000, 725])

    create_button("Стереть всё", lambda arg1=canvas_class, arg2=list_box, arg3=points_list, arg4=lst:
                  clear(arg1, arg2, arg3, arg4), [1000, 775])
    canvas_class.canvas.bind('<Button-1>', lambda event,
                             arg1=canvas_class, arg2=list_box, arg3=points_list, arg4=lst: add_point_click(event, arg1, arg2, arg3, arg4))

    root.mainloop()


if __name__ == "__main__":
    main()
