from amath.constants import e


def sin(a):
    return (e ** (1j * a)).imag


# TODO-everyone fix cos
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


def asin(a):
    """Returns the arcsine of a"""
    pass
    if a > 1.00 or a < -1.00:
        raise ValueError("math domain error")
    return rad(a)
