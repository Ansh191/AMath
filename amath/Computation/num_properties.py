def factors(x):
    """Returns factors of x"""
    f = []
    for i in range(1, x):
        if x % i == 0:
            f.append(i)
    f.append(x)
    return f


def NFactors(x):
    nl = factors(x)
    return len(nl)


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
        if type(x) is not float:
            if type(x) is not Fraction:
                del Fraction
                raise TypeError(x + " is not a number")
    if isinstance(x, Fraction):
        del Fraction
        return x.digits()
    del Fraction
    if int(x) == x:
        return len(str(x))
    else:
        return len(str(x)) - 1


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
    i = 0
    m = 0.0
    correct = False
    if x == 0:
        correct = True
    while not correct:
        p = pow(2, i)
        m = x / float(p)
        if 0.5 <= abs(m) < 1:
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

    """
    return float(x * (2 ** i))


def modf(x):
    """
    Splits X into integer and decimal peices
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

    a1 = str(x).find(".")
    a2 = len(str(x)[a1 + 1:])
    intx = floor(x)
    decx = round(x - int(intx), a2 + 1)
    del floor
    return decx, intx
