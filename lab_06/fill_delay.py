from stack import *


def fill_right_delay(canvas_class, x, y):
    while canvas_class.img.get(round(x), round(y)) != canvas_class.color_line[0]:
        canvas_class.canvas.after(
            0, canvas_class.draw_pixel((x, y)))
        canvas_class.canvas.update()
        x += 1
    return x - 1


def fill_left_delay(canvas_class, x, y):
    while canvas_class.img.get(round(x), round(y)) != canvas_class.color_line[0]:
        canvas_class.canvas.after(
            0, canvas_class.draw_pixel((x, y)))
        canvas_class.canvas.update()
        x -= 1

    return x + 1
