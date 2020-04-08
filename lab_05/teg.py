from tkinter import *

color_bg = 'white'
color_line = 'black'


def create_canvas():
    for i in range(800):
        for j in range(800):
            canvas.create_line(round(i), round(j), round(
                i), round(j) + 1, width=1, fill=color_bg, tags=str(i) + 'x' + str(j) + 'b')

    print("END")


def reverse_color(str_color):
    print(str_color, str_color[-1])
    if str_color[-1] == 'b':
        return str_color[-1]


def color(event):
    print(event.x, event.y)
    x = event.x
    y = event.y

    if len(canvas.gettags(str(x) + 'x' + str(y) + 'b')) != 0:
        canvas.itemconfig(str(x) + 'x' + str(y) + 'b',
                          tags=str(x) + 'x' + str(y) + 'l', fill=color_line)
        return

    if len(canvas.gettags(str(x) + 'x' + str(y) + 'l')) != 0:
        canvas.itemconfig(str(x) + 'x' + str(y) + 'l',
                          tags=str(x) + 'x' + str(y) + 'b', fill=color_bg)
        return


root = Tk()
canvas = Canvas(width=800, height=800, bg=color_bg)
canvas.focus_set()
canvas.pack()

create_canvas()

canvas.bind('<Button-1>', color)


root.mainloop()
