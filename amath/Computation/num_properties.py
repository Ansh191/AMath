try:
    import amath.ext._numprop as _np
except ModuleNotFoundError:
    print("_numprop failed to import")


def factors(x: int) -> list:
    """
    Returns the factors of x

    :param x: Integer to factor
    :return: List of factors of x

    >>> factors(16)
    [1, 2, 4, 8, 16]
    >>> factors(5)
    [1, 5]
    >>> factors(500)
    [1, 2, 4, 5, 10, 20, 25, 50, 100, 125, 250, 500]
    """
    try:
        return _np.factors(x)
    except (NameError, TypeError, OverflowError):
        pass

    f = []
    x = int(x)
    if x == 0:
        return [0]
    sqrt = x ** .5
    for i in range(1, int(sqrt) + 1):  # Go through half of the factors
        if x % i == 0:  # if x is divisible by i
            f.append(i)  # add i to the factors list

    f2 = f.copy()  # Final factor list
    for i in reversed(f):
        f2.append(x // i)  # Add the other half of factors

    if sqrt == int(sqrt):
        f2.remove(int(sqrt))  # Remove the duplicated sqrt

    return f2


def NFactors(x: int) -> int:
    """
    Returns the number of factors x has

    :param x: Integer to get the number of factors of
    :return: Number of factors of x

    >>> NFactors(16)
    5
    >>> NFactors(5)
    2
    >>> NFactors(500)
    12
    """
    return len(factors(x))


def sign(x) -> int:
    """
    Returns sign of x. Returns either -1, 0, or 1

    :param x: Number to get the sign of
    :return: Returns -1, 0, or 1 based on sign of x

    >>> sign(5)
    1
    >>> sign(0)
    0
    >>> sign(-1.2)
    -1
    """
    if x < 0:
        return -1
    elif x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        raise TypeError("A float is required")


def digits(x):
    """
    Find the number of digits in x

    :param x: Number
    :return: Number of digits in x

    >>> digits(5)
    1
    >>> digits(234)
    3
    >>> digits(3.0)
    1
    >>> digits(3.4)
    2
    """
    from amath.testing.types import intQ, isFraction

    if isFraction(x):  # if x is a Fraction
        return x.digits()  # run the specified digits function
    if intQ(x):
        x = int(x)
    if int(x) == x:
        return len(str(abs(x)))  # for int
    else:
        return len(str(abs(x))) - 1  # for float


def digitsafterdecimal(x):
    """
    Get number of digits after decimal point

    :param x: A float
    :return: number of digits after decimal

    >>> digitsafterdecimal(5.5)
    1
    >>> digitsafterdecimal(0.26)
    2
    >>> digitsafterdecimal(1/3)
    16
    """
    from decimal import Decimal
    return -Decimal(str(x)).as_tuple().exponent


def frexp(x):
    """
    Convert x into the form a * 2^b

    :param x: Number to convert into the form a * 2^b
    :return: tuple containing (a, b) from the form a * 2^b

    >>> frexp(0)
    (0.0, 0)
    >>> frexp(8)
    (0.5, 4)
    """
    try:
        return _np.frexp(x)
    except (TypeError, NameError):
        pass
    b = 0
    a = 0.0
    correct = False
    if x == 0:
        correct = True  # if x is 0, we're done
    while not correct:
        p = pow(2, b)  # 2**b for b=hopeful number
        a = x / p  # get a
        if 0.5 <= abs(a) < 1:  # a must be between 0.5 and 1
            correct = True
        else:
            b += 1
    return a, b


def ldexp(a, b):
    """
    Opposite of frexp
    a * 2^b

    :param a: Multiplied number
    :param b: Exponent Number
    :return: Value of a * 2^b

    >>> ldexp(0.5,4)
    8.0

    >>> a,b = frexp(2342345)
    >>> ldexp(a, b)
    2342345.0


    """
    try:
        return _np.ldexp(a, b)
    except (TypeError, NameError):
        return a * (2 ** b)


def modf(x):
    """
    Splits X into integer and decimal pieces
    :param x:
    :return:

    >>> modf(-5.2)
    (-0.2, -5)
    >>> modf(53.34)
    (0.34, 53)

    Works with integers

    >>> modf(5)
    (0.0, 5)

    even works with long floats

    >>> modf(5.349293430359)
    (0.349293430359, 5)
    """
    # try:
    #     return _np.modf(x)
    # except (TypeError, NameError):
    #     pass

    a1 = str(x).find(".")  # get the decimal point location
    a2 = len(str(x)[a1 + 1:])  # get everything after the decimal point
    intx = int(x)  # get int part
    decx = round(float(x) - int(intx), a2 + 1)  # get float part
    return decx, intx


def continued_fraction(x, n=10):
    result = []
    for i in range(n):
        frac_part, int_part = modf(x)
        result.append(int_part)
        if frac_part == 0:
            break
        x = 1 / frac_part

    return result
