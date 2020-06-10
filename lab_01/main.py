#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import fabs
from tkinter import *
from tkinter import messagebox as mb

from solution import *
from define import *


def info_show():
    info = Toplevel(root)
    info_txt = "Условия задачи: На плоскости дано множество точек. Найти такой \
\nтреугольник с вершинами в этих точках, у которого сумма \
\nрасстояний от точки пересечения высот до координатных осей максимальна \
\n\nУловия ввода:\
\n1) Координатные оси ограничены. Вводимые точки должны быть в пределах (-400, 400).\
\n2) Ввод точек осуществляется парой x и y, разделённых пробелом.\
\n3) Чтобы разделить целую и дробную часть используется точка (.)\
\n4) Все символы, кроме цифр от 0 до 9, точки (.) и знака минс (-), будут считаться некорректным вводом"
    label1 = Label(info, text=info_txt, font="Verdana 14")
    label1.pack()


def print_error(string_error):
    mb.showerror(title="Ошибка ввода", message=string_error +
                 " Проверьте, пожалуйста, ввод.")


def check_answer(answer):
    # print(answer)
    for i in answer:
        if i not in correct:
            print_error("Возможно,\
вы ввели некорректные символы.")
            return false, false

    try:
        a, b = map(float, answer.split())
    except:
        print_error("Возможно,\
вы неправильно ввели координаты точки. Напоминаю, что точка задается двумя \
координатами x и y, разделённых пробелом.")
        return false, false

    if fabs(a) > max_coordinate or fabs(b) > max_coordinate:
        print_error(
            "Возможно, вы ввели координату, которая выходит за границу оси.")
        return false, false

    return (a, b)


def paint_point(a):
    canv.create_oval(a[0] - radius_point + 400, fabs(a[1] - radius_point - 400),
                     a[0] + radius_point + 400, fabs(a[1] + radius_point - 400), 
                     width=2, fill='red', outline='black')


def paint_line(a, b):
    canv.create_line(a[0] + 400, fabs(a[1] - 400), b[0] +
                     400, fabs(b[1] - 400), fill="black", width=2)


def paint_result(a, b, c, h):
    canv.delete(ALL)
    # Рисуем координатные оси.
    canv.create_line(0, 400, 800, 400, fill="gray", width=2, arrow=LAST,
                     arrowshape="10 20 10")
    canv.create_line(400, 0, 400, 800, fill="gray", width=2, arrow=FIRST,
                     arrowshape="10 20 10")

    # Делаем рисонок больше.
    p_copy = [a[0], a[1], b[0], b[1], c[0], c[1], h[0], h[1]]
    p = [a[0], a[1], b[0], b[1], c[0], c[1], h[0], h[1], 0, 0]
    name_point = ["A", "B", "C", "H"]
    max_x = p[0]
    max_y = p[1]

    for i in range(0, len(p), 2):
        # print(p[i], p[i+1])
        if fabs(p[i]) > fabs(max_x):
            max_x = p[i]
        if fabs(p[i + 1]) > fabs(max_y):
            max_y = p[i + 1]
    if fabs(max_x) > fabs(max_y):
        maximum = max_x
    else:
        maximum = max_y

    coefficient = fabs((max_coordinate - 140) / maximum)
    if coefficient == 0: 
        coefficient = 1

    # print("X = ", max_x, "Y = ", max_y, "MAX = ", maximum)
    # print("Коэффициент: ", coefficient)

    for i in range(len(p)):
        p[i] *= coefficient

    # print(p)

    for i in range(0, 8, 2):
        paint_point((p[i], p[i + 1]))
        paint_line((p[i], p[i + 1]), (p[6], p[7]))
        canv.create_text(p[i] + 330, fabs(p[i + 1] - 400),
            text = name_point[int(i / 2)] + "(" + str(round(p_copy[i], 2)) +
            ";" + str(round(p_copy[i + 1], 2)) + ")",
            font="Verdana 12", fill="red")
            # text="{:s} ({:f}; {:f})".format(name_point[int(i / 2)],
            # round(p_copy[i], 3), round(p_copy[i + 1], 3)), 

    paint_line((p[0], p[1]), (p[2], p[3]))
    paint_line((p[0], p[1]), (p[4], p[5]))
    paint_line((p[2], p[3]), (p[4], p[5]))


def add_point():
    a = check_answer(entry_add.get())

    if (a[0] == false):
        return

    if a in point_lst:
        print_error("Вы ввели точку, которая уже имеется.")
        return

    point_lst.append(a)
    paint_point(a)
    list_box.insert(END, a)
    # print(point_lst)


