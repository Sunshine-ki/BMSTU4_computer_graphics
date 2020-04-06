#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *

from functions_answer import *
from interface import *
from constants import *
from draw import *


def lock():
    pass


def fill(canvas_class):
    pass


def delayed_fill(canvas_class):
    pass


def add_point(point_coordinates, list_box):
    point = get_two_answer(point_coordinates.get())
    if point[0] == FALSE:
        return

    # Проверка, есть ли эта точка.

    # list_box.insert(END, a)

    # for i in range(len(point_lst), 0, -1):
    # list_box.delete(i)

    list_box.insert(END, point)


def main():
    root = Tk()
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

    create_button("Добавить точку", lambda arg1=entry_point_coordinates, arg2=list_box: add_point(
        arg1, arg2), [1000, 165])

    create_button("Замкнуть", lock, [1000, 200])

    create_button(
        "Заполнить", lambda arg1=canvas_class: fill(arg1), [1000, 675])

    create_button(
        "Заполнить с задержкой", lambda arg1=canvas_class: delayed_fill(arg1), [1000, 725])

    create_button("Стереть всё", canvas_class.clear_all, [1000, 775])

    root.mainloop()


if __name__ == "__main__":
    main()
