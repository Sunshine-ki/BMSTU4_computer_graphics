#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *
from tkinter import *
from tkinter import messagebox as mb
from tkinter import colorchooser


win_size = 800
false = "-"
color_line = ((0.0, 0.0, 0.0), '#000000')
color_bg = ((255, 255, 255), '#ffffff')


def info_show():
    info = Toplevel(root)
    info_txt = "Условия задачи: Нарисовать отрезок."
    label1 = Label(info, text=info_txt, font="Verdana 14")
    label1.pack()


def print_error(string_error):
    mb.showerror(title="Ошибка", message=string_error)


def check_answer(answer):
    # print(answer)
    if answer == "":
        print_error("У вас пустое поле ввода")
        return false, false

    correct = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", ".", "-"]

    for i in answer:
        if i not in correct:
            print_error("Вы ввели некорректные символы.")
            return false, false

    try:
        a, b = map(float, answer.split())
    except:
        print_error("Вы неправильно ввели координаты точки. \
Напоминаю, что точка задается двумя \
координатами x и y, разделённых пробелом.")
        return false, false

    # if fabs(a) > max_coordinate or fabs(b) > max_coordinate:
    #     print_error(
    #         "Возможно, вы ввели координату, которая выходит за границу оси.")
    #     return false, false

    return (a, b)


def int_answer(answer):
    try:
        a = int(answer)
    except:
        print_error("Возможно, у вас вещественное значение или пустой ввод.")
        return false

    return a


def float_answer(answer):
    try:
        a = float(answer)
    except:
        print_error("Возможно, у вас пустой ввод.")
        return false

    return a


def choose_color():
    # Интенсивность каждого цвета и сам цвет.
    return colorchooser.askcolor(title="Выбор цвета")


def choose_color_background():
    global color_bg
    color_bg = choose_color()
    canv.configure(bg=color_bg[1])
    print("Bg = ", color_bg)


def choose_color_line():
    global color_line
    color_line = choose_color()

    label_color_line.configure(bg=color_line[1])

    print("color_line = ", color_line)


def draw_color_background():
    global color_line, color_bg
    color_line = color_bg

    label_color_line.configure(bg=color_line[1])

    print("color_line = ", color_line)


def paint_line():
    start = check_answer(entry_start.get())
    if start[0] == false:
        return

    stop = check_answer(entry_stop.get())
    if stop[0] == false:
        return

    if (start == stop):
        print_error("Начало и конец совпадают")
        return

    print("Метод №", var.get(), "От: ", start, "До: ", stop)


def clear_all():
    canv.delete(ALL)


if __name__ == "__main__":
    root = Tk()
    root.title('Лабораторная работа №3')
    root.geometry("1200x800")
    root.configure(bg="lavender")
    root.resizable(width=False, height=False)

    main_menu = Menu(root)
    root.configure(menu=main_menu)

    third_item = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Инструкция",
                          menu=third_item, font="Verdana 10")
    third_item.add_command(label="Показать инструкцию",
                           command=info_show, font="Verdana 12")

    canv = Canvas(root, width=800, height=800, bg="white")
    canv.place(x=0, y=0)

    button = Button(text="Выбрать цвет фона", width=25,
                    command=choose_color_background,  bg="thistle3")
    button.place(x=1000, y=25, anchor="center")

    button = Button(text="Выбрать цвет отрезка", width=25,
                    command=choose_color_line,  bg="thistle3")
    button.place(x=1000, y=75, anchor="center")

    button = Button(text="Рисовать фоновым цветом", width=25,
                    command=draw_color_background,  bg="thistle3")
    button.place(x=1000, y=125, anchor="center")

    var = IntVar()
    var.set(0)
    method1 = Radiobutton(text="Метод №1", variable=var,
                          value=0, bg="lavender", width=25, font="Verdana 12")
    method2 = Radiobutton(text="Метод №2", variable=var,
                          value=1, bg="lavender", width=25, font="Verdana 12")
    method3 = Radiobutton(text="Метод №3", variable=var,
                          value=2, bg="lavender", width=25, font="Verdana 12")
    method4 = Radiobutton(text="Метод №4", variable=var,
                          value=3, bg="lavender", width=25, font="Verdana 12")
    method5 = Radiobutton(text="Метод №5", variable=var,
                          value=4, bg="lavender", width=25, font="Verdana 12")

    method1.place(x=1000, y=175, anchor="center")
    method2.place(x=1000, y=200, anchor="center")
    method3.place(x=1000, y=225, anchor="center")
    method4.place(x=1000, y=250, anchor="center")
    method5.place(x=1000, y=275, anchor="center")

    label = Label(root, text="Начальная точка (x, y):", bg="lavender", width=25,
                  font="Verdana 12")
    label.place(x=800, y=325, anchor="w", width=200)

    entry_start = Entry(root, width="50")
    entry_start.place(x=1000, y=325, anchor="w", width=150)

    label = Label(root, text="Конечная точка (x, y):", bg="lavender", width=25,
                  font="Verdana 12")
    label.place(x=800, y=350, anchor="w", width=200)

    entry_stop = Entry(root, width="50")
    entry_stop.place(x=1000, y=350, anchor="w", width=150)

    button = Button(text="Нарисовать отрезок", width=25,
                    command=paint_line,  bg="thistle3")
    button.place(x=1000, y=400, anchor="center")

    # entry_ym = Entry(root, width="50")
    # entry_ym.place(x=1000, y=600, anchor="center", width=150)

    # label = Label(root, text="kx:", bg="lavender").place(x=800,
    #                                                      y=450, anchor="w", width=100)

    label = Label(root, text="Цвет линии:", bg="lavender", width=25,
                             font="Verdana 12")
    label.place(x=800, y=700, anchor="w", width=200)

    label_color_line = Label(root, text=" " * 5, bg=color_line[1],
                             font="Verdana 12")
    label_color_line.place(x=1000, y=700, anchor="w", width=100)

    button = Button(text="Стереть всё", width=25,
                    command=clear_all,  bg="thistle3")
    button.place(x=1000, y=750, anchor="center")

    root.mainloop()
