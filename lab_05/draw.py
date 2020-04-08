from tkinter import *
from tkinter import colorchooser

from constants import *


class paint_class():

    color_line = ((0.0, 0.0, 0.0), '#000000')
    canvas = None

    def __init__(self, root):
        self.canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            10, 10, text="Экран 800x800", font="Verdana 12")

        for i in range(WIDTH):
            for j in range(HEIGHT):
                self.canvas.create_line(round(i), round(j), round(
                    i), round(j) + 1, width=1, fill=color_bg, tags=str(i) + 'x' + str(j) + 'b')

    def clear_all(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(
            10, 10, text="Экран 800x800", font="Verdana 12")

    # def print_pixel_fill(self, x, y):
        # if

    def print_pixel(self, x, y):
        self.canvas.create_line(round(x), round(y), round(
            x), round(y) + 1, width=1, fill=self.color_line[1], tags='line_user')

    def draw_figure(self, list_points):
        for i in range(len(list_points)):
            self.canvas.after(10, self.print_pixel(
                list_points[i][0], list_points[i][1]))
            self.canvas.update()
            # self.print_pixel(list_points[i][0], list_points[i][1])

    def draw_oval(self, a, b, c, d):
        self.canvas.create_oval(a, b, c, d, outline=self.color_line[1])

    def choose_color_line(self):
        temp = colorchooser.askcolor(title="Выбор цвета")
        self.color_line = temp
        self.canvas.itemconfig('line_user', fill=temp[1])
        print("color_line = ", color_line)

    def draw_color_background(self):
        self.color_line = ((255, 255, 255), '#ffffff')
        print("color_line = ", color_line)

    def reverse_color(self, x, y):
        if len(self.canvas.gettags(str(x) + 'x' + str(y) + 'b')) != 0:
            self.canvas.itemconfig(str(x) + 'x' + str(y) + 'b',
                                   tags=str(x) + 'x' + str(y) + 'l', fill=color_line[1])
            return

        if len(self.canvas.gettags(str(x) + 'x' + str(y) + 'l')) != 0:
            self.canvas.itemconfig(str(x) + 'x' + str(y) + 'l',
                                   tags=str(x) + 'x' + str(y) + 'b', fill=color_bg)
            return
