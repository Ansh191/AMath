from amath.Computation.power import root


def evenQ(x):
    # type: (int) -> bool
    """
    Checks if x is even
    :param x:
    :return:

    >>> evenQ(5)
    False
    >>> evenQ(6)
    True
    >>> evenQ(5.5)
    Traceback (most recent call last):
    ValueError: A integer is required
    """
    if type(x) != int:
        raise ValueError("A integer is required")
    if x % 2 == 0:
        return True
    else:
        return False


def oddQ(x):
    if type(x) != int:
        raise ValueError("A integer is required")
    if x % 2 == 1:
        return True
    else:
        return False


# def compositeQ(x):
#     """
#     Tests if X is compisite
#     :param x:
#     :return: boolean
#
#     >>> compositeQ(5)
#     False
#     >>> compositeQ(2.5)
#     False
#     >>> compositeQ(6)
#     True
#     >>> compositeQ(0)
#     False
#     >>> compositeQ(-2)
#     False
#     """
#     if type(x) is int:
#         if x > 0:
#             if not primeQ(x):
#                 return True
#             else:
#                 return False
#     return False


# def primeQ(x):
#     """
#     Checks if X is prime
#     :param x: suspected prime
#     :return: boolean
#
#     >>> primeQ(5)
#     True
#     >>> primeQ(2)
#     True
#     >>> primeQ(1)
#     False
#     >>> primeQ(-5)
#     False
#     >>> primeQ(20)
#     False
#     >>> primeQ(5.5)
#     Traceback (most recent call last):
#     TypeError: 5.5 is not an integer
#     """
#     if type(x) is not int:
#         raise TypeError(str(x) + " is not an integer")
#     if x > 1:
#         if int(x) == x:
#             for i in range(2, x):
#                 if (x % i) == 0:
#                     return False
#             return True
#     return False


def isPro(x, y):
    if type(x) != list:
        raise TypeError("x must be a list")
    if type(y) != list:
        raise TypeError("y must be a list")
    if len(x) < 2:
        raise ValueError("length of lists must be greater than 1")
    if len(x) != len(y):
        raise TypeError("length of lists must be same")

    s = 0
    f = False

    for i in range(len(x)):
        n = x[i]
        n2 = y[i]
        if n == 0:
            if n2 == 0:
                continue
            else:
                return False
        else:
            if n2 == 0:
                return False

        cs = float(n2) / n
        if not f:
            s = cs
            f = True

        if cs != s:
            return False
    return True


def coprime(x, y):
    """
    Tests if x and y are coprime
    :param x:
    :param y:
    :return: boolean

    >>> coprime(10,2)
    False
    >>> coprime(16,15)
    True
    >>> coprime(-4, -2)
    False
    >>> coprime(-5, -2)
    True
    """
    from amath.Computation.relationship import gcd
    if gcd(x, y) == 1:
        return True
    else:
        return False


def perfect(x):
    """Checks if x is a perfect number"""
    from amath.Computation.num_properties import factors
    fac = factors(x)
    y = 0
    for i in fac:
        y += i
        y -= x
    if y == x:
        return True
    else:
        return False


def square(x):
    """checks if x is a square number"""
    sq = root(x, 2)
    if sq.is_integer():
        return True
    else:
        return False


def cube(x):
    """
    Checks if X is a cube number
    :param x:
    :return:

    >>> cube(2)
    False
    >>> cube(9)
    False
    >>> cube(8)
    True
    """
    c = root(x, 3)
    if float.is_integer(c):
        return True
    else:
        return False
