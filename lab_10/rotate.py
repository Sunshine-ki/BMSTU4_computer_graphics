from math import pi, sin, cos


def rotateX(x, y, z, teta):
    teta = teta * pi / 180
    buf = y
    y = cos(teta) * y - sin(teta) * z
    z = cos(teta) * z + sin(teta) * buf
    return x, y, z


def rotateY(x, y, z, teta):
    teta = teta * pi / 180
    buf = x
    x = cos(teta) * x - sin(teta) * z
    z = cos(teta) * z + sin(teta) * buf
    return x, y, z


def rotateZ(x, y, z, teta):
    teta = teta * pi / 180
    buf = x
    x = cos(teta) * x - sin(teta) * y
    y = cos(teta) * y + sin(teta) * buf
    return x, y, z


def tranform(x, y, z, tetax, tetay, tetaz):
    x, y, z = rotateX(x, y, z, tetax)
    x, y, z = rotateY(x, y, z, tetay)
    x, y, z = rotateZ(x, y, z, tetaz)
    return round(x), round(y), round(z)
