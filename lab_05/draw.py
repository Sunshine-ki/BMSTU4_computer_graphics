from tkinter import *
from tkinter import colorchooser

from constants import *


class paint_class():

    color_line = ((0.0, 0.0, 0.0), '#000000')
    canvas = None
    img = None

    def __init__(self, root):
        self.canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
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

    def print_pixel(self, x, y):
        self.canvas.create_line(round(x), round(y), round(
            x), round(y) + 1, width=1, fill=self.color_line[1], tags="user_line")
        # self.img.put(self.color_line[1], (round(x), round(y)))

    def choose_color_line(self):
        temp = list(colorchooser.askcolor(title="Выбор цвета"))
        new_color = (tuple([int(i) for i in temp[0]]), temp[1])
        # print("color_line = ", new_color)
        self.color_line = new_color
        self.canvas.itemconfig("user_line", fill=self.color_line[1])
