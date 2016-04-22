from amath.testing import evenQ


def ceil(x):
    """
    Returns the ceiling of a number
    :param x: float
    :return: integer

    >>> ceil(5.3)
    6
    >>> ceil(6)
    6
    >>> ceil(-5.3)
    -5
    """
    try:
        if type(x) == str:
            forstring = float(x)
            y = int(forstring)
        else:
            y = int(x)
    except ValueError:
        raise TypeError("A float is required")
    if y == float(x):
        return x
    if float(x) > y:
        return y + 1
    else:
        return y


def floor(x):
    """
    floors float
    :param x: float
    :return: floor of x

    >>> floor(5.3)
    5
    >>> floor(-5.3)
    -6
    >>> floor(0)
    0
    """
    try:
        y = int(x)
    except ValueError:
        raise TypeError("A float is required")
    if y < 0:
        return y - 1
    else:
        return y


def trunc(x):
    """
    Return X truncated
    :param x: any float or int
    :return: X truncated
    >>> trunc(5.2)
    5
    >>> trunc(-5.2)
    -5
    """
    if x > 0:
        y = floor(x)
    else:
        y = ceil(x)
    return y


def fround(x):
    """
    rounds X to nearest integer
    :param x:
    :return:

    >>> fround(5)
    5
    >>> fround(2.5000000001)
    3
    >>> fround(-2.56)
    -3

    If X is exactly mid way- round to even number

    >>> fround(5.5)
    6
    >>> fround(4.5)
    4
    """
    try:
        intx = int(floor(x))
        decx = x - intx
        if decx < 0.5:
            return intx
        elif decx > 0.5:
            return intx + 1
        elif decx == 0.5:
            if evenQ(intx + 1):
                return intx + 1
            else:
                return intx
    except ValueError:
        raise TypeError("A float or integer is required")
