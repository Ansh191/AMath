from __future__ import division


def factors(x):
    # type: (int) -> list
    """
    Returns the factors of x
    :rtype: list
    :param x:
    :return:

    >>> factors(16)
    [1, 2, 4, 8, 16]
    >>> factors(5)
    [1, 5]
    >>> factors(500)
    [1, 2, 4, 5, 10, 25, 50, 100, 125, 250, 500]
    """
    f = []
    from amath.lists.iter import range  # For larger numbers, efficiency, and compatibility
    for i in range(1, x):
        if x % i == 0:  # if x is divisible by i
            f.append(i)  # add i to the factors list
    f.append(x)  # x is also a factor of x
    return f


def NFactors(x):
    # type: (int) -> int
    """
    Returns the number of factors x has
    :param x: 
    :return:

    >>> NFactors(16)
    5
    >>> NFactors(5)
    2
    >>> NFactors(500)
    11
    """
    nl = factors(x)  # get the factors
    return len(nl)  # get the length and return it


def sign(x):
    """Returns sign of X. Returns either -1, 0, or 1"""
    if x < 0:
        return -1
    elif x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        raise TypeError("A float is required")


def digits(x):
    from amath.DataTypes.Fraction import Fraction

    if type(x) is not int:
        if type(x) is not long:
            if type(x) is not float:
                if type(x) is not Fraction:
                    del Fraction
                    raise TypeError(str(x) + " is not a number")  # x is not a number
    if isinstance(x, Fraction):  # if x is a Fraction
        del Fraction
        return x.digits()  # run the specified digits function
    del Fraction
    if int(x) == x:
        return len(str(abs(x)))  # for int
    else:
        return len(str(abs(x))) - 1  # for float


def frexp(x):
    """
    power of 2 times number to equal X
    :param x:
    :return:
    >>> frexp(0)
    (0.0, 0)
    >>> frexp(8)
    (0.5, 4)
    """
    i = 0  # reset
    m = None  # reset
    correct = False  # reset
    if x == 0:
        correct = True  # if x is 0, we're done
    while not correct:
        p = pow(2, i)  # 2**i for i=hopeful number
        m = x / p  # get m
        if 0.5 <= abs(m) < 1:  # m must be between 0.5 and 1
            correct = True
        else:
            i += 1
    return m, i


def ldexp(x, i):
    """
    opposite of frexp
    :param x:
    :param i:
    :return:

    >>> ldexp(0.5,4)
    8.0

    >>> a,b = frexp(234234)
    >>> ldexp(a, b)
    234234.0


    """
    return float(x * (2 ** i))


def modf(x):
    """
    Splits X into integer and decimal pieces
    :param x:
    :return:

    >>> modf(5.2)
    (0.2, 5)
    >>> modf(53.34)
    (0.34, 53)

    Works with integers

    >>> modf(5)
    (0.0, 5)

    even works with long floats

    >>> modf(5.349293430359)
    (0.349293430359, 5)
    """
    from amath.Computation.rounding import floor

    a1 = str(x).find(".")  # get the decimal point location
    a2 = len(str(x)[a1 + 1:])  # get everything after the decimal point
    intx = floor(x)  # get int part
    decx = round(x - int(intx), a2 + 1)  # get float part
    del floor
    return decx, intx
