

# def parametric_ellipse(canvas, center, radius, axis, color_line):
# pass


def draw_ellipse(canvas, method, center, radius, axis, color_line):
    print("method = ", method)
    print("center, radius, axis", center, radius, axis)
    if method == 0:
        print("Канонический")
    elif method == 1:
        print("Параметрический")
        parametric_ellipse(canvas, center, radius, color_line)
    elif method == 2:
        pass
    elif method == 3:
        pass
    elif method == 4:
        print("Библиотечный")
        canvas.create_oval(center[0] - radius, center[1] - radius,
                           center[0] + radius, center[1] + radius, width=2)
