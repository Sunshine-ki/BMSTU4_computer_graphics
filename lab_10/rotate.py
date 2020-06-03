from math import pi, sin, cos
from constants import *

def scale(x, y):
    x *= SCALE
    y *= SCALE
    x += WIDTH // 2
    y += HEIGHT // 2 # - y
    return round(x), round(y)
    
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


def transform(x, y, z, angles):
    x, y = rotateX(x, y, z, angles[0])
    x, y = rotateY(x, y, z, angles[1])
    x, y = rotateZ(x, y, z, angles[2])
    return scale(x, y)

