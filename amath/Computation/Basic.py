import amath.ext._basic as _b


def sqrt(x):
    # type: (object) -> float
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
        try:
            return _b.sqrt(float(x))
        except ValueError:
            try:
                return _b.sqrt(complex(x))
            except ValueError:
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
            return _b.abs(float(x))
        except ValueError:
            try:
                return _b.abs(complex(x))
            except ValueError:
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
    1.0
    >>> fac(5)
    120
    >>> fac(0.5)
    0.886226925452758
    >>> fac(float("inf"))
    inf
    """
    x = float(x)
    if x == 0:
        return 1.0
    elif x < 0:
        from amath.constants import Cinf
        return Cinf
    else:
        if x > 170:
            x = int(x)
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
    from amath.DataTypes import Infinity
    from amath.testing.types import isinf, isnan, intQ
    x = int(x)
    if x >= 170 or t:  # to not overflow float or if in _basic failure
        if intQ(x):  # x must be an int
            from amath.stats.stats import product
            return product(lambda k: k, 1, x) // x
        elif isinf(x):
            if x > 0:
                return Infinity(True)
            else:
                from amath.Errors import Indeterminate
                raise Indeterminate()
        else:
            raise TypeError("For values over 170, x must be a integer")
    else:
        if isinf(y) or isnan(y):
            return Infinity(None)
        elif isinstance(x, int) or int(x) == x:
            return int(y)
        else:
            return y


# @lru_cache(1024)
def fib(n):
    try:
        y = _b.fib(n)
    except:
        y = float("inf")

    if y == float("inf"):
        from amath.constants import gr, pi
        from .trig import cos
        n = float(n)
        return int(int(gr ** n - cos(n * pi) / gr ** n) / sqrt(5))
    else:
        return y


def N():
    return NotImplemented
