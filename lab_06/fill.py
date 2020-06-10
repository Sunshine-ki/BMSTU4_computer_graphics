from time import time

from functions_answer import get_two_answer
from interface import print_info
from stack import stack_class
from fill_delay import *
from constants import *


def find_pixel(stack, canvas_class, x_right, x, y):
    # Ищем новый затравочный пиксель.
    while x <= x_right:
        # Флаг - признак нахождения нового затравочного пикселя.
        flag = False
        # Пока цвет текущего пикселя не равен цвету заполнения и не равен граничному цвету и x <= x_right
        while canvas_class.compare_color_line(x, y) and canvas_class.compare_color_fill(x, y) \
                and x <= x_right:
            # Нашли затравочный пиксель.
            if flag == False:
                flag = True
            x += 1

        # Если нашли новый пиксель, то помещаем его в стек.
        if flag:
            if x == x_right and canvas_class.compare_color_line(x, y) and \
                    canvas_class.compare_color_fill(x, y):
                stack.push([x, y])
            else:
                stack.push([x - 1, y])
            flag = False

        # Продолжаем проверку (Если интервал был прерван)
        x_temp = x
        while not canvas_class.compare_color_line(x, y) or \
                not canvas_class.compare_color_fill(x, y) and x < x_right:
            x += 1

        if x == x_temp:
            x += 1


def fill_right(canvas_class, x, y):
    # Пока что цвет пиксела не равен цвету границы
    while canvas_class.img.get(round(x), round(y)) != canvas_class.color_line[0]:
        # Отрисовываем пиксель
        canvas_class.draw_pixel((x, y))
        # Увеличиваем x (Идем вправо)
        x += 1
    # Возвращаем x - 1
    # Т.к. после цикла пиксель с координатами (x, y)
    # Будет равен цвету границы, а нам нужно взять
    # Крайний справа пиксель, т.е. пиксель,
    # Который находится справа от границы.
    return x - 1
# if canvas_class.check_borders((x, y)):
#     return


def fill_left(canvas_class, x, y):
    # Пока что цвет пиксела не равен цвету границы
    while canvas_class.img.get(round(x), round(y)) != canvas_class.color_line[0]:
        # Отрисовываем пиксель
        canvas_class.draw_pixel((x, y))
        # Уменьшаем x (Идем влево)
        x -= 1
    # Возвращаем x + 1
    # Т.к. нам нужен крайний слева пиксель.
    return x + 1


def fill(canvas_class, start_point):
    # Создаем стек и кладем в него затравочную точку.
    stack = stack_class(start_point)

    # Пока что стек не пуст
    while not stack.is_empty():
        # Достаем из стека новый затравочный пиксель.
        x, y = stack.pop()
        # Отрисовываем его.
        canvas_class.draw_pixel((x, y))
        # Заполняем все пиксели справа от затравочной точки до того момента,
        # Пока что не встретим пиксель с цветом границы.
        # В переменную x_right запоминаем крайний парвый пиксель.
        x_right = fill_right(canvas_class, x + 1, y)
        # Заполняем все пиксели слева от затравочной точки до того момента,
        # Пока что не встретим пиксель с цветом границы.
        # В переменную x_left запоминаем крайний левый пиксель.
        x_left = fill_left(canvas_class, x - 1, y)
        # На строке выше в диапазоне от x_left <= x <= x_right
        # Ищем новые затравочные пиксели и помещаем их в стек.
        find_pixel(stack, canvas_class, x_right, x_left, y + 1)
        # На строке ниже в диапазоне от x_left <= x <= x_right
        # Ищем новые затравочные пиксели и помещаем их в стек.
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
