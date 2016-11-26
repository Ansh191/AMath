import _basic as _b
# from _basic import log, ln, log2, log10

def sqrt(x):
    # type: (int) -> float
    # type: (float) -> float
    # type: (complex) -> complex
    """Returns square root of X
    :type x: object
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
        return _b.sqrt(x)  # call the c-api
    except TypeError:
        raise TypeError("{0} is not a number".format(str(x)))  # if it failed, x is not a number
    except ValueError:
        return sqrt(abs(x)) * 1j  # x is negative
    except:  # in case of _basic failure
        if isinstance(x, complex):
            return x ** 0.5
        if x < 0:
            return sqrt(abs(x)) * 1j
        return x ** 0.5


# noinspection PyShadowingBuiltins
def abs(x):
    # type: (float) -> float
    # type: (int) -> float
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
        return _b.abs(x)  # call c-api
    except:
        try:
            return x.__abs__()  # if c-api fails, run __abs__ function
        except AttributeError:
            raise TypeError("{0} is not a number".format(str(x)))  # x is then not a valid number


# TODO-Look at gamma
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
# TODO-Allow gamma to take larger numbers
def gamma(x):
    # type: (float) -> float
    t = False
    y = 0.0
    try:
        y = _b.gamma(x)  # call c-api
    except:
        t = True
    from amath.stats.stats import product
    from amath.DataTypes.Function import Function
    if x >= 170 or t:  # to not overflow float or if in _basic failure
        if isinstance(x, int) or isinstance(x, long):  # x must be an int
            return product(Function("k", "k"), 1, x) / x
        else:
            raise TypeError("For values over 170, x must be a integer")
    else:
        if isinstance(x, int) or isinstance(x, long) or int(x) == x:
            return int(y)
        else:
            return y


def N():
    return NotImplemented
