import numpy as np
from math import fabs, ceil, sqrt

from functions_answer import float_answer, get_two_answer
from draw import coordinate_transform
from interface import print_error
from functions import *
from constants import *
from rotate import *


def FindIntersection(xk, xn, yprev):
    pass


def FloatHorizon(borders_x, step_x, borders_z, step_z, canvas_class, f, angles):
    # Инициализируем начальными значениями массивы горизонтов.
    # x =   # [0,0,...,0]
    # top = {x: 0 for x in range(1, WIDTH)}
    # bottom = {x: HEIGHT for x in range(1, HEIGHT)}

    top = [HEIGHT] * WIDTH  # Верхний.
    bottom = [0] * WIDTH  # Нижний.

    x_start = borders_x[0]
    x_stop = borders_x[1]
    x_step = step_x

    z_start = borders_z[0]
    z_stop = borders_z[1]
    z_step = step_z

    # count_i = round((z_stop - z_start) / z_step + 1)
    count = ceil((x_stop - x_start) / x_step)

    i = 0
    for z in np.arange(z_stop, z_start, -z_step):
        j = 0
        for x in np.arange(x_start, x_stop, x_step):
            # Вычисления текущих и следующих значений.
            x_next = x + x_step
            y_next = f(x_next, z)
            y = f(x, z)
            x, y = rotate(x, y, z, angles)
            x_next, y_next = rotate(x_next, y_next, z, angles)

            x, y, x_next, y_next = coordinate_transform(
                [x, y], [x_next, y_next])
            # Обрабатываем левое боковое ребро.
            if not j:
                # Если очередная точка является первой точкой первой кривой
                if not i:
                    # то запомнит ее в p_b.
                    p_b = [x, y]
                else:
                    # Если очередная точка является первой точкой
                    # не первой кривой, то соединить ее с точкой p_b
                    # и запомнить ее в p_b
                    canvas_class.draw_line(p_b, [x, y])
                    p_b = [x, y]
            # Обрабатываем правое боковое ребро
            elif j == count - 1:
                # Если очередная точка является последней точкой первой кривой
                if not i:
                    # то запомнит ее в p_e.
                    p_e = [x_next, y_next]
                else:
                    canvas_class.draw_line(p_e, [x_next, y_next])
                    p_e = [x_next, y_next]

            # Если сегмент кривой видим, то изобразить его целиком.
            if (y >= bottom[x] or y <= top[x]) and (y_next >= bottom[x] or y_next
                                                    <= top[x]):
                canvas_class.draw_line([x, y], [x_next, y_next])

            # if y < top[x] and y_next > top[x_next]:
            #     dx = x_next - x
            #     dy1 = top[x_next] - top[x]
            #     dy2 = y_next - y
            #     x_inters = x - dx * (y + top[x]) / (dy1 - dy2)
            #     print(x, x_inters, x_next)

            # Если видимость сегмента кривой изменилась, то найти точку пересечения с горизонтом
            if y < top[x] and y_next > top[x_next]:
                # print("Есть такое")
                dx = x_next - x
                dy_prev = top[x_next] - top[x]
                dy_curr = y_next - y
                x_intersection = x - dx * (y - top[x]) / (dy_curr - dy_prev)
                # print(x, x_intersection, x_next)
                m_curr = (y_next - y)/dx
                y_intersection = m_curr * (x_intersection - x) + y
                # print(y, y_intersection, y_next)
                canvas_class.draw_line(
                    [x, y], [x_intersection, y_intersection])

                # print(x_intersection, y_intersection)

            # Если точка расположена выше верхнего или ниже нижнего горизонта,
            # то скорректировать массивы верхнего и нижнего горизонта.
            if y > bottom[x]:
                bottom[x] = y
            if y < top[x]:
                top[x] = y

            # Отрисовка.
            # print(x, x_next)
            # canvas_class.draw_line([x, y], [x_next, y_next])
            j += 1
        i += 1


def SolutionWrapper(choice, borders, step, angles, canvas_class):
    borders_x = get_two_answer(borders[0].get())
    if borders_x[0] == FALSE:
        return

    step_x = float_answer(step[0].get())
    if step_x == FALSE:
        return

    borders_z = get_two_answer(borders[1].get())
    if borders_z[0] == FALSE:
        return

    step_z = float_answer(step[1].get())
    if step_z == FALSE:
        return

    angle_x = float_answer(angles[0].get())
    if angle_x == FALSE:
        return

    angle_y = float_answer(angles[1].get())
    if angle_y == FALSE:
        return

    angle_z = float_answer(angles[2].get())
    if angle_z == FALSE:
        return

    f = [f1, f2, f3, f4]
    index = CHOICE.index(choice.get())

    canvas_class.clear_all()
    FloatHorizon(borders_x, step_x, borders_z, step_z,
                 canvas_class, f[index], [angle_x, angle_y, angle_z])


# x_start = -5
# x_stop = 5
# x_step = 0.5
# for x in np.arange(x_start, x_stop + x_step, x_step):
#     x_next = x + x_step + 0.1
#     y_next = f(x_next, z)
#     # print(x, f(x, z))
#     y = f(x, z)
#     x, y, a = rotateX(x, y, z, DEFAULT_ANGLE_X)
#     x, y, a = rotateY(x, y, z, DEFAULT_ANGLE_Y)

#     x_next, y_next, a = rotateX(x_next, y_next, z, DEFAULT_ANGLE_X)
#     x_next, y_next, a = rotateY(x_next, y_next, z, DEFAULT_ANGLE_Y)

#     # canvas_class.create_pixel(x, y)

#     canvas_class.draw_line([x, y], [x_next, y_next])
