#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from copy import deepcopy
from math import *
from tkinter import *
from tkinter import messagebox as mb

a = 40
b = 60
win_size = 800
radius_point = 3
list_point = []
false = "-"
inverse_matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]


def func_x(t):
    return (a + b)*cos(t)-a*cos((a+b)*t/a)


def func_y(t):
    return (a+b)*sin(t)-a*sin((a+b)*t/a)


def multiplication_matrix(matrix_a, matrix_b):
    matrix_res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            temp = 0
            for k in range(3):
                temp += matrix_a[i][k] * matrix_b[k][j]
            matrix_res[i][j] = temp
    return matrix_res


def multiplication_vector(vector, matrix):
    vector_res = [0, 0, 0]

    for i in range(3):
        temp = 0
        for k in range(3):
            temp += vector[k] * matrix[k][i]
        vector_res[i] = temp

    return vector_res


def minor(m, i, j):
    return m[(i + 1) % 3][(j + 1) % 3] * m[(i + 2) % 3][(j + 2) % 3] - \
        m[(i + 1) % 3][(j + 2) % 3] * m[(i + 2) % 3][(j + 1) % 3]


def transpose(matrix):
    matrix_res = deepcopy(matrix)

    for i in range(3):
        for j in range(0, i):
            matrix_res[i][j], matrix_res[j][i] = matrix_res[j][i], matrix_res[i][j]

    return matrix_res


def determinant(m):
    det = 0
    for i in range(3):
        det += m[0][i] * minor(m, 0, i)

    return det


def inverse_func(matrix):
    matrix_res = transpose(matrix)
    matrix_copy = deepcopy(matrix_res)

    # Ищем определитель матрицы
    det = determinant(matrix_res)
    if det == 0:
        print("det = ", det)
        # det = 1
        return

    # Ищем алгебраич. доп.
    for i in range(3):
        for j in range(3):
            matrix_res[i][j] = minor(matrix_copy, i, j) / det

    return matrix_res
    # return np.linalg.inv(matrix)


def paint_point(cordinate):
    r = 1
    t = win_size / 2
    x = cordinate[0]
    y = cordinate[1]
    canv.create_oval(x - r + t, -y - r + t,
                     x + r + t, -y + r + t, fill='black')


def paint_line(a, b):
    t = win_size / 2
    canv.create_line(a[0] + t, -a[1] + t, b[0] + t,
                     -b[1] + t, fill="black", width=3)


def info_show():
    info = Toplevel(root)
    info_txt = "Условия задачи: Нарисовать эпициклоид.\
\n\nЗатем его переместить, промасштабировать и повернуть."
    label1 = Label(info, text=info_txt, font="Verdana 14")
    label1.pack()


def print_error(string_error):
    mb.showerror(title="Ошибка", message=string_error)


def check_answer(answer):
    correct = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", ".", "-"]

    for i in answer:
        if i not in correct:
            print_error("Возможно, вы ввели некорректные символы.")
            return False
    return True


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


def moving_func(dx, dy):
    matrix_mov = [[1, 0, 0],
                  [0, 1, 0],
                  [dx, dy, 1]]

    global inverse_matrix
    inverse_matrix = inverse_func(matrix_mov)

    for i in range(len(list_point)):
        list_point[i] = multiplication_vector(list_point[i], matrix_mov)
        # list_point[i] = np.dot(list_point[i], matrix_mov)
    print_scene()


def rotation():
    angle = entry_angle.get()
    if (check_answer(angle) == False):
        return
    angle = float_answer(angle)
    if (angle == false):
        return

    xm = entry_angle_xm.get()
    if (check_answer(xm) == False):
        return
    xm = float_answer(xm)
    if (xm == false):
        return

    ym = entry_angle_ym.get()
    if (check_answer(ym) == False):
        return
    ym = float_answer(ym)
    if (ym == false):
        return

    # print("angle = ", angle, "Xm = ", xm, "Ym = ", ym)

    dx = -xm
    dy = -ym
    # dx = -list_point[len(list_point) - 1][0]
    # dy = -list_point[len(list_point) - 1][1]

    # Переводим в радианы.
    angle *= pi / 180
    matrix = [[cos(angle), sin(angle), 0],
              [-sin(angle), cos(angle), 0],
              [0, 0, 1]]

    matrix_mov = [[1, 0, 0],
                  [0, 1, 0],
                  [dx, dy, 1]]

    matrix_res = multiplication_matrix(matrix_mov, matrix)
    matrix_mov[2][0], matrix_mov[2][1] = -dx, -dy
    matrix_res = multiplication_matrix(matrix_res, matrix_mov)

    global inverse_matrix

    for i in range(len(list_point)):
        list_point[i] = multiplication_vector(list_point[i], matrix_res)
        # list_point[i] = np.dot(list_point[i], matrix)

    inverse_matrix = inverse_func(matrix_res)

    print_scene()


