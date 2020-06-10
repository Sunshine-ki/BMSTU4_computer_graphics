from math import *
from tkinter import *
import numpy as np

win_size = 1000
a = 80
b = 120


def paint_point(cordinate):
    r = 1
    t = win_size / 2
    x = cordinate[0]
    y = cordinate[1]
    canv.create_oval(x - r + t, -y - r + t,
                     x + r + t, -y + r + t, fill='black')


def paint_line(a, b):
    t = win_size / 2
    canv.create_line(a[0] + t, -a[1] + t, b[0] + t, -
                     b[1] + t, fill="black", width=3)


def x_test(t):
    return b * cos(t)


def y_test(t):
    return b * sin(t)


def func_x(t):
    return (a + b)*cos(t)-a*cos((a+b)*t/a)
    # return 160*(sin(t))**3
    # return 200 * (sin(t))**3
    # return 200 * cos(t)


def func_y(t):
    return (a+b)*sin(t)-a*sin((a+b)*t/a)
    # return 130*cos(t)-50*cos(2*t)-20*cos(3*t)-cos(4*t)
    # return 200 * (cos(t))**3
    # return 200 * sin(t)


root = Tk()

canv = Canvas(root, width=win_size, height=win_size, bg='white')
canv.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
canv.create_line(0, 500, 1000, 500, width=2, arrow=LAST)

list_point = []

for i in np.arange(0, 2 * pi * 2, 0.1):
    try:
        x = func_x(i)
        y = func_y(i)
        list_point.append([x, y, 1])
        # paint_point(x, y)
        # print(x, y)
    except:
        pass

for i in np.arange(0, 2 * pi * 2, 0.1):
    try:
        x = x_test(i)
        y = y_test(i)
        list_point.append([x, y, 1])
        # paint_point(x, y)
        # print(x, y)
    except:
        pass


# for i in range(1, len(list_point)):
# 	print(list_point[i])

paint_point(list_point[0])

for i in range(1, len(list_point)):
    paint_point(list_point[i])
    paint_line(list_point[i], list_point[i - 1])

canv.pack()
root.mainloop()
