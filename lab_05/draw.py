from tkinter import *
from tkinter import colorchooser
from constants import *

from functions_answer import get_two_answer
from interface import print_error
from fill import find_intersections


class paint_class():

    color_line = ((0.0, 0.0, 0.0), '#000000')
    canvas = None
    img = None

    def __init__(self, root):
        self.canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="lavender")
        self.canvas.place(x=0, y=0)

        self.img = PhotoImage(width=WIDTH, height=HEIGHT)
        self.canvas.create_image(
            (WIDTH/2, HEIGHT/2), image=self.img, state="normal")
        self.canvas.create_text(
            10, 10, text="Экран 800x800", font="Verdana 12")
        self.img.put(color_bg[1], to=(0, 0, WIDTH, HEIGHT))

    def clear_all(self):
        self.canvas.delete(ALL)

        self.img = PhotoImage(width=WIDTH, height=HEIGHT)
        self.canvas.create_image(
            (WIDTH/2, HEIGHT/2), image=self.img, state="normal")
        self.canvas.create_text(
            10, 10, text="Экран 800x800", font="Verdana 12")
        self.img.put(color_bg[1], to=(0, 0, WIDTH, HEIGHT))

    def reverse_pixel(self, x, y):
        # print("ЦВЕТ = ", self.img.get(round(x), round(y)))
        color_pixel = self.img.get(round(x), round(y))
        # print(color_pixel, self.color_line[0])
        if color_pixel == color_bg[0]:
            self.img.put(self.color_line[1], (round(x), round(y)))
            # print("Реверснуть на цвет линии")
        elif color_pixel == self.color_line[0]:
            self.img.put(color_bg[1], (round(x), round(y)))
            # print("Реверснуть на цвет фона")

    def print_line(self, start, stop):
        self.canvas.create_line(
            start[0], start[1], stop[0], stop[1], fill=self.color_line[1], tags="user_line")

    def print_pixel(self, x, y):
        self.canvas.create_line(round(x), round(y), round(
            x), round(y) + 1, width=1, fill=self.color_line[1])  # , tags="user_line")
        # self.img.put(self.color_line[1], (round(x), round(y)))

    def choose_color_line(self):
        temp = list(colorchooser.askcolor(title="Выбор цвета"))
        new_color = (tuple([int(i) for i in temp[0]]), temp[1])
        # print("color_line = ", new_color)
        self.color_line = new_color
        self.canvas.itemconfig("user_line", fill=self.color_line[1])


def lock(points_list, canvas_class, list_box, lst):
    if len(points_list[-1]) > 1:
        start = points_list[-1][-1]
        stop = points_list[-1][0]

        find_intersections(canvas_class, start, stop, lst)
        canvas_class.print_line(start, stop)

        points_list.append(list())
        list_box.insert(END, "_" * 8)
        # print(lst)


def add_point(points_list, point, canvas_class, list_box, lst):
    if point in points_list[-1]:
        print_error("Такая точка уже имеется в данном многоугольнике!")
        return
    points_list[-1].append(point)

    list_box.insert(END, point)

    # print(points_list[-1])

    if len(points_list[-1]) > 1:
        start = points_list[-1][-2]
        stop = points_list[-1][-1]

        find_intersections(canvas_class, stop, start, lst)
        canvas_class.print_line(start, stop)

    elif len(points_list[-1]) == 1:
        canvas_class.print_pixel(points_list[-1][0][0], points_list[-1][0][1])
        # if [points_list[-1][0][0], points_list[-1][0][1]] not in lst:
        # lst.append([points_list[-1][0][0], points_list[-1][0][1]])


def add_point_click(event, canvas_class, list_box, points_list, lst):
    add_point(points_list, [event.x, event.y], canvas_class, list_box, lst)


def add_point_entry(point_coordinates, list_box, canvas_class, points_list, lst):
    point = list(get_two_answer(point_coordinates.get()))
    if point[0] == FALSE:
        return
    add_point(points_list, point, canvas_class, list_box, lst)


def clear(canvas_class, list_box, points_list, lst):
    canvas_class.clear_all()

    list_box.delete(1, list_box.size())

    for i in range(len(points_list) - 1, -1, -1):
        del points_list[i]

    for i in range(len(lst) - 1, -1, -1):
        del lst[i]

    points_list.append([])
