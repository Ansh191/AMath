import _basic as _b


def sqrt(x):
    # type: (complex) -> complex
    # type: (float) -> float
    # type: (int) -> float
    """Returns square root of X
    :param x:
    :return: float


    >>> sqrt(16)
    4.0
    >>> sqrt(25)
    5.0
    >>> sqrt(2)
    1.4142135623730951

    If X is negative, Returns a complex number

    >>> sqrt(-1)
    1j
    >>> sqrt(-16)
    4j

    Can accept Fractions and floats

    >>> sqrt(5.5)
    2.345207879911715
    >>> from amath.DataTypes.Fraction import Fraction
    >>> sqrt(Fraction(25,4))
    5/2
    """
    try:
        ans = _b.sqrt(x)
    except ValueError:
        raise TypeError("{0} is not a number".format(str(x)))

    if ans != ans:
        return sqrt(abs(x)) * 1j
    else:
        return ans


def d(*x):
    """
    Division
    :param x:
    :return:

    >>> d(10,2)
    5.0
    >>> d(10,2,5)
    1.0
    """
    z = []
    for i in x:
        z.append(i)
    y = z[0]
    z.remove(y)
    for i in z:
        y /= float(i)
    return y


def a(*x):
    """
    addition
    ========
    :param x: tuple
    :return:

    >>> a(5,2)
    7
    >>> a(2,-3)
    -1

    Multiple numbers can be inputed as well

    >>> a(2,5,3)
    10
    >>> a(-2,-3,2)
    -3
    """
    z = []
    for i in x:
        z.append(i)
    y = z[0]
    z.remove(y)
    for i in z:
        y += i
    return y


def m(*x):
    z = []
    for i in x:
        z.append(i)
    y = z[0]
    z.remove(y)
    for i in z:
        y *= i
    return y


def s(*x):
    z = []
    for i in x:
        z.append(i)
    y = z[0]
    z.remove(y)
    for i in z:
        y -= i
    return y


# noinspection PyShadowingBuiltins
def abs(x):
    # type: (int) -> float
    # type: (float) -> float
    # type: (complex) -> float
    """
    Returns the absolute value of a float
    :param x: float, int, complex
    :return: absolute value of x

    >>> abs(5)
    5
    >>> abs(-5)
    5
    >>> abs(-5.2)
    5.2
    >>> abs(5.2)
    5.2

    Complex is different

    >>> abs(1j)
    1.0
    >>> abs(-532j)
    532.0
    """
    try:
        return _b.abs(x)
    except AttributeError:
        try:
            return x.__abs__()
        except AttributeError:
            raise TypeError("{0} is not a number".format(str(x)))


def fac(x):
    # type: (float) -> float
    """
    Finds x factorial
    :param x: integer
    :return: x factorial

    >>> fac(0)
    1
    >>> fac(5)
    120
    """
    from amath.constants import Cinf
    if x == 0:
        return 1.0
    elif x < 0:
        return Cinf
    else:
        return x * gamma(x)


# TODO-Allow gamma to accept complex numbers
def gamma(x):
    # type: (float) -> float
    return _b.gamma(x)


def N():
    pass
