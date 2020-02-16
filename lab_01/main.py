#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


def info_show():
    info = Toplevel(root)
    label1 = Label(info, text='информация ' * 10, font=20)
    label1.pack()


def main():
    root = Tk()
    root.title('Геометрическая задача')
    root.geometry("1200x900")
    root.configure(bg='white')
    root.resizable(width=False, height=False)

    c = Canvas(root, width=800, height=800, bg='yellow')
    c.grid(row=0, column=0, columnspan=2, rowspan=8)
    my_lable = Label(root, text="Добавить точку:", bg="white", font=(
        "Comic Sans MS", 16, "bold"), anchor="center").grid(row=0, column=3)

    my_entry = Entry(root, width=10)
    my_entry.grid(row=1, column=3)
    # my_lable = Label(root, text="Добавить точку:", bg=.grid(row=1, column=3)"white", font=(
        # "Comic Sans MS", 16, "bold"), anchor="center").grid(row=1, column=3)

    my_lable = Label(root, text="Добавить точку:", bg="white", font=(
        "Comic Sans MS", 16, "bold"), anchor="center").grid(row=2, column=3)
    my_lable = Label(root, text="Добавить точку:", bg="white", font=(
        "Comic Sans MS", 16, "bold"), anchor="center").grid(row=3, column=3)
    my_lable = Label(root, text="Добавить точку:", bg="white", font=(
        "Comic Sans MS", 16, "bold"), anchor="center").grid(row=4, column=3)
    my_lable = Label(root, text="Добавить точку:", bg="white", font=(
        "Comic Sans MS", 16, "bold"), anchor="center").grid(row=5, column=3)
    my_lable = Label(root, text="Добавить точку:", bg="white", font=(
        "Comic Sans MS", 16, "bold"), anchor="center").grid(row=6, column=3)
    my_lable = Label(root, text="Добавить точку:", bg="white", font=(
        "Comic Sans MS", 16, "bold"), anchor="center").grid(row=7, column=3)
            
    # my_entry = Entry(root, width=100)
    # my_entry.grid(row=0, column=3)

    main_menu = Menu(root)
    root.configure(menu=main_menu, bg='#ffffff')

    third_item = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Информация", menu=third_item)
    third_item.add_command(label='Показать информацию', command=info_show)

    root.mainloop()


if __name__ == "__main__":
    main()


# c = Canvas(root, width=200, height=200, bg='white')
# c.pack()

# c.create_line(10, 10, 190, 50)

# c.create_line(100, 180, 100, 60, fill='green',
#               width=5, arrow=LAST, dash=(10, 2),
#               activefill='lightgreen',
#               arrowshape="10 20 10")

# root.mainloop()
