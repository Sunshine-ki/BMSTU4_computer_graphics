#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import fabs
from tkinter import *
from tkinter import messagebox as mb

max_coordinate = 400
radius_point = 5
false = -1000


def info_show():
    info = Toplevel(root)
    label1 = Label(info, text='информация ' * 10, font=20)
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
    c.create_oval(a[0] - radius_point + 400, fabs(a[1] - radius_point - 400),
                  a[0] + radius_point + 400, fabs(a[1] + radius_point - 400), width=2, fill='red', outline='black')  # ,tag = "x" + str(len(point_lst)))# tag=str(a[0])+" "+str(a[1]))


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

    print(point_lst)


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
    c.delete(ALL)
    paint(c)

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
    c.delete(ALL)
    paint(c)
    point_lst.clear()

    print(point_lst)


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


def function():
    pass


def paint(c):
    # Рисуем координатные оси.
    c.create_line(0, 400, 800, 400, fill="black", width=2, arrow=LAST,
                  arrowshape="10 20 10")
    c.create_line(400, 0, 400, 800, fill="black", width=2, arrow=FIRST,
                  arrowshape="10 20 10")

    # Линии.
    for i in range(0, 800, 40):
        c.create_line(i, 0, i, 800, fill="gray72")
        c.create_line(0, i, 800, i, fill="gray72")

    # Засечки.
    for i in range(0, 400, 40):
        c.create_line(i, 390, i, 410)
        if (i-400 and i):
            c.create_text(i, 420, text=str(i - 400),
                          justify=CENTER, font="Verdana 8")
    for i in range(400, 800, 40):
        c.create_line(i, 390, i, 410)
        if (i-400 and i):
            c.create_text(i, 380, text=str(i - 400),
                          justify=CENTER, font="Verdana 8")
    for i in range(0, 400, 40):
        c.create_line(390, i, 410, i)
        if (i-400 and i):
            c.create_text(380, i, text=str(i - 400),
                          justify=CENTER, font="Verdana 8")
    for i in range(400, 800, 40):
        c.create_line(390, i, 410, i)
        if (i-400 and i):
            c.create_text(420, i, text=str(i - 400),
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
    main_menu.add_cascade(label="Инструкция", menu=third_item)
    third_item.add_command(label="Показать инструкцию", command=info_show)

    c = Canvas(root, width=800, height=800, bg="snow")
    c.place(x=0, y=0)

    paint(c)

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
                          command=function, bg="thistle3")
    button_solve.place(x=1000, y=700, anchor="center")

    button_del_all = Button(text="Стереть всё", width=15,
                            command=clear_all, bg="thistle3")
    button_del_all.place(x=1000, y=750, anchor="center")

    # showerror(), showinfo() и showwarning().
    # answer = mb.showinfo(title="Начало работы", message="Добро пожаловать \
    # в геометрическую программу, чтобы вам проще было её использовать предлагаю \
    # прочитать инструкцию, которая находится в верхнем левом углу.")

    root.mainloop()
