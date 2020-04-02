from tkinter import *


def print_pixel(canvas, color_line, x, y):
    canvas.create_line(round(x), round(y), round(
        x), round(y) + 1, width=1, fill=color_line[1])


def draw_figure(canvas, color_line, list_points):
    for i in range(len(list_points)):
        print_pixel(canvas, color_line, list_points[i][0], list_points[i][1])