def del_elem_list(point_lst, a):
    for i in range(len(point_lst)):
        if a == point_lst[i]:
            # print("Нашли: ", point_lst[i])
            for j in range(i, len(point_lst) - 1):
                temp = point_lst[j]
                point_lst[j] = point_lst[j + 1]
                point_lst[j + 1] = temp
            del point_lst[len(point_lst) - 1]
            list_box.delete(i + 1)
            break


def del_point(a):
    if (a[0] == false):
        return

    del_elem_list(point_lst, a)
    canv.delete(ALL)
    paint(canv)

    for i in range(len(point_lst)):
        paint_point(point_lst[i])

    # print(point_lst)


def del_user_point():

    if (len(point_lst) == 0):
        mb.showerror(title="Ошибка ввода", message="Нет точек. ")
        return
    a = check_answer(entry_del_point.get())

    del_point(a)


def clear_all():
    for i in range(len(point_lst), 0, -1):
        list_box.delete(i)
    canv.delete(ALL)
    paint(canv)
    point_lst.clear()

    # print(point_lst)


def change_point():
    point_of = check_answer(entry_change_point_of.get())
    if point_of[0] == false:
        return

    if point_of not in point_lst:
        print_error("Вы ввели точку, которой нет.")
        return

    point_in = check_answer(entry_change_point_in.get())
    if point_in[0] == false:
        return

    if point_of == point_in:
        return

    if point_in in point_lst:
        print_error("Вы ввели точку, которая уже имеется.")
        return

    point_lst.append(point_in)
    list_box.insert(END, point_in)

    # print("Из", point_of, "в", point_in);

    del_point(point_of)
    paint_point(point_in)
    # print(point_lst)


def function_solution():
    if (len(point_lst) < 3):
        print_error("Не хватает точек для решения задачи.")
        return

    max_sum = -1.0

    n = len(point_lst)
    res_point = [0, 0]

    # number_triangles = factorial(n) / (6 * factorial(n - 3))
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # print(point_lst[i], point_lst[j], point_lst[k])
                a, b, c = point_lst[i], point_lst[j], point_lst[k]


                if a[0] == b[0] == c[0]:
                    # print("Точки лежат на одной прямой. (Параллельно оси У)")
                    continue
                if find_coefficients(point_lst[i], point_lst[j]) == find_coefficients(point_lst[j], point_lst[k]):
                    # print("Точки лежат на одной прямой.")
                    continue
                perpendicular = perpendicular_triangles(a, b, c)
                if perpendicular[0] != False:
                    intersection = perpendicular
                    if (distance(intersection) > max_sum):
                        max_sum = distance(intersection)
                        triangles = a, b, c
                        res_point[0], res_point[1] = intersection[0], intersection[1]
                        continue

                line_one = find_coefficients(a, c)
                k = perpendicular_lines(line_one[0])
                line_perpendicular_one = (k, find_coefficients_b(b, k))

                line_two = find_coefficients(b, c)
                k = perpendicular_lines(line_two[0])
                line_perpendicular_two = (k, find_coefficients_b(a, k))

                intersection = find_intersection_point(
                    line_perpendicular_one, line_perpendicular_two)
                # print(intersection)

                if (distance(intersection) > max_sum):
                    max_sum = distance(intersection)
                    triangles = a, b, c
                    res_point[0], res_point[1] = intersection[0], intersection[1]

    # if intersection[0] > max_coordinate || intersection[1] > max_coordinate:
        # mb.showerror(title="Ошибка", message="")
        # return       
    if max_sum == -1:
        mb.showerror(title="Ошибка", message="Нет решения")
        return
    paint_result(triangles[0], triangles[1], triangles[2], intersection)
    answer = mb.showinfo(title="Результат", message="Ура! Нам удалось найти подходящий под \
условие утреугольник! Давайте взглянем на него. Вот его координаты:\
\nA(" + str(round(triangles[0][0], 2)) + ";" +  str(round(triangles[0][1], 2)) +
")\nB(" + str(round(triangles[1][0], 2)) + ";" +  str(round(triangles[1][1], 2)) +
")\nC(" + str(round(triangles[2][0], 2)) + ";" +  str(round(triangles[2][1], 2)) +
")\nТочка пересечения высот:" +
"\nH(" + str(round(intersection[0], 2)) + ";" +  str(round(intersection[1], 2)) +
")\nИ сумма расстояний от точки пересечения высот до осей координат = " + str(round(distance(intersection),2)))


