#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import scrolledtext as tkst
from tkinter import messagebox as mb
from tkinter import colorchooser

from math import *
import numpy as np
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

WIDTH, HEIGHT = 800, 800

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


def get_two_answer(answer):
    try:
        a, b = map(float, answer.split())
    except:
        print_error("Вы неправильно ввели координаты точки. \
Напоминаю, что точка задается двумя \
координатами x и y, разделённых пробелом.")
        return false, false
    return (a, b)


def check_answer(answer):
    # print(answer)
    if answer == "":
        print_error("У вас пустое поле ввода")
        return 1

    correct = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", ".", "-"]

    for i in answer:
        if i not in correct:
            print_error("Вы ввели некорректные символы.")
            return 1

    # if fabs(a) > max_coordinate or fabs(b) > max_coordinate:
    #     print_error(
    #         "Возможно, вы ввели координату, которая выходит за границу оси.")
    #     return false, false
    return 0


def choose_color():
    # Интенсивность каждого цвета и сам цвет.
    return colorchooser.askcolor(title="Выбор цвета")


def choose_color_background():
    global color_bg
    color_bg = choose_color()
    canv.configure(bg=color_bg[1])
    label_color_bg.configure(bg=color_bg[1])
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


def print_pixel(x, y):
    img.put(color_line[1], (round(x), round(y)))
    # (round(x + WIDTH / 2), round(-y + HEIGHT / 2)))


def differential_analyzer(start, stop):
    dx = stop[0] - start[0]
    dy = stop[1] - start[1]

    if fabs(dx) - fabs(dy) >= 0:
        l = fabs(dx)
    else:
        l = fabs(dy)

    dx, dy = dx / l, dy / l
    x, y = float(start[0]), float(start[1])

    for _ in range(int(l + 1)):
        print_pixel(x, y)
        x += dx
        y += dy


def sign(a):
    if a == 0:
        return 0
    return a / abs(a)


def bresenham(start, stop):
    dx = fabs(stop[0] - start[0])
    dy = fabs(stop[1] - start[1])
    x, y = float(start[0]), float(start[1])
    sx, sy = sign(dx), sign(dy)

    swap = 0

    if dy > dx:
        swap = 1
        dx, dy = dy, dx

    m = dy / dx
    e = m - 0.5

    for _ in range(int(dx + 1)):
        print_pixel(x, y)
        # print(x, y)

        if e >= 0:
            if swap == 0:
                y += sy
            else:
                x += sx
            e -= 1

        if e < 0:
            if swap == 0:
                x += sx
            else:
                y += sy
            e += m


def library_method(a, b):
    # t = win_size / 2
    # canv.create_line(a[0] + t, -a[1] + t, b[0] + t,
    #                  -b[1] + t, fill="black", width=3)
    # , fill="black", width=3)
    canv.create_line(a[0], a[1], b[0], b[1], fill=color_line[1])

# def bresenham(start, stop):
#     dx = fabs(stop[0] - start[0])
#     dy = fabs(stop[1] - start[1])

#     x, y = float(start[0]), float(start[1])

#     f = dx / 2

#     if dx - dy < 0:
#         dx, dy = dy, dx

#     for _ in range(int(dx + 1)):
#         print_pixel(x, y)
#         print(x, y)
#         temp = f - dy
#         if temp <= 0:
#             f = dx + temp
#             y += 1
#         x += 1

    # sx, sy = sign(dx), sign(dy)


def paint_line():
    if check_answer(entry_start.get()):
        return

    start = get_two_answer(entry_start.get())
    if start[0] == false:
        return

    if check_answer(entry_stop.get()):
        return
    stop = get_two_answer(entry_stop.get())
    if stop[0] == false:
        return

    if (start == stop):
        print_error("Начало и конец совпадают")
        return

    method = var.get()

    print("Метод №", method, "От: ", start, "До: ", stop)

    if method == 0:
        print("Метод ЦДА")
        differential_analyzer(start, stop)
    elif method == 1:
        print("Метод Брезенхема")
        bresenham(start, stop)
    elif method == 2:
        print("Библиотечный метод")
        library_method(start, stop)


def paint_lines():
    if check_answer(entry_length.get()):
        return

    if check_answer(entry_step.get()):
        return

    length = float_answer(entry_length.get())  # Float ?
    if length == false:
        return

    if length < 0:
        print_error("Длина не может быть отрицательной")
        return

    step = float_answer(entry_step.get())  # Float ?
    if step == false:
        return

    print("Метод №", var.get(), "Длина: ", length, "Шаг: ", step)

    if 360 % step != 0:
        print_error("Шаг должен быть кратен 360")
        return

    method = var.get()

    x, y = length + WIDTH / 2, HEIGHT / 2
    t = step
    start = (WIDTH / 2, HEIGHT / 2)

    for _ in range(int(360 / step)):
        if method == 0:
            differential_analyzer(start, (int(x), int(y)))
        elif method == 1:
            bresenham(start, (int(x), int(y)))
        elif method == 2:
            library_method(start, (int(x), int(y)))

        x = length * cos(t * pi / 180) + WIDTH / 2
        y = -(length * sin(t * pi / 180)) + HEIGHT / 2
        t += step


def clear_all():
    global img

    canv.delete(ALL)

    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canv.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
    canv.create_text(10, 10, text="Экран 800x800", font="Verdana 12")


