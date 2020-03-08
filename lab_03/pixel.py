#!/usr/bin/python
# -*- coding: utf-8 -*-


# from tkinter import Tk, Canvas, PhotoImage, mainloop
# from math import sin

# WIDTH, HEIGHT = 640, 480

# window = Tk()
# canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
# canvas.pack()
# img = PhotoImage(width=WIDTH, height=HEIGHT)
# canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

# for x in range(4 * WIDTH):
#     y = int(HEIGHT/2 + HEIGHT/4 * sin(x/80.0))
#     img.put("#ffffff", (x//4, y))

# # canvas.create_image((WIDTH/2, HEIGHT/2), image=img) # Что-то для сохранения ссылки.
# # canvas.image = img

# mainloop()

from tkinter import *
root = Tk()
l1 = Label(text="Машинное обучение", font="Arial 32")
l2 = Label(text="Распознавание образов", font=("Comic Sans MS", 24, "bold"))
l1.config(bd=20, bg='#ffaaaa')
l2.config(bd=20, bg='#aaffff')
l1.pack()
l2.pack()
root.mainloop()
