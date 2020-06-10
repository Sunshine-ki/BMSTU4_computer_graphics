from tkinter import *
from tkinter import colorchooser

from functions_answer import get_two_answer
from interface import print_error
from constants import *


class paint_class():
    canvas = None
    flag = False
    start = False
    stop = False

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
        self.canvas.create_line(0, 0, 0, 0, tags="line_rectangle")

        # self.canvas.create_rectangle(
        # 0, 0, 0, 0, tags="rectangle_temp", outline="black")
        # self.canvas.create_rectangle(
        # 0, 0, 0, 0, tags="contour", outline="black")

    def draw_line(self, coords, color="blue", w=1):
        self.canvas.create_line(
            coords[0], coords[1], coords[2], coords[3], fill=color, width=w)

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

        self.canvas.create_line(
            self.start[0], self.start[1], event.x, event.y, fill="red")
        line_list[-1].append([self.start[0], self.start[1], event.x, event.y])

        self.flag = False
        self.start = False
        # print(line_list)

    def Motion(self, event):
        if self.start:
            self.canvas.coords(
                "line_temp", self.start[0], self.start[1], event.x, event.y)

    def Motion_rectangle(self, event):
        if self.stop:
            self.canvas.coords("line_rectangle",
                               self.stop[0], self.stop[1], event.x, event.y)
            # print(self.start[0], self.start[1],event.x, event.y)

    def keyPress_rectangle(self, event):
        self.start = self.stop
        self.stop = [event.x, event.y]
        # self.flag = True

    def keyRelease_rectangle(self, event, lst, color):
        if self.start:
            self.canvas.create_line(
                self.start[0], self.start[1], self.stop[0], self.stop[1], fill=color)

            lst[-1].append([self.start[0], self.start[1],
                            self.stop[0], self.stop[1]])
            # print(self.start, self.stop)

    def keySpace_rectangle(self, event, lst, color):
        if (len(lst[-1]) > 1):
            self.canvas.create_line(
                lst[-1][-1][2], lst[-1][-1][3], lst[-1][0][0], lst[-1][0][1], fill=color)

            lst[-1].append([lst[-1][-1][2], lst[-1][-1][3],
                            lst[-1][0][0], lst[-1][0][1]])
            lst.append([])
            # print(lst)
            self.canvas.coords("line_rectangle", 0, 0, 0, 0)
            self.flag = False
            self.start = False
            self.stop = False


def close_contour(cutter, contour, lst, canvas_class, selection):  # cutter отсекатель 0
    if len(lst) >= 2:
        choice = selection.get()
        color = "blue"
        if choice == 0:
            color = "red"
        canvas_class.canvas.create_line(
            lst[-1][0], lst[-1][1], lst[0][0], lst[0][1], fill=color)
        # print(selection.get())
        if choice == 1:
            for i in range(len(lst) - 1):
                contour[-1].append([lst[i][0], lst[i][1],
                                    lst[i+1][0], lst[i+1][1]])
            contour[-1].append([lst[-1][0], lst[-1][1], lst[0][0], lst[0][1],
                                ])
            contour.append([])
        elif choice == 0:
            for i in range(len(lst) - 1):
                cutter[-1].append([lst[i][0], lst[i][1],
                                   lst[i+1][0], lst[i+1][1]])
            cutter[-1].append([lst[-1][0], lst[-1][1], lst[0][0], lst[0][1]])
            cutter.append([])

    # print("contour = ", contour)
    # print("cutter = ", cutter)

    for i in range(len(lst) - 1, -1, -1):
        del lst[i]

    # print(lst)


def add_contour(lst, start, canvas_class, selection):
    choice = selection.get()
    color = "blue"
    if choice == 0:
        color = "red"
    start = get_two_answer(start.get())
    if start[0] == FALSE:
        return
    lst.append([start[0], start[1]])
    if len(lst) >= 2:
        canvas_class.canvas.create_line(
            lst[-1][0], lst[-1][1], lst[-2][0], lst[-2][1], fill=color)


def add_line(lst, start, stop, canvas):
    # if len(lst) >= 10:
    #     print_error("Нельзя рисовать более 10 линий!")
    #     return

    start = get_two_answer(start.get())
    if start[0] == FALSE:
        return

    stop = get_two_answer(stop.get())
    if stop[0] == FALSE:
        return

    if [start[0], start[1], stop[0], stop[1]] in lst:
        print_error("Данная линяя уже имеется!")
        return

    canvas.canvas.create_line(
        start[0], start[1], stop[0], stop[1], fill="red")
    lst.append([start[0], start[1], stop[0], stop[1]])
    # print(lst)
