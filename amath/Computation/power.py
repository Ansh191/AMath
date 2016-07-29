from __future__ import print_function, division
from amath.constants import e


def exp(x):
    """
    returns e^X
    :param x: exponent
    :return: float
    >>> exp(1)
    2.718281828459045
    """
    return e ** x


# noinspection PyShadowingBuiltins
def pow(x, y):
    """
    X to the Y power
    :param x:
    :param y:
    :return:

    >>> pow(2,3)
    8
    >>> pow(5,-1)
    0.2
    >>> pow(25,0.5)
    5.0
    """
    return x ** y


def root(x, y):
    """
    Returns y Root of X
    :param x:
    :param y:
    :return:
    >>> root(8,3)
    2.0
    >>> root(4,-2)
    0.5
    >>> root(0,2)
    0.0
    >>> root(2,0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    >>> root(-8, 3)
    2j
    >>> root(8j, 3)
    2j
    """
    if type(x) is complex:
        return x ** (1.0 / y)
    try:
        x = float(x)
    except:
        raise TypeError("{0} is not a number".format(x))
    if x < 0:
        return root(abs(x), y) * 1j
    return x ** (1.0 / y)


def expm1(x):
    if abs(x) < 1e-5:
        return x + 0.5 * x * x
    else:
        return exp(x) - 1.0


# TODO-everyone work on log
def log(x, base, error=0.000001):
    """Returns log of x"""
    return float(ln(x, error)) / float(ln(base, error))


def ln(z, error=0.000001):
    if z <= 0:
        raise ValueError("math domain error")

    x = 0
    y = e ** x
    minimum = 0
    maximum = 0
    Begin = True
    while True:
        if y == z:
            return x
        elif (z - error) < y < (z + error):
            return x

        if z > 1:
            if y < z:
                if Begin is True:
                    minimum = x
                    x += 1
                else:
                    minimum = x
                    x = (minimum + maximum) / 2.0
            elif y > z:
                Begin = False
                maximum = x
                x = (minimum + maximum) / 2.0

        else:
            if y > z:
                if Begin is True:
                    maximum = x
                    x -= 1
                else:
                    maximum = x
                    x = (minimum + maximum) / 2.0
            elif y < z:
                Begin = False
                minimum = x
                x = (minimum + maximum) / 2.0

        y = e ** x