def moving():
    dx = entry_dx.get()
    dy = entry_dy.get()

    if (check_answer(dx) == False):
        return
    dx = int_answer(dx)
    if (dx == false):
        return

    if (check_answer(dy) == False):
        return
    dy = int_answer(dy)
    if (dy == false):
        return

    moving_func(dx, dy)


def scale():
    kx = entry_kx.get()
    if (check_answer(kx) == False):
        return
    kx = float_answer(kx)
    if (kx == false):
        return

    ky = entry_ky.get()
    if (check_answer(ky) == False):
        return
    ky = float_answer(ky)
    if (ky == false):
        return

    if kx == 0 or ky == 0:
        print_error("При таких значениях рисунка не будет!")
        return

    xm = entry_xm.get()
    if (check_answer(xm) == False):
        return
    xm = -float_answer(xm)
    if (xm == false):
        return

    ym = entry_ym.get()
    if (check_answer(ym) == False):
        return
    ym = -float_answer(ym)
    if (ym == false):
        return

    # print("kx = ", kx, "ky = ", ky, "xm = ", xm, "ym = ", ym)

    matrix = [[kx, 0, 0],
              [0, ky, 0],
              [0, 0, 1]]

    matrix_mov = [[1, 0, 0],
                  [0, 1, 0],
                  [xm, ym, 1]]

    matrix_res = multiplication_matrix(matrix_mov, matrix)
    matrix_mov[2][0], matrix_mov[2][1] = -xm, -ym
    matrix_res = multiplication_matrix(matrix_res, matrix_mov)

    global inverse_matrix
    # inverse_matrix = inverse_func(matrix)
    inverse_matrix = inverse_func(matrix_res)

    for i in range(len(list_point)):
        list_point[i] = multiplication_vector(list_point[i], matrix_res)
        # list_point[i] = np.dot(list_point[i], matrix)

    print_scene()


def cancel():
    global inverse_matrix
    for i in range(len(list_point)):
        list_point[i] = np.dot(list_point[i], inverse_matrix)
    inverse_matrix = [[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]]
    print_scene()


def print_scene():
    canv.delete(ALL)
    canv.create_line(win_size/2, win_size, win_size/2, 0, width=2, arrow=LAST)
    canv.create_line(0, win_size / 2, win_size,
                     win_size / 2, width=2, arrow=LAST)
    canv.create_text(10, 10, text="Экран 800x800")

    for i in range(len(list_point) - 2 - 8):
        paint_point(list_point[i])
        paint_line(list_point[i], list_point[i + 1])
    paint_point(list_point[len(list_point) - 1 - 8])

    paint_line(list_point[len(list_point) - 8],
               list_point[len(list_point) - 7])
    paint_line(list_point[len(list_point) - 6],
               list_point[len(list_point) - 5])

    paint_line(list_point[len(list_point) - 4],
               list_point[len(list_point) - 3])
    paint_line(list_point[len(list_point) - 2],
               list_point[len(list_point) - 1])
    # paint_line([-250, 150], [250, 150])
    # paint_line([-250, -150], [250, -150])

    # paint_line([-250, -150], [-250, 150])
    # paint_line([250, -150], [250, 150])


