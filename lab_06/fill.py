from time import time

from functions_answer import get_two_answer
from interface import print_info
from stack import stack_class
from fill_delay import *
from constants import *


def find_pixel(stack, canvas_class, x_right, x, y):
    while x <= x_right:
        flag = False
        while canvas_class.compare_color_line(x, y) and canvas_class.compare_color_fill(x, y):
            if flag == 0:
                flag = 1
            x += 1

        if flag:
            if x == x_right and canvas_class.compare_color_line(x, y) and \
                    canvas_class.compare_color_fill(x, y):
                stack.push([x, y])
            else:
                stack.push([x - 1, y])
            flag = 0

        # Продолжаем проверку (Если интервал был прерван)
        x_temp = x
        while not canvas_class.compare_color_line(x, y) and \
                not canvas_class.compare_color_fill(x, y) and x < x_right:
            x += 1

        if x == x_temp:
            x += 1


def fill_right(canvas_class, x, y):
    while canvas_class.img.get(round(x), round(y)) != canvas_class.color_line[0]:
        canvas_class.draw_pixel((x, y))
        x += 1
        # if canvas_class.check_borders((x, y)):
        #     return
    return x - 1


def fill_left(canvas_class, x, y):
    while canvas_class.img.get(round(x), round(y)) != canvas_class.color_line[0]:
        canvas_class.draw_pixel((x, y))
        x -= 1
        # if canvas_class.check_borders((x, y)):
        #     return
    return x + 1


def fill(canvas_class, start_point):
    # Создаем стек и кладем в него затравочную точку.
    stack = stack_class(start_point)

    while not stack.is_empty():
        point = stack.pop()

        x, y = point[0], point[1]

        canvas_class.draw_pixel((x, y))
        x_right = fill_right(canvas_class, x + 1, y)
        x_left = fill_left(canvas_class, x - 1, y)

        find_pixel(stack, canvas_class, x_right, x_left, y + 1)
        find_pixel(stack, canvas_class, x_right, x_left, y - 1)


def fill_delay(canvas_class, start_point):
    # Создаем стек и кладем в него затравочную точку.
    stack = stack_class(start_point)
    # print(stack)

    while not stack.is_empty():
        point = stack.pop()

        x, y = point[0], point[1]

        canvas_class.draw_pixel((x, y))
        x_right = fill_right_delay(canvas_class, x + 1, y)
        x_left = fill_left_delay(canvas_class, x - 1, y)

        find_pixel(stack, canvas_class, x_right, x_left, y + 1)
        find_pixel(stack, canvas_class, x_right, x_left, y - 1)


def fill_wrapper(canvas_class, start_point, flag=False):
    start_point = get_two_answer(start_point.get())
    if start_point[0] == FALSE:
        return

    if not flag:
        time_start = time()
        fill(canvas_class, start_point)
        print_info(f"Время заполнения: {round(time() - time_start, 4)} ")
    else:
        fill_delay(canvas_class, start_point)


#_____________________________________________#
#  ПРОСТОЙ АЛГОРИТМ #
# def fill(canvas_class, start_point):
#     # Создаем стек и кладем в него затравочную точку.
#     stack = [start_point]

#     while len(stack):
#         point = stack.pop()

#         if canvas_class.check_borders(point):
#             return

#         canvas_class.draw_pixel(point)

#         if canvas_class.compare_color(point[0], point[1] + 1):
#             stack.append((point[0], point[1] + 1))

#         if canvas_class.compare_color(point[0], point[1] - 1):
#             stack.append((point[0], point[1] - 1))

#         if canvas_class.compare_color(point[0] + 1, point[1]):
#             stack.append((point[0] + 1, point[1]))

#         if canvas_class.compare_color(point[0] - 1, point[1]):
#             stack.append((point[0] - 1, point[1]))
