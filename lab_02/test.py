from math import *
from tkinter import *

def func_x(t):
	return 10 * cos(t)

def func_y(t):
	return 10 * sin(t)

def func(x):
	return x * x

root = Tk()

canv = Canvas(root, width = 1000, height = 1000, bg = "white")
canv.create_line(500,1000,500,0,width=2,arrow=LAST) 
canv.create_line(0,500,1000,500,width=2,arrow=LAST) 

First_x = -500;

for i in range(16000):
	try:
		x = First_x + (1 / 16) * i
		y = -func(x) + 500
		x += 500
		print(func_x(x), )
		canv.create_oval(x, y, x + 1, y + 1, fill = 'black')
	except:
		pass
canv.pack()	
root.mainloop()