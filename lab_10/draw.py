from tkinter import *
from tkinter import colorchooser

from functions_answer import get_two_answer
from interface import print_error
from constants import *


class paint_class():
    canvas = None

    def __init__(self, root):
        self.canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.place(x=0, y=0)
        self.initial_parameters_canvas()

    def clear_all(self):
        self.canvas.delete(ALL)
        self.initial_parameters_canvas()

    def initial_parameters_canvas(self):
        self.canvas.create_text(
            10, 10, text="Экран 800x800", font=FONT)

    def create_pixel(self, x, y, color="white"):
        x *= SCALE
        y *= SCALE
        x += WIDTH // 2
        y = HEIGHT // 2 - y

        self.canvas.create_line(round(x), round(y), round(
            x), round(y) + 1, fill=color)

    def draw_line(self, begin, end, color="white"):
        begin, end = coordinate_transformations(begin, end)
        self.canvas.create_line(begin[0], begin[1], end[0], end[1], fill=color)


def coordinate_transformations(begin, end):
    for i in range(2):
        begin[i] *= SCALE
        end[i] *= SCALE

    begin[0] += WIDTH // 2
    end[0] += WIDTH // 2
    begin[1] = HEIGHT // 2 - begin[1]
    end[1] = HEIGHT // 2 - end[1]
    return begin, end
