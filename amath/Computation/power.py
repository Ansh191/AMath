try:
    import amath.ext._basic as _b
    from amath.ext._basic import log
except ImportError:
    print("_b failed to import")

import amath.constants as const


def ln(x):
    """Find natural log of x

    :param x: Number
    :return: Natural log of x

    >>> ln(e)
    1.0
    """
    return log(x, const.e)


def exp(x):
    """returns e^x

    :param x: exponent
    :return: e^x

    >>> exp(1)
    2.718281828459045
    """
    return pow(const.e, x)


# noinspection PyShadowingBuiltins
def pow(b, e, m=None):
    """
    b to the e power
    Optional modulus to do modular exponentiation

    :param b: Base
    :param e: Exponent
    :param m: Modulus
    :return: x^y or x^y mod m

    >>> pow(2,3)
    8
    >>> pow(5,-1)
    0.2
    >>> pow(25,0.5)
    5.0
    >>> pow(5, 2, 4)
    1
    >>> pow(2, 2342, 402)
    100
    """
    try:
        return _b.pow(b, e, m)
    except (TypeError, ValueError):
        if m is None:
            return b ** e
        if m == 1:
            return 0
        c = 1
        b %= m
        while e > 0:
            if e % 2 == 1:
                c = (c * b) % m
            e >>= 1
            b = (b * b) % m
        return c


def root(x, y, precision=20):
    """
    Returns y Root of X
    :param x:
    :param y:
    :return:
    >>> root(8,3)
    2.0
    >>> root(4,-2)
    0.5
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
    elif y < 0:
        return x ** (1.0 / y)

    if int(x) == x:
        x = int(x)
    if int(y) == y:
        y = int(y)
    # return x ** (1.0 / y)

    f = lambda n: n ** y - x
    fprime = lambda n: y * n ** (y - 1)

    guess = 10
    change = 1

    while change > 10 ** -precision:
        guess2 = guess - f(guess) / fprime(guess)
        change = abs(guess2 - guess)
        guess = guess2

    return guess

# def expm1(x):
#
#     if abs(x) < 1e-5:
#         return x + 0.5 * x * x
#     else:
#         return exp(x) - 1.0
