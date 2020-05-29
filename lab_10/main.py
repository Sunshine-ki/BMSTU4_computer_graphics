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
    "Чтобы нарисовать отсекатель зажми левую кнопку мыши и кликай по холсту, тем самым ты задашь углы многоугольника." + \
    "Чтобы замкнуть нажми пробел. Все просто.\n" + \
    "Но для рисования отсекаемого многоугольника тебе потребуется зажать shift и кликать по холсту " + \
    " Чтобы замкнуть многоугольник нужно нажать (не отпуская shift) пробел"


def main():
    root = Tk()

    cutter = [[]]  # отсекатель
    contour = [[]]
    temp_contour = []
    settings_interface(root, "1200x800", "Лабораторная работа №9")

    # print_info(greeting)

    canvas_class = paint_class(root)

    figure_selection = selection(2, CHOICE, [1000, 100])

    create_label(root, "Красный - отсекатель", [1000, 15])
    create_label(root, "Синий - отсекаемый\n многоугольник ", [1000, 60])

    # create_label(root, "Ввод:", [1000, 425])
    create_label(root, "Вершина", [900, 175])
    entry_contour_start = create_entry(root, [1030, 175])
    # create_label(root, "До:", [900, 500])
    # entry_contour_stop = create_entry(root, [1000, 500])
    create_button("Добавить вершину", lambda arg1=temp_contour, arg2=entry_contour_start,
                  arg3=canvas_class, arg4=figure_selection: add_contour(arg1, arg2, arg3, arg4), [1000, 225])

    create_button("Замкнуть", lambda arg1=cutter,  arg2=contour, arg3=temp_contour,
                  arg4=canvas_class, arg5=figure_selection: close_contour(arg1, arg2, arg3, arg4, arg5), [1000, 275])

    create_button("Отсечь", lambda arg1=canvas_class, arg2=cutter, arg3=contour:
                  SolutionWrapper(arg1, arg2, arg3), [1000, 700])

    create_button("Стереть всё", lambda arg1=canvas_class, arg2=cutter, arg3=contour:
                  clear(arg1, arg2, arg3), [1000, 775])

    settings_bind(canvas_class, cutter, contour)
    root.bind(
        "<Shift-space>", lambda event, arg1=contour: canvas_class.keySpace_rectangle(event, arg1, "blue"))

    root.bind(
        "<space>", lambda event, arg1=cutter: canvas_class.keySpace_rectangle(event, arg1, "red"))

    root.mainloop()


if __name__ == "__main__":
    main()
