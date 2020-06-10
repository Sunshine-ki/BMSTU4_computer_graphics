#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import scrolledtext as tkst
from tkinter import messagebox as mb
from tkinter import colorchooser

from time import *
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
        if len(answer.split()) != 1:
            print_error("У вас больше одного числа")
            return false
        if answer == "":
            print_error("У вас пустой ввод")
            return false
        a = int(answer)
    except:
        print_error("Возможно, у вас вещественное значение")
        return false

    return a


def float_answer(answer):
    try:
        if len(answer.split()) != 1:
            print_error("У вас больше одного числа")
            return false
        if answer == "":
            print_error("У вас пустой ввод")
            return false
        a = float(answer)
    except:
        print_error("Ошибка ввода")
        return false

    return a


def get_two_answer(answer):
    try:
        if len(answer.split()) != 2:
            print_error("Вы неправильно ввели координаты точки. \
Напоминаю, что точка задается двумя \
координатами x и y, разделённых пробелом.")
            return false, false
        a, b = map(int, answer.split())
    except:
        print_error("Координаты должны быть целого типа")
        return false, false
    return (a, b)


def check_answer(answer):
    # print(answer)
    if answer == "":
        print_error("У вас пустое поле ввода")
        return 1

    correct = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "-", "."]

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


def parse_color(color):
    color_str = "#"
    # print("color = ", color)
    for i in range(3):
        temp = hex(int(color[i]))
        # print("temp = ", temp)
        temp = temp[2:]

        if int(temp, base=16) <= 15:
            temp = "0" + temp
        color_str += str(temp)
    return color_str


def print_pixel_color(x, y, intensity):
    # if intensity ==
    global color_line
    intensity = fabs(intensity)
    intensity_color = list(color_line[0])
    # print("intensity_color = ", intensity_color)
    # print("intensity = ", intensity)
    for i in range(3):
        if fabs(round(intensity_color[i]) - 256) < 2:
            continue

        intensity_color[i] = (255 - intensity_color[i]) * intensity

    # print("real = ", color_line[1])
    # print("intensity_color = ", intensity_color)
    # print("parse_color(intensity_color) = ", parse_color(intensity_color))

    canv.create_line(round(x), round(y), round(
        x), round(y) + 1, width=1, fill=parse_color(intensity_color))


def print_pixel(x, y):
    canv.create_line(round(x), round(y), round(
        x), round(y) + 1, width=1, fill=color_line[1])
    # img.put(color_line[1], (round(x), round(y)))
    # (round(x + WIDTH / 2), round(-y + HEIGHT / 2)))


def differential_analyzer(start, stop):
    dx = stop[0] - start[0]
    dy = stop[1] - start[1]

    if fabs(dx) - fabs(dy) >= 0:
        l = fabs(dx)
    else:
        l = fabs(dy)

    dx, dy = dx / l, dy / l
    x, y = start[0], start[1]
    print("dx, dy", dx, dy)

    # print("l = ", l)
    for _ in range(int(l + 1)):
        print_pixel(x, y)
        # print(x, y)
        x += dx
        y += dy


def sign(a):
    if a == 0:
        return 0
    return a / abs(a)


def bresenham_float(start, stop):
    dx = stop[0] - start[0]
    dy = stop[1] - start[1]
    x, y = start[0], start[1]
    sx, sy = sign(dx), sign(dy)
    dx = fabs(dx)
    dy = fabs(dy)

    swap = 0
    if dy > dx:
        swap = 1
        dx, dy = dy, dx
    m = dy / dx
    e = m - 0.5

    for _ in range(int(dx + 1)):
        print_pixel(x, y)
        if e >= 0:
            if swap == 0:
                y += sy
            else:
                x += sx
            e -= 1

        if swap == 0:
            x += sx
        else:
            y += sy
        e += m


def bresenham_int(start, stop):
    dx = stop[0] - start[0]
    dy = stop[1] - start[1]
    x, y = start[0], start[1]
    sx, sy = sign(dx), sign(dy)
    dx = fabs(dx)
    dy = fabs(dy)

    swap = 0

    if dy > dx:
        swap = 1
        dx, dy = dy, dx

    # m = dy / dx
    e = 2 * dy - dx

    for _ in range(int(dx + 1)):
        print_pixel(x, y)
        # print(e, x, y)

        if e >= 0:
            if swap == 0:
                y += sy
            else:
                x += sx
            e -= (2 * dx)

        if e < 0:
            if swap == 0:
                x += sx
            else:
                y += sy
            e += (2 * dy)


def bresenham_smooth(start, stop):
    dx = stop[0] - start[0]
    dy = stop[1] - start[1]
    x, y = start[0], start[1]
    sx, sy = sign(dx), sign(dy)
    dx = fabs(dx)
    dy = fabs(dy)

    swap = 0
    if dy > dx:
        swap = 1
        dx, dy = dy, dx
    m = dy / dx
    e = 0.5

    for _ in range(int(dx + 1)):
        print_pixel_color(x, y, 1 - e)

        if e >= 1:
            if swap == 0:
                y += sy
            else:
                x += sx
            e -= 1
        if swap == 0:
            x += sx
        else:
            y += sy
        e += m


