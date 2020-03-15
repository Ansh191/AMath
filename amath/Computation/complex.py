from .Basic import sqrt
from .trig import arctan2, arccos, cos, sin


def arg(z: complex):
    x = z.real
    y = z.imag
    return arctan2(y, x)


def complex_to_polar(z: complex):
    x = z.real
    y = z.imag
    r = sqrt(x ** 2 + y ** 2)
    angle = arccos(x / r)
    return r, angle


def polar_to_complex(r, angle):
    return r * cos(angle) + r * sin(angle) * 1j
