from math import pi, sin, cos

from constants import *


def convers(arg):
    return arg * pi / 180


def rotateX(x, y, z, angle):
    angle = convers(angle)
    y = cos(angle) * y - sin(angle) * z
    return x, y


def rotateY(x, y, z, angle):
    angle = convers(angle)
    x = cos(angle) * x - sin(angle) * z
    return x, y


def rotateZ(x, y, z, angle):
    angle = convers(angle)
    buf = x
    x = cos(angle) * x - sin(angle) * y
    y = cos(angle) * y + sin(angle) * buf
    return x, y


def rotate(x, y, z, angle_x, angle_y, angle_z):
    x, y = rotateX(x, y, z, DEFAULT_ANGLE_X)
    x, y = rotateY(x, y, z, DEFAULT_ANGLE_Y)
    x, y = rotateZ(x, y, z, DEFAULT_ANGLE_Z)
    return x, y
