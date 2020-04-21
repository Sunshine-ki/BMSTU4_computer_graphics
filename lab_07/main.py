#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *

from functions_answer import *
from interface import *
from constants import *
from draw import *
from solution import *


def main():
    root = Tk()
    # Список для всех линий.
    line_list = list()
    contour = list()
    settings_interface(root, "1200x800", "Лабораторная работа №7")

    canvas_class = paint_class(root)

    create_label(root, "Координаты линии:", [1000, 25])
    create_label(root, "От:", [900, 75])
    entry_line_start = create_entry(root, [1000, 75])
    create_label(root, "До:", [900, 125])
    entry_line_stop = create_entry(root, [1000, 125])
    create_button("Добавить линию", lambda arg1=line_list, arg2=entry_line_start,
                  arg3=entry_line_stop, arg4=canvas_class: add_line(arg1, arg2, arg3, arg4), [1000, 175])

    create_label(root, "Координаты контура:", [1000, 400])
    create_label(root, "От:", [900, 450])
    entry_contour_start = create_entry(root, [1000, 450])
    create_label(root, "До:", [900, 500])
    entry_contour_stop = create_entry(root, [1000, 500])
    create_button("Добавить контур", lambda arg1=contour, arg2=entry_contour_start,
                  arg3=entry_contour_stop, arg4=canvas_class: add_contour(arg1, arg2, arg3, arg4), [1000, 550])

    create_button("Отсечь", lambda arg1=canvas_class, arg2=line_list, arg3=contour:
                  solution_wrapper(arg1, arg2, arg3), [1000, 700])

    create_button("Стереть всё", lambda arg1=canvas_class, arg2=line_list:
                  clear(arg1, arg2), [1000, 775])

    settings_bind(canvas_class, line_list, contour)

    root.mainloop()


if __name__ == "__main__":
    main()
