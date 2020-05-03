from constants import *

from test import *


def multiplication_code(code1, code2):  # scalar_product
    result = 0
    for i in range(len(code1)):
        result += code1[i] * code2[i]
    return result


def sum_code(code):
    result_sum = 0
    for c in code:
        result_sum += c
    return result_sum


def create_code(point, rectangle):
    result_list = [0, 0, 0, 0]
    # print("point, rectangle = ", point, rectangle)

    result_list[0] = 1 if point[X] < rectangle[LEFT] else 0
    result_list[1] = 1 if point[X] > rectangle[RIGHT] else 0
    # Чуть иначе для Y (Не так, как в конспекте, потому что у нас ось Y направлена вниз).
    result_list[2] = 1 if point[Y] > rectangle[DOWN] else 0
    result_list[3] = 1 if point[Y] < rectangle[UP] else 0

    # print("result_list = ", result_list, "sum_code = ", sum_code(result_list))
    return result_list


def is_visible(code_1, code_2, rectangle):
    """Видимость:
            1 = видимый
            0 = частично видимый
            -1 = невидимый"""
    # code_1 = create_code([start[X], start[Y]], rectangle)
    # code_2 = create_code([end[X], end[Y]], rectangle)

    if not sum_code(code_1) and not sum_code(code_2):
        return VISIBLE_LINE

    if multiplication_code(code_1, code_2) != 0:
        return INVISIBLE_LINE

    return PARTLY_VISIBLE_LINE


def cohen_sutherland(line, rectangle):
    # Возвращает концы видимого отрезка.
    # Если отрезок невидим, то возвращает INVISIBLE_LINE
    """
    flag - Положение отрезка:
    1 = общего положения
    0 = горизонтальный
    -1 = вертикальный
    """
    # Изначально считаем, что отрезок общего положения.
    flag, m = NORMAL_LINE, 1
    # Проверка на то, что отрезок вертикальный.
    if line[X1] - line[X2] == 0:
        flag = VERTICAL_LINE
    else:
        # Если отрезок не вертикальный, то вычисляем тангенс.
        m = (line[Y2] - line[Y1]) / (line[X2] - line[X1])
        # Проверка на то, что отрезок горизонтальный.
        if m == 0:
            flag = HORIZONTAL_LINE

    # Итерируемся по 4 сторонам отсекателя
    # В порядке: (x_левое, x_правое, y_нижнее, y_верхнее)
    for i in range(4):
        # Формируем четырехразрядный код начала отрезка.
        code_1 = create_code([line[X1], line[Y1]], rectangle)
        # Формируем четырехразрядный код конца отрезка.
        code_2 = create_code([line[X2], line[Y2]], rectangle)
        # Определяем видимость отрезка.
        vis = is_visible(code_1, code_2, rectangle)
        # Если отрезок видимый, возвращаем его координаты (начало и конец).
        if vis == VISIBLE_LINE:
            return line
        # Если отрезок невидимый возвращаем признак невидимости.
        elif vis == INVISIBLE_LINE:
            return INVISIBLE_LINE

        # Проверяем пересечение отрезка и стороны отсекателя.
        # До этого момента не дойдет отрезок, у которого две
        # координаты по одну сторону, потому что выше мы это обработали.
        # Т.е. в данном случае может могут быть только
        # Такие значения code_1[i] и code_2[i]: 0 и 1, 1 и 0, 0 и 0
        # 1 и 0, 0 и 1 - означает, что данный отрезок пересекает
        # Данную сторону отсекателя (Т.е. одна его сторона находится
        # По невидимую сторону, а вторая по видимую => есть
        # Пересечение с данной стороной) - это то, что нам нужно.
        # 0 и 0 - означает обратное => отрезок ее не пересекает.
        if code_1[i] == code_2[i]:
            continue

        # Т.к. мы собираемся искать пересечение
        # Прямой и стороны отсекателя мы должны будем после
        # Того, как найдем данное пересечение
        # Присвоить одной вершине отрезка найденное пересечение.
        # Чтобы корректной вершине присвоить пересечение
        # Мы должны проверить, что данная вершина находится по
        # Невидимую сторону стороны отсекателя. Если это не так
        # То поменять местами. Если данную проверку не произвести (И обмен),
        # То получится, что после того, как мы найдем пересечение
        # Мы можем присвоить вершине, которая и так является видимой, а та
        # Вершина, которая находилась вне отсекателя так там и останется.
        # Т.е. вместо того, чтобы отбросить невидимую часть отрезка
        # Мы можем (Если не произведем данный обмен) отбросить видимую часть.
        if not code_1[i]:
            line[X1], line[Y1], line[X2], line[Y2] = line[X2], line[Y2], line[X1], line[Y1]

        # Если не вертикальная линия.
        if flag != VERTICAL_LINE:
            # Т.к. rectangle представлен данном виде:
            # (x_левое, x_правое, y_нижнее, y_верхнее)
            # Это значит, что при i<2 мы ищем пересечение
            # Либо с x_левой либо с x_правой.
            if i < 2:
                # Находим пересечение.
                line[Y1] = m * (rectangle[i] - line[X1]) + line[Y1]
                # Мы точно знаем, что раз есть пересечение,
                # То координата x будет соответствовать x_левому или x_правому
                # В зависимости от того, с какой стороной
                # Мы на данный момент работаем.
                line[X1] = rectangle[i]
                continue
            else:
                line[X1] = (1 / m) * (rectangle[i] - line[Y1]) + line[X1]
        line[Y1] = rectangle[i]

    return line


def find_solution(line_list, rectangle):
    result_list = list()

    for i in range(len(line_list)):
        res = cohen_sutherland(line_list[i], rectangle)
        if res != INVISIBLE_LINE:
            result_list.append(res)

    return result_list


def solution_wrapper(canvas_class, line_list, contour):
    result_list = find_solution(line_list, contour)
    # А если точка, а не линия?
    # А если нет линий, удовлетворяющих условию?
    for i in range(len(result_list)):
        canvas_class.draw_line(result_list[i])
