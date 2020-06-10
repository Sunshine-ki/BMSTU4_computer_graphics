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

    settings_interface(root, "1200x800", "Алгоритм Плавающего горизонта")

    canvas_class = paint_class(root)

    choice_func = option_menu(root, CHOICE, [1000, 30])

    create_label(root, "Пределы по x:", [1000, 100])
    borders_x = create_entry(root, [1000, 125], DEFAULT_BORDERS_X)

    create_label(root, "Шаг по x:", [1000, 150])
    step_x = create_entry(root, [1000, 175], DEFAULT_STEP_X)

    create_label(root, "Пределы по z:", [1000, 225])
    borders_z = create_entry(root, [1000, 250], DEFAULT_BORDERS_Z)

    create_label(root, "Шаг по z:", [1000, 275])
    step_z = create_entry(root, [1000, 300], DEFAULT_STEP_Z)

    create_label(root, "∠ по x:", [1000, 350])
    angle_x = create_entry(root, [1000, 375], DEFAULT_ANGLE_X)

    create_label(root, "∠ по y:", [1000, 400])
    angle_y = create_entry(root, [1000, 425], DEFAULT_ANGLE_Y)

    create_label(root, "∠ по z:", [1000, 450])
    angle_z = create_entry(root, [1000, 475], DEFAULT_ANGLE_Z)

    create_button(
        "Отобразить", lambda arg1=choice_func, arg2=[borders_x, borders_z], arg3=[step_x, step_z], arg4=[angle_x, angle_y, angle_z], arg5=canvas_class:  SolutionWrapper(arg1, arg2, arg3, arg4, arg5), [1000, 700])

    canvas_class.canvas.bind(
        "<Motion>", lambda event: canvas_class.in_canvas(event))

    root.mainloop()


if __name__ == "__main__":
    main()