def time_characteristic():
    window = Tk()
    window.geometry('700x700')
    window.title('Времянные характеристики')

    data_lst = [31, 41, 59, 26, 53, 58, 97]
    # data_lst.sort()

    fig = Figure(figsize=(10, 10))  # , dpi=100)
    # Оси (1 строка. 1 столбец) axes
    ax = fig.add_subplot(111)

    # ax.set_facecolor('red')
    # ax.set_xlim([-10, 10])
    # ax.set_ylim([-2, 2])
    # ax.set_title('Основы анатомии matplotlib')
    # ax.set_xlabel('ось абцис (XAxis)')
    # ax.set_ylabel('ось ординат (YAxis)')

    ind = np.arange(len(data_lst))  # [0, 1, ... , len(data_lst) - 1]
    ax.bar(ind, data_lst, 0.8)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=RIGHT)

    window.mainloop()


def step_characteristic():
    pass


if __name__ == "__main__":
    # Настройка окна.
    root = Tk()
    root.title('Лабораторная работа №3')
    root.geometry("1200x800")
    root.configure(bg="lavender")
    root.resizable(width=False, height=False)

    main_menu = Menu(root)
    root.configure(menu=main_menu)

    # Инструкция.

    third_item = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Инструкция",
                          menu=third_item, font="Verdana 10")
    third_item.add_command(label="Показать инструкцию",
                           command=info_show, font="Verdana 12")

    # Canvas.

    canv = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
    canv.place(x=0, y=0)

    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canv.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
    canv.create_text(10, 10, text="Экран 800x800", font="Verdana 12")

    # Цвета.

    button = Button(text="Выбрать цвет фона", width=40,
                    command=choose_color_background,  bg="thistle3")
    button.place(x=1000, y=25, anchor="center")

    button = Button(text="Выбрать цвет отрезка", width=40,
                    command=choose_color_line,  bg="thistle3")
    button.place(x=1000, y=75, anchor="center")

    button = Button(text="Рисовать фоновым цветом", width=40,
                    command=draw_color_background,  bg="thistle3")
    button.place(x=1000, y=125, anchor="center")

    # Выбор метода.

    var = IntVar()
    var.set(0)
    method1 = Radiobutton(text="Метод ЦДА", variable=var,
                          value=0, bg="lavender", width=25, font="Verdana 12")
    method2 = Radiobutton(text="Метод Брезенхема", variable=var,
                          value=1, bg="lavender", width=25, font="Verdana 12")
    method3 = Radiobutton(text="Библиотечный метод", variable=var,
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

    # Линия.

    label = Label(root, text="Начальная точка (x y):", bg="lavender", width=25,
                  font="Verdana 12")
    label.place(x=800, y=325, anchor="w", width=200)

    entry_start = Entry(root, width="50")
    entry_start.place(x=1000, y=325, anchor="w", width=150)

    label = Label(root, text="Конечная точка (x y):", bg="lavender", width=25,
                  font="Verdana 12")
    label.place(x=800, y=350, anchor="w", width=200)

    entry_stop = Entry(root, width="50")
    entry_stop.place(x=1000, y=350, anchor="w", width=150)

    button = Button(text="Нарисовать отрезок", width=40,
                    command=paint_line,  bg="thistle3")
    button.place(x=1000, y=400, anchor="center")

    # Пучок.

    label = Label(root, text="Длина пучка:", bg="lavender", width=25,
                  font="Verdana 12")
    label.place(x=800, y=450, anchor="w", width=200)

    entry_length = Entry(root, width="50")
    entry_length.place(x=1000, y=450, anchor="w", width=150)

    label = Label(root, text="Шаг изменения угла:", bg="lavender", width=25,
                  font="Verdana 12")
    label.place(x=800, y=475, anchor="w", width=200)

    entry_step = Entry(root, width="50")
    entry_step.place(x=1000, y=475, anchor="w", width=150)

    button = Button(text="Нарисовать пучок", width=40,
                    command=paint_lines,  bg="thistle3")
    button.place(x=1000, y=525, anchor="center")

    # Цвет линии.

    label = Label(root, text="Цвет линии:", bg="lavender", width=25,
                  font="Verdana 12")
    label.place(x=800, y=575, anchor="w", width=200)

    label_color_line = Label(root, text=" " * 5, bg=color_line[1],
                             font="Verdana 12")
    label_color_line.place(x=1000, y=575, anchor="w", width=100)

    # Цвет фона.

    label = Label(root, text="Цвет фона:", bg="lavender", width=25,
                  font="Verdana 12")
    label.place(x=800, y=610, anchor="w", width=200)

    label_color_bg = Label(root, text=" " * 5, bg=color_bg[1],
                           font="Verdana 12")
    label_color_bg.place(x=1000, y=610, anchor="w", width=100)

    # Временная характеристика.

    button = Button(text="Показать времянные характеристики", width=40,
                    command=time_characteristic,  bg="thistle3")
    button.place(x=1000, y=650, anchor="center")

    # Ступенчатость.

    button = Button(text="Исследование ступенчатости", width=40,
                    command=step_characteristic,  bg="thistle3")
    button.place(x=1000, y=700, anchor="center")

    # Очистка экрана.

    button = Button(text="Стереть всё", width=40,
                    command=clear_all,  bg="thistle3")
    button.place(x=1000, y=750, anchor="center")

    root.mainloop()
