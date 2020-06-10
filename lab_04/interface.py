from tkinter import *
from tkinter import messagebox as mb


def print_error(string_error):
    mb.showerror(title="Ошибка", message=string_error)


def create_button(str, function, coordinates):
    button = Button(text=str, width=40,
                    command=function,  bg="thistle3")
    button.place(x=coordinates[0], y=coordinates[1], anchor="center")


def create_label(root, str, coordinates):
    label = Label(root, text=str, bg="lavender", width=25,
                  font="Verdana 12")
    label.place(x=coordinates[0], y=coordinates[1], anchor="center", width=200)


def settings_interface(root, size, title):
    root.title(title)
    root.geometry(size)
    root.configure(bg="lavender")
    root.resizable(width=False, height=False)


def selection(count, list_text, coordinates):
    # Выбор.
    var = IntVar()
    var.set(0)
    list_method = list()

    for i in range(count):
        method = Radiobutton(text=list_text[i], variable=var,
                             value=i, bg="lavender", width=25, font="Verdana 12")
        method.place(x=coordinates[0],
                     y=coordinates[1] + 25 * i, anchor="center")
        list_method.append(method)

    return var


def create_entry(root, coordinates):
    entry = Entry(root, width="50")
    entry.place(x=coordinates[0], y=coordinates[1], anchor="center", width=150)
    return entry