def vu(start, stop):
    dx = stop[0] - start[0]
    dy = stop[1] - start[1]
    x, y = start[0], start[1]
    sx, sy = sign(dx), sign(dy)
    dx = fabs(dx)
    dy = fabs(dy)

    swap = 0
    if dy > dx:
        swap = 1
        dx, dy = dy, dx
    m = dy / dx
    e = 0.5
    w = 1

    for _ in range(int(dx + 1)):
        if swap == 0:
            print_pixel_color(x, y, - e)
            print_pixel_color(x, y + sy, e - 1)
        else:
            print_pixel_color(x, y, e)
            print_pixel_color(x + sx, y, e - 1)

        if e >= w - m:
            if swap == 0:
                y += sy
            else:
                x += sx
            e -= 1
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
    # global canv
    canv.create_line(a[0], a[1], b[0], b[1], fill=color_line[1])


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
    # t1 = 0

    print("Метод №", method, "От: ", start, "До: ", stop)

    if method == 0:
        print("Метод ЦДА")
        # t1 = time()
        differential_analyzer(start, stop)
        # time_list[0] = round(time() - t1, 6)
    elif method == 1:
        print("Метод Брезенхема (float)")
        # t1 = time()
        bresenham_float(start, stop)
        # time_list[1] = round(time() - t1, 6)
    elif method == 2:
        print("Метод Брезенхема (int)")
        bresenham_int(start, stop)
    elif method == 3:
        print("Метод Брезенхема (Сглаживаение)")
        bresenham_smooth(start, stop)
    elif method == 4:
        print("Библиотечный метод")
        library_method(start, stop)
    elif method == 5:
        print("Метод ВУ")
        vu(start, stop)
    canv.create_line(round(start[0]), round(start[1]), round(
        start[0]), round(start[1]) + 1, width=1, fill="red")

    canv.create_line(round(stop[0]), round(stop[1]), round(
        stop[0]), round(stop[1]) + 1, width=1, fill="red")


def paint_lines():
    if check_answer(entry_length.get()):
        return

    if check_answer(entry_step.get()):
        return

    length = int_answer(entry_length.get())
    if length == false:
        return

    if length < 0:
        print_error("Длина не может быть отрицательной")
        return

    step = int_answer(entry_step.get())  # Float ?
    if step == false:
        return

    # print("Метод №", var.get(), "Длина: ", length, "Шаг: ", step)

    if 360 % step != 0:
        print_error("Шаг должен быть кратен 360")
        return

    method = var.get()

    x, y = length + WIDTH / 2, HEIGHT / 2
    t = step
    start = (WIDTH / 2, HEIGHT / 2)

    for _ in range(int(360 / step)):
        if method == 0:
            differential_analyzer(start, (round(x), round(y)))
        elif method == 1:
            bresenham_float(start, (round(x), round(y)))
        elif method == 2:
            bresenham_int(start, (round(x), round(y)))
        elif method == 3:
            # print(start, (round(x), round(y)))
            bresenham_smooth(start, (round(x), round(y)))
        elif method == 4:
            library_method(start, (round(x), round(y)))
        elif method == 5:
            vu(start, (round(x), round(y)))
        print(x, y)

        x = length * cos(t * pi / 180) + WIDTH / 2
        y = -(length * sin(t * pi / 180)) + HEIGHT / 2
        t += step


def clear_all():
    # global img

    canv.delete(ALL)

    # img = PhotoImage(width=WIDTH, height=HEIGHT)
    # canv.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
    canv.create_text(10, 10, text="Экран 800x800", font="Verdana 12")


def close_windows():
    pass


def time_characteristic(entry_start_q, entry_stop_q, window_question):
    if check_answer(entry_start_q.get()):
        # window_question.destroy()
        return

    start = get_two_answer(entry_start_q.get())
    if start[0] == false:
        # window_question.destroy()
        return

    if check_answer(entry_stop_q.get()):
        # window_question.destroy()
        return
    stop = get_two_answer(entry_stop_q.get())
    if stop[0] == false:
        # window_question.destroy()
        return

    if (start == stop):
        print_error("Начало и конец совпадают")
        # window_question.destroy()
        return

    # print(start, stop)

    window_question.destroy()

    time_list = [0, 0, 0, 0, 0, 0]

    # Метод ЦДА.
    t1 = time()
    for _ in range(30):
        differential_analyzer(start, stop)
    time_list[0] = round(time() - t1, 6)

    # Метод Брезенхема. (float)
    t1 = time()
    for _ in range(30):
        bresenham_float(start, stop)
    time_list[1] = round(time() - t1, 6)

    # Метод Брезенхема. (int)
    t1 = time()
    for _ in range(30):
        bresenham_int(start, stop)
    time_list[2] = round(time() - t1, 6)

    # Метод Брезенхема. (сглаживание)
    t1 = time()
    for _ in range(30):
        bresenham_smooth(start, stop)
    time_list[3] = round(time() - t1, 6)

    # Библиотечный метод.
    t1 = time()
    for _ in range(30):
        library_method(start, stop)
    time_list[4] = round(time() - t1, 6)

    # ВУ.
    t1 = time()
    for _ in range(30):
        vu(start, stop)
    time_list[5] = round(time() - t1, 6)

    print(time_list)

    window = Tk()
    window.geometry('750x750')
    window.title('Времянные характеристики')

    fig = Figure(figsize=(10, 10))  # , dpi=100)
    # Оси (1 строка. 1 столбец) axes
    ax = fig.add_subplot(111)

    # ax.set_facecolor('red')
    # ax.set_xlim([-10, 10])
    # ax.set_ylim([-2, 2])
    # ax.set_title('Основы анатомии matplotlib')
    # ax.set_xlabel('ось абцис (XAxis)')
    ax.set_ylabel('Время (t) [секунды]')

    ind = ("ЦДА", "Брезенхем\n(float)", "Брезенхем\n(int)",
           "Брезенхем\n(сглаживание)", "Библиотечный", "ВУ")  # np.arange(len(time_list))  # [0, 1, ... , len(data_lst) - 1]
    ax.bar(ind, time_list, 0.4)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=RIGHT)

    window.mainloop()


