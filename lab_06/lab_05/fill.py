from math import fabs


def sign(a):
    if a == 0:
        return 0
    return a / abs(a)


def bresenham_int(canvas_class, start, stop, lst):
    dx = stop[0] - start[0]
    dy = stop[1] - start[1]
    x, y = start[0], start[1]
    sx, sy = sign(dx), sign(dy)
    dx = fabs(dx)
    dy = fabs(dy)

    swap = 0

    if dy > dx:
        swap = 1
        dx, dy = dy, dx

    e = 2 * dy - dx

    for _ in range(int(dx + 1)):

        canvas_class.print_pixel(int(x), int(y))
        if e >= 0:
            if swap == 0:
                y += sy
                if start[1] != stop[1] and [int(x), int(y)] not in lst:
                    lst.append([int(x), int(y)])
            else:
                x += sx
            e -= (2 * dx)

        if e < 0:
            if swap == 0:
                x += sx
            else:
                y += sy
                if start[1] != stop[1] and [int(x), int(y)] not in lst:
                    lst.append([int(x), int(y)])
            e += (2 * dy)
    # print(lst)


def fill(canvas_class, lst):
    septum = lst[len(lst) // 2][0]
    print(septum)
    for i in range(len(lst)):
        if lst[i][0] < septum:
            for j in range(lst[i][0], septum + 1):
                canvas_class.reverse_pixel(j, lst[i][1])
        elif lst[i][0] > septum:
            for j in range(lst[i][0], septum, -1):
                canvas_class.reverse_pixel(j, lst[i][1])


def delayed_fill(canvas_class, lst):
    # for i in range(len(lst)):
    #     for j in range(lst[i][0], WIDTH):
    #         canvas_class.canvas.after(
    #             1, canvas_class.reverse_pixel(j, lst[i][1]))
    #         canvas_class.canvas.update()
    septum = lst[len(lst) // 2][0]
    print(septum)
    for i in range(len(lst)):
        if lst[i][0] < septum:
            for j in range(lst[i][0], septum + 1):
                canvas_class.canvas.after(
                    1, canvas_class.reverse_pixel(j, lst[i][1]))
                canvas_class.canvas.update()
        elif lst[i][0] > septum:
            for j in range(lst[i][0], septum, -1):
                canvas_class.canvas.after(
                    1, canvas_class.reverse_pixel(j, lst[i][1]))
                canvas_class.canvas.update()
