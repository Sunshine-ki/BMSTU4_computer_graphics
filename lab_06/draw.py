from tkinter import *
from tkinter import colorchooser

from interface import print_error
from constants import *


class paint_class():
    color_fill = COLOR_FILL_INIT
    color_line = COLOR_LINE
    canvas = None
    img = None

    def __init__(self, root):
        self.canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.place(x=0, y=0)

        self.img = PhotoImage(width=WIDTH, height=HEIGHT)
        self.canvas.create_image(
            (WIDTH/2, HEIGHT/2), image=self.img, state="normal")
        self.canvas.create_text(
            10, 10, text="Экран 800x800", font=FONT)
        self.img.put(COLOR_BG[1], to=(0, 0, WIDTH, HEIGHT))

    def clear_all(self):
        self.canvas.delete(ALL)

        self.img = PhotoImage(width=WIDTH, height=HEIGHT)
        self.canvas.create_image(
            (WIDTH/2, HEIGHT/2), image=self.img, state="normal")
        self.canvas.create_text(
            10, 10, text="Экран 800x800", font=FONT)
        self.img.put(COLOR_BG[1], to=(0, 0, WIDTH, HEIGHT))

    def check_borders(self, point):
        if point[0] <= 0 or point[0] >= WIDTH:
            print_error("Выход за границы экрана!")
            return True
        if point[1] <= 0 or point[1] >= HEIGHT:
            print_error("Выход за границы экрана!")
            return True

        return False

    def draw_pixel(self, coordinates):
        self.img.put(self.color_fill[1], (round(
            coordinates[0]), round(coordinates[1])))

    def print_pixel(self, x, y):
        self.img.put(self.color_line[1], (round(x), round(y)))

    def choose_color_line(self):
        temp = list(colorchooser.askcolor(title="Выбор цвета"))
        new_color = (tuple([int(i) for i in temp[0]]), temp[1])

        if temp[1] == self.color_line[1]:
            print_error("Цвет отрезка и заполнения должны отличаться!")

        self.color_fill = new_color
        # self.canvas.itemconfig("user_line", fill=self.color_line[1])

    def in_canvas(self, event):
        self.canvas.delete("coordinates")
        self.canvas.create_text(event.x + 45, event.y - 15,  text=f"({event.x}, {event.y})",
                                font=FONT, tags="coordinates")

    def compare_color_line(self, x, y):
        return self.img.get(round(x), round(y)) != self.color_line[0]

    def compare_color_fill(self, x, y):
        return self.img.get(round(x), round(y)) != self.color_fill[0]
