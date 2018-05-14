import amath.ext._basic as _b
from amath.ext._basic import log

from amath.constants import e


def ln(x):
    return log(x, e)


def exp(x):
    """
    returns e^X
    :param x: exponent
    :return: float
    >>> exp(1)
    2.718281828459045
    """
    return pow(e, x)


# noinspection PyShadowingBuiltins
def pow(x, y, m=None):
    """
    X to the Y power
    :param m:
    :param x:
    :param y:
    :return:

    >>> pow(2,3)
    8
    >>> pow(5,-1)
    0.2
    >>> pow(25,0.5)
    5.0
    >>> pow(5, 2, 4)
    1
    """
    try:
        return _b.pow(x, y, m)
    except TypeError:
        try:
            x = float(x)
        except:
            try:
                x = complex(x)
            except:
                raise TypeError("{0}{1} cannot be raised to the {2}{3} power".format(type(x), x, type(y), y))

        try:
            y = float(y)
        except:
            try:
                y = complex(y)
            except:
                raise TypeError("{0}{1} cannot be raised to the {2}{3} power".format(type(x), x, type(y), y))

        if m is not None:
            try:
                m = float(m)
            except:
                try:
                    m = complex(m)
                except:
                    raise TypeError("{0}{1} cannot be raised to the {2}{3} power".format(type(x), x, type(y), y))
        try:
            return _b.pow(x, y, m)
        except ValueError:
            if isinstance(y, float):
                from amath.DataTypes.Fraction import dectofr
                y = dectofr(y)
                return _b.pow(x, y, m)
    except ValueError:
        if isinstance(y, float):
            from amath.DataTypes.Fraction import dectofr
            y = dectofr(y)
            return _b.pow(x, y, m)


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
        ...
    ZeroDivisionError: float division by zero
    >>> root(-8, 3)
    -2.0
    >>> root(4j, 2)
    (1.4142135623730951+1.4142135623730951j)
    """
    if type(x) is complex:
        return x ** (1.0 / y)
    if type(y) is complex:
        return x ** (1.0 / y)
    try:
        x = float(x)
    except:
        raise TypeError("{0} is not a number".format(x))
    try:
        y = float(y)
    except:
        raise TypeError("{0} is not a number".format(y))
    if x < 0 and y % 2 == 0:
        return root(abs(x), y) * 1j
    elif x < 0:
        return -root(abs(x), y)
    return x ** (1.0 / y)

# def expm1(x):
#
#     if abs(x) < 1e-5:
#         return x + 0.5 * x * x
#     else:
#         return exp(x) - 1.0