def create_scene():
    for i in np.arange(0, 2 * pi * 2, 0.1):
        # try:
        x = func_x(i)
        y = func_y(i)
        list_point.append([x, y, 1])
        # except:
        # pass
    list_point.append([0, 0, 1])

    list_point.append([-250, 150, 1])
    list_point.append([250, 150, 1])

    list_point.append([-250, -150, 1])
    list_point.append([250, -150, 1])

    list_point.append([-250, -150, 1])
    list_point.append([-250, 150, 1])

    list_point.append([250, -150, 1])
    list_point.append([250, 150, 1])

    print_scene()


def return_all():
    global inverse_matrix
    inverse_matrix = [[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]]
    for i in range(len(list_point) - 1, -1, -1):
        del list_point[i]
    # print("Массив: ", list_point)
    create_scene()


if __name__ == "__main__":

    # root_a_b = Tk()
    # root_a_b.title('Лабораторная работа №2')
    # root_a_b.geometry("600x400")
    # root_a_b.configure(bg="lavender")
    # root_a_b.resizable(width=False, height=False)

    # label = Label(root, text="kx:", bg="lavender").place(x=800,
    #                                                      y=450, anchor="w", width=100)

    # entry_dx = Entry(root_a_b, width="50")
    # entry_dx.place(x=100, y=100, anchor="center", width=150)

    # root_a_b.mainloop()

    #
    root = Tk()
    root.title('Лабораторная работа №2')
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

    create_scene()

    button = Button(text="Перенести", width=15,
                    command=moving, bg="thistle3")
    button.place(x=1000, y=50, anchor="center")
    label = Label(root, text="dx:", bg="lavender").place(x=800,
                                                         y=100, anchor="w", width=100)
    entry_dx = Entry(root, width="50")
    entry_dx.place(x=1000, y=100, anchor="center", width=150)
    label = Label(root, text="dy:", bg="lavender").place(x=800,
                                                         y=150, anchor="w", width=100)
    entry_dy = Entry(root, width="50")
    entry_dy.place(x=1000, y=150, anchor="center", width=150)

    button = Button(text="Повернуть", width=15,
                    command=rotation,  bg="thistle3")
    button.place(x=1000, y=200, anchor="center")
    label = Label(root, text="Угол:", bg="lavender").place(x=800,
                                                           y=250, anchor="w", width=100)
    label = Label(root, text="Xm:", bg="lavender").place(x=800,
                                                         y=300, anchor="w", width=100)
    label = Label(root, text="Ym:", bg="lavender").place(x=800,
                                                         y=350, anchor="w", width=100)
    entry_angle = Entry(root, width="50")
    entry_angle.place(x=1000, y=250, anchor="center", width=150)

    entry_angle_xm = Entry(root, width="50")
    entry_angle_xm.place(x=1000, y=300, anchor="center", width=150)

    entry_angle_ym = Entry(root, width="50")
    entry_angle_ym.place(x=1000, y=350, anchor="center", width=150)

    button = Button(text="Масштабировать", width=15,
                    command=scale,  bg="thistle3")
    button.place(x=1000, y=400, anchor="center")

    entry_kx = Entry(root, width="50")
    entry_kx.place(x=1000, y=450, anchor="center", width=150)

    entry_ky = Entry(root, width="50")
    entry_ky.place(x=1000, y=500, anchor="center", width=150)

    entry_xm = Entry(root, width="50")
    entry_xm.place(x=1000, y=550, anchor="center", width=150)

    entry_ym = Entry(root, width="50")
    entry_ym.place(x=1000, y=600, anchor="center", width=150)

    label = Label(root, text="kx:", bg="lavender").place(x=800,
                                                         y=450, anchor="w", width=100)
    label = Label(root, text="ky:", bg="lavender").place(x=800,
                                                         y=500, anchor="w", width=100)
    label = Label(root, text="Xm:", bg="lavender").place(x=800,
                                                         y=550, anchor="w", width=100)
    label = Label(root, text="Ym:", bg="lavender").place(x=800,
                                                         y=600, anchor="w", width=100)

    button = Button(text="Вернуть \nначальный рисунок", width=15,
                    command=return_all, bg="thistle3")
    button.place(x=1000, y=675, anchor="center")

    button_del_all = Button(text="Шаг назад\n(Можно только 1 раз)", width=15,
                            command=cancel, bg="thistle3")
    button_del_all.place(x=1000, y=750, anchor="center")

    root.mainloop()