def time_characteristic_question():
    # list_method = ("ЦДА\n", "Брезенхем (int)\n", "Брезенхем (float)\n",
    #                "Брезенхем (сглаживание)\n", "Библиотченый\n")
    # str_err = "Недостаточно данных. Вы не использовали:\n"
    # flag = 0
    # for i in range(len(time_list)):
    #     if time_list[i] == -1:
    #         flag = 1
    #         str_err += list_method[i]
    # if flag:
    #     print_error(str_err + "")
    #     return
    window_question = Tk()
    window_question.geometry('300x250')
    window_question.configure(bg="lavender")
    window_question.title('Ввод')

    label = Label(window_question, text="Начальная точка (x y):", bg="lavender", width=25,
                  font="Verdana 12")
    label.place(x=150, y=10, anchor="center", width=200)

    entry_start_q = Entry(window_question, width=50)
    entry_start_q.place(x=150, y=50, anchor="center", width=150)

    label = Label(window_question, text="Конечная точка (x y):", bg="lavender", width=25,
                  font="Verdana 12")
    label.place(x=150, y=100, anchor="center", width=200)

    entry_stop_q = Entry(window_question, width=50)
    entry_stop_q.place(x=150, y=150, anchor="center", width=150)

    button = Button(window_question, text="Сравнить",
                    command=lambda arg1=entry_start_q, arg2=entry_stop_q,
                    arg3=window_question: time_characteristic(arg1, arg2, arg3),  bg="thistle3")
    button.place(x=200, y=200, anchor="e")

    window_question.mainloop()


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

    # img = PhotoImage(width=WIDTH, height=HEIGHT)
    # canv.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
    canv.create_text(10, 10, text="Экран 800x800", font="Verdana 12")

    # Цвета.

    # button = Button(text="Выбрать цвет фона", width=40,
    #                 command=choose_color_background,  bg="thistle3")
    # button.place(x=1000, y=25, anchor="center")

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
    method2 = Radiobutton(text="Метод Брезенхема (float)", variable=var,
                          value=1, bg="lavender", width=25, font="Verdana 12")
    method3 = Radiobutton(text="Метод Брезенхема (int)", variable=var,
                          value=2, bg="lavender", width=25, font="Verdana 12")
    method4 = Radiobutton(text="Брезенхем (Сглаживаение)", variable=var,
                          value=3, bg="lavender", width=25, font="Verdana 12")
    method5 = Radiobutton(text="Библиотечный метод", variable=var,
                          value=4, bg="lavender", width=25, font="Verdana 12")
    method6 = Radiobutton(text="Метод ВУ", variable=var,
                          value=5, bg="lavender", width=25, font="Verdana 12")

    method1.place(x=1000, y=175, anchor="center")
    method2.place(x=1000, y=200, anchor="center")
    method3.place(x=1000, y=225, anchor="center")
    method4.place(x=1000, y=250, anchor="center")
    method6.place(x=1000, y=275, anchor="center")
    method5.place(x=1000, y=300, anchor="center")

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

    # label = Label(root, text="Цвет фона:", bg="lavender", width=25,
    #               font="Verdana 12")
    # label.place(x=800, y=610, anchor="w", width=200)

    # label_color_bg = Label(root, text=" " * 5, bg=color_bg[1],
    #                        font="Verdana 12")
    # label_color_bg.place(x=1000, y=610, anchor="w", width=100)

    # Временная характеристика.

    button = Button(text="Показать времянные характеристики", width=40,
                    command=time_characteristic_question,  bg="thistle3")
    button.place(x=1000, y=650, anchor="center")

    # Ступенчатость.

    # button = Button(text="Исследование ступенчатости", width=40,
    #                 command=step_characteristic,  bg="thistle3")
    # button.place(x=1000, y=700, anchor="center")

    # Очистка экрана.

    button = Button(text="Стереть всё", width=40,
                    command=clear_all,  bg="thistle3")
    button.place(x=1000, y=750, anchor="center")

    root.mainloop()
