
LEFT = 0
RIGHT = 1
DOWN = 2
UP = 3

X = 0
Y = 1

VISIBLE_LINE = 1
PARTLY_VISIBLE_LINE = 0
INVISIBLE_LINE = -1


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


def is_visible(start, end, rectangle):
    """Видимость:
            1 = видимый
            0 = частично видимый
            -1 = невидимый"""
    code_1 = create_code([start[X], start[Y]], rectangle)
    code_2 = create_code([end[X], end[Y]], rectangle)

    if not sum_code(code_1) and not sum_code(code_2):
        return VISIBLE_LINE

    if multiplication_code(code_1, code_2) != 0:
        return INVISIBLE_LINE

    return PARTLY_VISIBLE_LINE


def cohen_sutherland(line, rectangle):
    # Возвращает концы видимого отрезка.
    # Если отрезок невидим, то возвращает INVISIBLE_LINE
    vis = is_visible([line[0], line[1]], [line[2], line[3]], rectangle)
    if vis == VISIBLE_LINE:
        return line
    elif vis == INVISIBLE_LINE:
        return INVISIBLE_LINE

    print("Частично видимая")
    return PARTLY_VISIBLE_LINE


def find_solution(line_list, rectangle):
    result_list = list()

    for i in range(len(line_list)):
        res = cohen_sutherland(line_list[i], rectangle)
        if res != INVISIBLE_LINE:
            result_list.append(res)

    return result_list


def solution_wrapper(canvas_class, line_list, contour):
    result_list = find_solution(line_list, contour)
    # А если точка, а не линяя?
    # А если нет линий, удовлетворяющих условию?
    for i in range(len(result_list)):
        canvas_class.draw_line(result_list[i])
