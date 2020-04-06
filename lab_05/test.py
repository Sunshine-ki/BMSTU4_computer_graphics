from tkinter import *
root = Tk()
c = Canvas(width=300, height=300, bg='white')
c.focus_set()
c.pack()


def print_points_on_board(event, f):
    c.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5,
                  fill="#6515A2", activefill='black')
    print(event.x, event.y)


ball = c.create_oval(140, 140, 160, 160, fill='green')
c.bind('<Up>', lambda event: c.move(ball, 0, -4))
c.bind('<Down>', lambda event: c.move(ball, 0, 4))
c.bind('<Left>', lambda event: c.move(ball, -4, 0))
c.bind('<Right>', lambda event: c.move(ball, 4, 0))

c.bind('<Button-1>', lambda event, f="Verdana": print_points_on_board(event, f))

root.mainloop()
