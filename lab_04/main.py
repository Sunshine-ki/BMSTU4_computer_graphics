from tkinter import *

from functions_answer import *
from interface import *
from constants import *
from ellipse import *
from circle import *


def click(figure_selection, method, entry_center, entry_radius, entry_half_shafts, canvas, color_line):
    print(entry_radius.get())
    radius = int_answer(entry_radius.get())
    if radius == FALSE:
        return

    center = get_two_answer(entry_center.get())
    if center[0] == FALSE:
        return

    if figure_selection.get() == CIRCLE:
        draw_circle(canvas, method.get(), center, radius, color_line)
    else:
        axis = get_two_answer(entry_half_shafts.get())
        if axis[0] == FALSE:
            return
        draw_ellipse(canvas, method.get(), center, radius, axis, color_line)


def clear_all(canvas):
    canvas.delete(ALL)
    canvas.create_text(10, 10, text="Экран 800x800", font="Verdana 12")


def main():
    color_line = ((0.0, 0.0, 0.0), '#000000')
    root = Tk()
    settings_interface(root, "1200x800", "Лабораторная работа №4")

    canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
    canvas.place(x=0, y=0)
    canvas.create_text(10, 10, text="Экран 800x800", font="Verdana 12")

    create_button("Выбрать цвет отрезка",
                  lambda arg1=color_line: choose_color_line(arg1), [1000, 25])
    create_button("Рисовать фоновым цветом",
                  lambda arg1=color_line: draw_color_background(arg1), [1000, 60])

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
                  arg4=entry_radius, arg5=entry_half_shafts, arg6=canvas, arg7=color_line: click(arg1, arg2, arg3, arg4, arg5, arg6, arg7), [1000, 550])

    create_button(
        "Стереть всё", lambda arg1=canvas: clear_all(arg1), [1000, 775])

    root.mainloop()


if __name__ == "__main__":
    main()
