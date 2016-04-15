def sqrt(x):
    """Returns square root of X
    :param x:
    :return:

    Returns a float

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
    >>> sqrt(Fraction(16,4))
    2
    """
    if type(x) is complex:
        return x ** 0.5
    try:
        x = float(x)
    except:
        raise TypeError("{0} is not a number".format(str(x)))
    if x < 0:
        return sqrt(abs(x)) * 1j
    return x ** 0.5


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


def abs(x):
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
    if type(x) is complex:
        return sqrt(pow(x.real, 2) + pow(x.imag, 2))
    try:
        x = float(x)
    except:
        raise TypeError("{0} is not a number".format(str(x)))
    if x > 0:
        return x
    else:
        return -x


def fac(x):
    # type: (int) -> int
    """
    Finds x factorial
    :param x: integer
    :return: x factorial

    >>> fac(0)
    1
    >>> fac(5)
    120
    """
    if type(x) is not int:
        raise TypeError("A integer is required")
    if x == 0:
        return 1
    elif x < 0:
        raise TypeError("Not for negative values")
    else:
        return x * fac(x - 1)
