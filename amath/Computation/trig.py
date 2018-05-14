import amath.ext._trig as _t

from amath.constants import e, pi


def degtorad(d):
    return (d * pi) / 180


def radtodeg(r):
    return (r * 180) / pi


def sin(a):
    if a == pi:
        return 0
    try:
        return _t.sin(a)
    except TypeError:
        return (e ** (1j * a)).imag


def cos(a):
    """
    Return the Cosine of x
    :param a:
    :return:
    """
    try:
        return _t.cos(a)
    except TypeError:
        return (e ** (1j * a)).real


def tan(a):
    """Returns tan(a)"""
    try:
        return _t.tan(a)
    except TypeError:
        return (sin(a)) / cos(a)


def cot(a):
    """Returns cotangent(a)"""
    answer = (cos(a)) / (sin(a))
    return answer


def sec(a):
    """Returns secant(a)"""
    answer = 1.00 / cos(a)
    return answer


def csc(a):
    """Returns the cosecant of a"""
    return 1.00 / sin(a)


def arcsin(a):
    return _t.asin(a)


def arccos(a):
    try:
        return _t.acos(a)
    except TypeError:
        return (pi / 2.0) - arcsin(a)


def arctan(a):
    return _t.atan(a)


def arccot(a):
    try:
        return _t.acot(a)
    except TypeError:
        return arctan(1.0 / a)


def arcsec(a):
    try:
        return _t.asec(a)
    except TypeError:
        return arccos(1.0 / a)


def arccsc(a):
    try:
        return _t.acsc(a)
    except TypeError:
        return arcsin(1 / a)
