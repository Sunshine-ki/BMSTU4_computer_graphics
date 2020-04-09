from math import fabs

from functions_answer import get_two_answer
from constants import *


def sign(a):
    if a == 0:
        return 0
    return a / abs(a)


def bresenham_int(canvas_class, start, stop, lst):
    dx = stop[0] - start[0]
    dy = stop[1] - start[1]
    x, y = start[0], start[1]
    sx, sy = sign(dx), sign(dy)
    dx = fabs(dx)
    dy = fabs(dy)

    swap = 0

    if dy > dx:
        swap = 1
        dx, dy = dy, dx

    e = 2 * dy - dx

    for _ in range(int(dx + 1)):

        canvas_class.print_pixel(int(x), int(y))
        if e >= 0:
            if swap == 0:
                y += sy
                if start[1] != stop[1] and [int(x), int(y)] not in lst:
                    lst.append([int(x), int(y)])
            else:
                x += sx
            e -= (2 * dx)

        if e < 0:
            if swap == 0:
                x += sx
            else:
                y += sy
                if start[1] != stop[1] and [int(x), int(y)] not in lst:
                    lst.append([int(x), int(y)])
            e += (2 * dy)


def fill(canvas_class, start_point, flag=False):
    start_point = get_two_answer(start_point.get())
    if start_point[0] == FALSE:
        return

    # Создаем стек и кладем в него затравочную точку.
    stack = [start_point]

    while len(stack):
        point = stack.pop()

        if canvas_class.check_borders(point):
            return

        if flag:
            canvas_class.canvas.after(
                1, canvas_class.draw_pixel(point))
            canvas_class.canvas.update()
        else:
            canvas_class.draw_pixel(point)

        if canvas_class.compare_color(point[0], point[1] + 1):
            stack.append((point[0], point[1] + 1))

        if canvas_class.compare_color(point[0], point[1] - 1):
            stack.append((point[0], point[1] - 1))

        if canvas_class.compare_color(point[0] + 1, point[1]):
            stack.append((point[0] + 1, point[1]))

        if canvas_class.compare_color(point[0] - 1, point[1]):
            stack.append((point[0] - 1, point[1]))
