from math import fabs


def find_intersections(canvas_class, start, stop, lst):
    if stop[1] == start[1]:
        return

    if start[1] > stop[1]:
        start, stop = stop, start

    dy = 1
    dx = (stop[0] - start[0]) / (stop[1] - start[1])
    x = start[0]
    y = start[1]

    while y < stop[1]:
        lst.append([int(x), int(y)])
        y += dy
        x += dx


def fill(canvas_class, lst):
    septum = lst[len(lst) // 2][0]
    print(septum)
    for i in range(len(lst)):
        if lst[i][0] < septum:
            for j in range(lst[i][0] + 1, septum + 1):
                canvas_class.reverse_pixel(j, lst[i][1])
        elif lst[i][0] > septum:
            for j in range(lst[i][0], septum, -1):
                canvas_class.reverse_pixel(j, lst[i][1])


def delayed_fill(canvas_class, lst):
    septum = lst[len(lst) // 2][0]
    print(septum)
    for i in range(len(lst)):
        if lst[i][0] < septum:
            for j in range(lst[i][0] + 1, septum + 1):
                canvas_class.canvas.after(
                    1, canvas_class.reverse_pixel(j, lst[i][1]))
                canvas_class.canvas.update()
        elif lst[i][0] > septum:
            for j in range(lst[i][0], septum, -1):
                canvas_class.canvas.after(
                    1, canvas_class.reverse_pixel(j, lst[i][1]))
                canvas_class.canvas.update()
