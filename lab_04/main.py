from tkinter import *

from functions_answer import *
from interface import *
from constants import *
from ellipse import *
from circle import *
from draw import *


def click(figure_selection, method, entry_center, entry_radius, entry_half_shafts, canvas_class):
    print(entry_radius.get())

    center = get_two_answer(entry_center.get())
    if center[0] == FALSE:
        return

    if figure_selection.get() == CIRCLE:
        radius = int_answer(entry_radius.get())
        if radius == FALSE:
            return
        draw_circle(canvas_class, method.get(), center, radius)
    else:
        axis = get_two_answer(entry_half_shafts.get())
        if axis[0] == FALSE:
            return
        draw_ellipse(canvas_class, method.get(), center, axis)


def main():
    color_line = ((0.0, 0.0, 0.0), '#000000')
    root = Tk()
    settings_interface(root, "1200x800", "Лабораторная работа №4")

    canvas_class = paint_class(root)

    create_button("Выбрать цвет отрезка",
                  canvas_class.choose_color_line, [1000, 25])
    create_button("Рисовать фоновым цветом",
                  canvas_class.draw_color_background, [1000, 60])

    create_label(root, "Рисуем:", [1000, 100])
    figure_selection = selection(2, CHOICE, [1000, 125])

    create_label(root, "Алгоритм:", [1000, 200])
    method = selection(5, ALGORITHMS, [1000, 225])

    create_label(root, "Центр:", [1000, 375])
    entry_center = create_entry(root, [1000, 400])

    create_label(root, "Радиус:", [1000, 425])
    entry_radius = create_entry(root, [1000, 450])

    create_label(root, "Полуоси:", [1000, 475])
    entry_half_shafts = create_entry(root, [1000, 500])

    create_button("Нарисовать", lambda arg1=figure_selection, arg2=method, arg3=entry_center,
                  arg4=entry_radius, arg5=entry_half_shafts, arg6=canvas_class: click(arg1, arg2, arg3, arg4, arg5, arg6), [1000, 550])

    create_button("Стереть всё", canvas_class.clear_all, [1000, 775])

    root.mainloop()


if __name__ == "__main__":
    main()
