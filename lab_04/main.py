from tkinter import *

from interface import *
from constants import *
from draw import *
from click import *


def main():
    root = Tk()
    settings_interface(root, "1200x800", "Лабораторная работа №4")

    canvas_class = paint_class(root)

    create_button("Выбрать цвет",
                  canvas_class.choose_color_line, [1000, 25])
    create_button("Рисовать фоновым цветом",
                  canvas_class.draw_color_background, [1000, 60])

    create_label(root, "Рисуем:", [1000, 100])
    figure_selection = selection(2, CHOICE, [1000, 125])

    create_label(root, "Алгоритм:", [1000, 200])
    method = selection(5, ALGORITHMS, [1000, 225])

    create_label(root, "Центр:", [1000, 355])
    entry_center = create_entry(root, [1000, 380])

    create_label(root, "Радиус:", [1000, 405])
    entry_radius = create_entry(root, [1000, 430])

    create_label(root, "Полуоси:", [1000, 455])
    entry_half_shafts = create_entry(root, [1000, 480])

    create_button("Нарисовать", lambda arg1=figure_selection, arg2=method, arg3=entry_center,
                  arg4=entry_radius, arg5=entry_half_shafts, arg6=canvas_class: click(arg1, arg2, arg3, arg4, arg5, arg6), [1000, 525])

    create_label(root, "Центр:", [1000, 560])
    entry_center_concentric = create_entry(root, [1000, 580])
    create_label(root, "r1:", [900, 610])
    create_label(root, "r2:", [1100, 610])
    entry_r1 = create_entry(root, [900, 630])
    entry_r2 = create_entry(root, [1100, 630])
    create_label(root, "Шаг:", [900, 660])
    create_label(root, "Количество:", [1100, 660])
    entry_step = create_entry(root, [900, 680])
    entry_count = create_entry(root, [1100, 680])

    create_button("Нарисовать спектр", lambda arg1=figure_selection, arg2=method, arg3=[entry_center_concentric, entry_r1,
                                                                                        entry_r2, entry_step, entry_count],
                  arg4=canvas_class: click_concentric(arg1, arg2, arg3, arg4), [1000, 715])

    create_button("Стереть всё", canvas_class.clear_all, [1000, 775])

    root.mainloop()


if __name__ == "__main__":
    main()