# "Ура! Нам удалось найти подходящий под \
# условие утреугольник! Давайте взглянем на него. Вот его координаты: \
# \nA({:.2f}, {:.2f})\
# \nB({:.2f}, {:.2f})\
# \nC({:.2f}, {:.2f})\
# \nТочка пересечения высот:\
# \nH({:.2f}, {:.2f})\
# \nИ сумма расстояний от точки пересечения высот до осей координат = {:.2f}".format(triangles[0][0], triangles[0][1], triangles[1][0], 
#     triangles[1][1],triangles[2][0], triangles[2][1], intersection[0], intersection[1], distance(intersection)))



def paint(canv):
    # Рисуем координатные оси.
    canv.create_line(0, 400, 800, 400, fill="black", width=2, arrow=LAST,
                     arrowshape="10 20 10")
    canv.create_line(400, 0, 400, 800, fill="black", width=2, arrow=FIRST,
                     arrowshape="10 20 10")

    # Линии.
    for i in range(0, 800, 40):
        canv.create_line(i, 0, i, 800, fill="gray72")
        canv.create_line(0, i, 800, i, fill="gray72")

    # Засечки.
    for i in range(0, 400, 40):
        canv.create_line(i, 390, i, 410)
        if (i-400 and i):
            canv.create_text(i, 420, text=str(i - 400),
                             justify=CENTER, font="Verdana 8")
    for i in range(400, 800, 40):
        canv.create_line(i, 390, i, 410)
        if (i-400 and i):
            canv.create_text(i, 380, text=str(i - 400),
                             justify=CENTER, font="Verdana 8")
    for i in range(0, 400, 40):
        canv.create_line(390, i, 410, i)
        if (i-400 and i):
            canv.create_text(420, i, text=str(-(i - 400)),
                             justify=CENTER, font="Verdana 8")
    for i in range(400, 800, 40):
        canv.create_line(390, i, 410, i)
        if (i-400 and i):
            canv.create_text(380, i, text=str(-(i - 400)),
                             justify=CENTER, font="Verdana 8")

    # my_lable = Label(root, text="Добавить точку:", bg="white", font=(
    #	 "Comic Sans MS", 16, "bold")).place(x=1000, y=50, anchor="center")
if __name__ == "__main__":
    point_lst = []
    correct = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", ".", "-"]
    root = Tk()
    root.title('Геометрическая задача')
    root.geometry("1200x800")
    root.configure(bg="lavender")
    root.resizable(width=false, height=false)

    main_menu = Menu(root)
    root.configure(menu=main_menu)

    third_item = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Инструкция",
                          menu=third_item, font="Verdana 10")
    third_item.add_command(label="Показать инструкцию",
                           command=info_show, font="Verdana 12")

    canv = Canvas(root, width=800, height=800, bg="snow")
    canv.place(x=0, y=0)

    paint(canv)

    button_add = Button(text="Добавить точку", width=15,
                        command=add_point, bg="thistle3")
    button_add.place(x=1000, y=50, anchor="center")
    entry_add = Entry(root, width="50")
    entry_add.place(x=1000, y=100, anchor="center", width=150)

    button_del_all = Button(text="Удалить точку", width=15,
                            command=del_user_point,  bg="thistle3")
    button_del_all.place(x=1000, y=150, anchor="center")
    entry_del_point = Entry(root, width="50")
    entry_del_point.place(x=1000, y=200, anchor="center", width=150)

    button_change = Button(text="Изменить точку", width=15,
                           command=change_point, bg="thistle3")
    button_change.place(x=1000, y=250, anchor="center")
    entry_change_point_of = Entry(root, width="50")
    entry_change_point_of.place(x=800, y=300, anchor="w", width=150)
    label_change = Label(
        root, text="--->", bg="lavender").place(x=950, y=300, anchor="w", width=100)
    entry_change_point_in = Entry(root, width="50")
    entry_change_point_in.place(x=1050, y=300, anchor="w", width=150)

    # label_change = Label(root, text="--->" * 50, bg="lavender").place(x=800, y=300, anchor="w", width=400)
    list_box = Listbox(root, width=48, height=17, bg="lavender")
    list_box.insert(END, "(x y)")
    list_box.place(x=800, y=350)
    scroll = Scrollbar(command=list_box.yview)
    scroll.place(x=1190, y=350, height=310)

    button_solve = Button(text="Решить", width=15,
                          command=function_solution, bg="thistle3")
    button_solve.place(x=1000, y=700, anchor="center")

    button_del_all = Button(text="Стереть всё", width=15,
                            command=clear_all, bg="thistle3")
    button_del_all.place(x=1000, y=750, anchor="center")

    # showerror(), showinfo() и showwarning().
    answer = mb.showinfo(title="Начало работы", message="Добро пожаловать \
    в геометрическую программу, чтобы вам проще было её использовать предлагаю \
    прочитать инструкцию, которая находится в верхнем левом углу.")

    root.mainloop()
