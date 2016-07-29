from amath.constants import e, pi


def sin(a):
    return (e ** (1j * a)).imag


def cos(a):
    """
    Return the Cosine of x
    :param a:
    :return:
    """
    return (e ** (1j * a)).real


def tan(a):
    """Returns tan(a)"""
    answer = (sin(a)) / cos(a)
    return answer


def cot(a):
    """Returns cotangent(a)"""
    answer = (cos(a)) / (sin(a))
    return answer


def sec(a):
    """Returns secant(a)"""
    answer = 1.00 / cos(a)
    return answer


def csc(a):
    """Returns the cosecant of a"""
    return 1.00 / sin(a)


def arcsin(a, error=0.00000000000000000001):
    if a > 1 or a < -1:
        raise ValueError("math domain error")

    minimum = -(pi / 2.0)
    maximum = pi / 2.0
    x = (maximum + minimum) / 2.0
    while True:
        if sin(x) == a:
            return x
        if (a - error) < sin(x) < (a + error):
            return x

        if sin(x) < a:
            minimum = x
            x = (maximum + minimum) / 2.0
        else:
            maximum = x
            x = (maximum + minimum) / 2.0


def arccos(a, error=0.00000000000000000001):
    return (pi / 2.0) - arcsin(a, error)


