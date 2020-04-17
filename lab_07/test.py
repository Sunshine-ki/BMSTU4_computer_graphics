#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *

flag = False
start = False


def keyPress(event):
    global flag, start

    if not flag:
        global start
        start = [event.x, event.y]
    flag = True

    start = [event.x, event.y]


def keyRelease(event):
    global flag, start

    canvas.create_line(start[0], start[1], event.x, event.y)

    flag = False
    start = False


def Motion(event):
    # canvas.create_line(10, )
    global start
    print(start)
    print(event.x, event.y)
    if start:
        canvas.coords("line_temp", start[0], start[1], event.x, event.y)
        # canvas.create_line(start[0], start[1], event.x, event.y)


def keyPress_rectangle(event):
    global flag, start

    if not flag:
        global start
        start = [event.x, event.y]
    flag = True

    start = [event.x, event.y]


def keyRelease_rectangle(event):
    global flag, start

    canvas.create_rectangle(start[0], start[1], event.x, event.y)

    flag = False
    start = False


def Motion_rectangle(event):
    # canvas.create_line(10, )
    global start
    print(start)
    print(event.x, event.y)
    if start:
        canvas.coords("rectangle_temp", start[0], start[1], event.x, event.y)
        # canvas.create_line(start[0], start[1], event.x, event.y)


root = Tk()
root.geometry("400x400")

canvas = Canvas(root, width=400, height=400, bg="white")
canvas.place(x=0, y=0)

canvas.create_line(0, 0, 0, 0, tags="line_temp")
canvas.create_rectangle(0, 0, 0, 0, tags="rectangle_temp")

canvas.bind("<ButtonPress>", keyPress)
canvas.bind("<ButtonRelease>", keyRelease)
canvas.bind("<Motion>", Motion)

canvas.bind("<Shift-ButtonPress>", keyPress_rectangle)
canvas.bind("<Shift-ButtonRelease>", keyRelease_rectangle)
canvas.bind("<Shift-Motion>", Motion_rectangle)

# frame.focus_set()

root.mainloop()
