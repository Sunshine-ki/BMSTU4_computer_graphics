def reflection_z(list_points, center):
    n = len(list_points)

    for i in range(n):
        x = list_points[i][0] - center[0]
        y = list_points[i][1] - center[1]
        x, y = y, x
        x += center[0]
        y += center[1]
        list_points.append([x, y])


def reflection_y(list_points, center):
    n = len(list_points)

    for i in range(n):
        x = list_points[i][0] - center[0]
        y = list_points[i][1] - center[1]
        x *= -1
        x += center[0]
        y += center[1]
        list_points.append([x, y])


def reflection_x(list_points, center):
    n = len(list_points)

    for i in range(n):
        x = list_points[i][0] - center[0]
        y = list_points[i][1] - center[1]
        y *= -1
        x += center[0]
        y += center[1]
        list_points.append([x, y])


def symmetrical_reflection(list_points, center):
    reflection_z(list_points, center)
    reflection_y(list_points, center)
    reflection_x(list_points, center)
