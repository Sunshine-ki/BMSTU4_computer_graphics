#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


def info_show():
    info = Toplevel(root)
    label1 = Label(info, text='информация ' * 10, font=20)
    label1.pack()


def add_point():
    answer = entry_add.get()

    # point_lst.append(map(int, answer.split()))


    print(answer)
    print(point_lst[0])
    # Тут работаем с добавлением точки


def del_point():
    point = entry_del_point.get()
    print(point)


def del_all():
    print("Удаляем все точки")


def clear_all():
    print("Стереть всё")


def change_point():
    point_of = entry_change_point_of.get()
    point_in = entry_change_point_in.get()
    print("Из", point_of, "в", point_in);


def function():
    pass


def paint(c):
    # Рисуем координатные оси.
    c.create_line(0, 400, 800, 400, fill="black", width=2, arrow=LAST,
                  arrowshape="10 20 10")
    c.create_line(400, 0, 400, 800, fill="black", width=2, arrow=FIRST,
                  arrowshape="10 20 10")
    # Засечки
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
    #     "Comic Sans MS", 16, "bold")).place(x=1000, y=50, anchor="center")
if __name__ == "__main__":
    point_lst = []
    root = Tk()
    root.title('Геометрическая задача')
    root.geometry("1200x800")
    root.configure(bg="lavender")
    root.resizable(width=False, height=False)

    main_menu = Menu(root)
    root.configure(menu=main_menu)

    third_item = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Информация", menu=third_item)
    third_item.add_command(label='Показать информацию', command=info_show)

    c = Canvas(root, width=800, height=800, bg="snow")
    c.place(x=0, y=0)

    paint(c)

    button_add = Button(text="Добавить точку", width=15,
                        command=add_point, bg="thistle3")
    button_add.place(x=1000, y=50, anchor="center")
    entry_add = Entry(root, width="50")
    entry_add.place(x=1000, y=100, anchor="center", width=150)

    button_del_all = Button(text="Удалить точку", width=15,
                            command=del_point,  bg="thistle3")
    button_del_all.place(x=1000, y=150, anchor="center")
    entry_del_point = Entry(root, width="50")
    entry_del_point.place(x=1000, y=200, anchor="center", width=150)

    button_change = Button(text="Изменить точку", width=15, command=change_point, bg="thistle3")
    button_change.place(x=1000, y=250, anchor="center")
    entry_change_point_of = Entry(root, width="50")
    entry_change_point_of.place(x=800, y=300, anchor="w", width=150)
    label_change = Label(root, text="--->", bg="lavender").place(x=950, y=300, anchor="w", width=100)
    entry_change_point_in = Entry(root, width="50")
    entry_change_point_in.place(x=1050, y=300, anchor="w", width=150)

    button_solve = Button(text="Решить", width=15,
                          command=function, bg="thistle3")
    button_solve.place(x=1000, y=700, anchor="center")

    button_del_all = Button(text="Стереть всё", width=15,
                            command=clear_all, bg="thistle3")
    button_del_all.place(x=1000, y=750, anchor="center")

    root.mainloop()
