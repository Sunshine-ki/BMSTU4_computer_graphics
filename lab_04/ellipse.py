

# def parametric_ellipse(center, axis):
# pass


def draw_ellipse(canvas_class, method, center, axis):
    print("method = ", method)
    print("center, axis", center, axis)
    print("color_line = ", canvas_class.color_line)

    list_points = list()

    if method == 0:
        print("Канонический")
        # canonical_circle(center, radius)
    elif method == 1:
        print("Параметрический")
    elif method == 2:
        pass
    elif method == 3:
        pass
    elif method == 4:
        print("Библиотечный")
        canvas_class.draw_oval(
            center[0] - axis[0], center[1] - axis[1], center[0] + axis[0], center[1] + axis[1])
        # canvas_class.draw_oval(
        # center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius)

    canvas_class.draw_figure(list_points)
