from tkinter import *
from tkinter import colorchooser

from functions_answer import get_two_answer
from interface import print_error
from constants import *


# class point_class():
#     x, y = 0, 0

#     def __init__(self, x, y):
#         self.x, self.y = x, y


# class line_class():
#     start, end = point_class(0, 0), point_class(0, 0)

#     def __init__(self, x1, y1, x2, y2):
#         self.start = point_class(x1, y1)
#         self.end = point_class(x2, y2)


class paint_class():
    canvas = None
    flag = False
    start = False

    def __init__(self, root):
        self.canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.place(x=0, y=0)
        self.initial_parameters_canvas()

    def clear_all(self):
        self.canvas.delete(ALL)
        self.initial_parameters_canvas()

    def initial_parameters_canvas(self):
        self.canvas.create_text(
            10, 10, text="Экран 800x800", font=FONT)
        self.canvas.create_line(0, 0, 0, 0, tags="line_temp")
        self.canvas.create_rectangle(
            0, 0, 0, 0, tags="rectangle_temp", outline="black")
        self.canvas.create_rectangle(
            0, 0, 0, 0, tags="contour", outline="black")

    def draw_line(self, coords, color="blue"):
        self.canvas.create_line(
            coords[0], coords[1], coords[2], coords[3], fill=color)

    def new_rectangle(self, start, stop):
        self.canvas.coords("contour", start[0], start[1], stop[0], stop[1])
        self.canvas.coords("rectangle_temp", 0, 0, 0, 0)

    def keyPress(self, event):
        if not self.flag:
            self.start = [event.x, event.y]
        self.flag = True

        # self.start = [event.x, event.y]

    def keyRelease(self, event, line_list):
        self.canvas.coords("line_temp", 0, 0, 0, 0)
        if len(line_list) >= 10:
            self.start = False
            self.flag = False
            print_error("Нельзя рисовать более 10 линий!")
            return

        self.canvas.create_line(
            self.start[0], self.start[1], event.x, event.y, fill="red")
        line_list.append([self.start[0], self.start[1], event.x, event.y])

        self.flag = False
        self.start = False
        # print(line_list)

    def Motion(self, event):
        if self.start:
            self.canvas.coords(
                "line_temp", self.start[0], self.start[1], event.x, event.y)

    def keyPress_rectangle(self, event):
        self.start = [event.x, event.y]
        self.flag = True

    def keyRelease_rectangle(self, event, lst):
        self.canvas.coords("line_temp", 0, 0, 0, 0)
        self.canvas.coords(
            "contour", self.start[0], self.start[1], event.x, event.y)

        for i in range(len(lst) - 1, -1, -1):
            del lst[i]

        # lst.append(self.start[0])
        # lst.append(self.start[1])
        # lst.append(event.x)
        # lst.append(event.y)
        if self.start[0] < event.x:
            lst.append(self.start[0])
            lst.append(event.x)
        else:
            lst.append(event.x)
            lst.append(self.start[0])

        if self.start[1] > event.y:
            lst.append(self.start[1])
            lst.append(event.y)
        else:
            lst.append(event.y)
            lst.append(self.start[1])

        # print(lst)

        self.flag = False
        self.start = False

    def Motion_rectangle(self, event):

        if self.start:
            self.canvas.coords("rectangle_temp",
                               self.start[0], self.start[1], event.x, event.y)

    # def check_borders(self, point):
    #     if point[0] <= 0 or point[0] >= WIDTH:
    #         print_error("Выход за границы экрана!")
    #         return True
    #     if point[1] <= 0 or point[1] >= HEIGHT:
    #         print_error("Выход за границы экрана!")
    #         return True

    #     return False


def add_contour(lst, start, stop, canvas_class):
    start = get_two_answer(start.get())
    if start[0] == FALSE:
        return

    stop = get_two_answer(stop.get())
    if stop[0] == FALSE:
        return

    if start == stop:
        print_error("Начало и конец совпадают!")
        return

    canvas_class.new_rectangle(start, stop)

    for i in range(len(lst) - 1, -1, -1):
        del lst[i]

    # lst.append(list(start))
    # lst.append(list(stop))

    # lst.append(start[0])
    # lst.append(start[1])
    # lst.append(stop[0])
    # lst.append(stop[1])

    if start[0] < stop[0]:
        lst.append(start[0])
        lst.append(stop[0])
    else:
        lst.append(stop[0])
        lst.append(start[0])

    if start[1] > stop[1]:
        lst.append(start[1])
        lst.append(stop[1])
    else:
        lst.append(stop[1])
        lst.append(start[1])

    # print(lst)


def add_line(lst, start, stop, canvas):
    if len(lst) >= 10:
        print_error("Нельзя рисовать более 10 линий!")
        return

    start = get_two_answer(start.get())
    if start[0] == FALSE:
        return

    stop = get_two_answer(stop.get())
    if stop[0] == FALSE:
        return

    # if start == stop:
    #     print_error("Начало и конец совпадают!")
    #     return

    if [start[0], start[1], stop[0], stop[1]] in lst:
        print_error("Данная линяя уже имеется!")
        return

    # canvas.draw_line(start, stop)
    canvas.canvas.create_line(
        start[0], start[1], stop[0], stop[1], fill="red")
    lst.append([start[0], start[1], stop[0], stop[1]])
    # print(lst)
