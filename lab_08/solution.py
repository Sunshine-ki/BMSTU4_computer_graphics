from constants import *

from test import *


def find_solution(line_list, rectangle):
    result_list = list()

    for i in range(len(line_list)):
        pass
        # res = cohen_sutherland(line_list[i], rectangle)
        # if res != INVISIBLE_LINE:
        #     result_list.append(res)

    return result_list


def solution_wrapper(canvas_class, line_list, contour):
    result_list = find_solution(line_list, contour)

    for i in range(len(result_list)):
        canvas_class.draw_line(result_list[i])
