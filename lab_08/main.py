#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *

from functions_answer import *
from interface import *
from constants import *
from draw import *
from solution import *

greeting = "Добро пожаловать в \"Интуитивно понятный интерфейс\".\n" + \
    "Сейчас я коротко расскажу как рисовать:\n" + \
    "Чтобы нарисовать линию зажми левую кнопку мыши и проведи в нужное место, затем отпусти. Все просто.\n" + \
    "Но для рисования многоугольника тебе потребуется зажать shift и кликать по холсту, тем самым " + \
    "ты задашь углы многоугольника. Чтобы замкнуть многоугольник нужно нажать (не отпуская shift) пробел"


def main():
    root = Tk()
    # Список для всех линий.
    line_list = list()
    contour = [[]]
    temp_contour = []
    settings_interface(root, "1200x800", "Лабораторная работа №8")

    print_info(greeting)

    canvas_class = paint_class(root)

    create_label(root, "Координаты линии:", [1000, 25])
    create_label(root, "От:", [900, 75])
    entry_line_start = create_entry(root, [1000, 75])
    create_label(root, "До:", [900, 125])
    entry_line_stop = create_entry(root, [1000, 125])
    create_button("Добавить линию", lambda arg1=line_list, arg2=entry_line_start,
                  arg3=entry_line_stop, arg4=canvas_class: add_line(arg1, arg2, arg3, arg4), [1000, 175])

    create_label(root, "Ввод контура:", [1000, 425])
    create_label(root, "Вершина", [900, 450])
    entry_contour_start = create_entry(root, [1030, 450])
    create_button("Добавить вершину", lambda arg1=temp_contour, arg2=entry_contour_start,
                  arg4=canvas_class: add_contour(arg1, arg2, arg4), [1000, 500])

    create_button("Замкнуть", lambda arg1=temp_contour, arg2=contour,
                  arg3=canvas_class: close_contour(arg1, arg2, arg3), [1000, 550])

    create_button("Отсечь", lambda arg1=canvas_class, arg2=line_list, arg3=contour:
                  SolutionWrapper(arg1, arg2, arg3), [1000, 700])

    create_button("Стереть всё", lambda arg1=canvas_class, arg2=line_list, arg3=contour:
                  clear(arg1, arg2, arg3), [1000, 775])

    settings_bind(canvas_class, line_list, contour)
    root.bind(
        "<Shift-space>", lambda event, arg1=contour: canvas_class.keySpace_rectangle(event, arg1))

    root.mainloop()


if __name__ == "__main__":
    main()
