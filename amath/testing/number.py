from amath.Computation.power import root


def evenQ(x):
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
    fac = factors(x)[0:-1]
    y = 0
    for i in fac:
        y += i
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
