from math import ceil

from functions_answer import *
from constants import *
from ellipse import *
from circle import *
from draw import *


def click(figure_selection, method, entry_center, entry_radius, entry_half_shafts, canvas_class):
    # print(entry_radius.get())
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


def click_concentric(figure_selection, method, array_entry, canvas_class):
    # [entry_center_concentric, entry_r1,
    #  entry_r2, entry_step, entry_count]
    method = method.get()
    center = get_two_answer(array_entry[0].get())
    if center[0] == FALSE:
        return

    r1 = int_answer(array_entry[1].get())
    if r1 == FALSE:
        return
    r2 = int_answer(array_entry[2].get())
    if r2 == FALSE:
        return

    if r1 < 0 or r2 < 0:
        print_error("r1 и r2 должны быть положительными")
        return
    if r1 >= r2:
        print_error("Некорректно введены r1 и r2")
        return

    flag = True
    if array_entry[3].get() == "":
        flag = False

    if flag:
        step = int_answer(array_entry[3].get())
        if step == FALSE:
            return
    else:
        count = int_answer(array_entry[4].get())
        if count == FALSE:
            return

    # print("center", center)
    # print("r1 = ", r1, "r2 = ", r2)
    # if flag:
    #     print("step = ", step)
    # else:
    #     print("count = ", count)

    if figure_selection.get() == CIRCLE:
        # print("Рисуем окружности ")
        if not flag:
            step = ceil((r2 - r1) / count)

        draw_concentric_circle(canvas_class, center,
                               method, r1, r2, step)
    else:
        # print("Рисуем эллипсы")
        if flag:
            count = int_answer(array_entry[4].get())
            if count == FALSE:
                return
        else:
            step = int_answer(array_entry[3].get())
            if step == FALSE:
                return
        draw_concentric_ellipse(canvas_class, center,
                                method, r1, r2, count, step)
