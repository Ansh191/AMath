# def ceil(x):
#     """
#     Returns the ceiling of a number
#     :param x: float
#     :return: integer
#
#     >>> ceil(5.3)
#     6
#     >>> ceil(6)
#     6
#     >>> ceil(-5.3)
#     -5
#     """
#     try:
#         if type(x) == str:
#             forstring = float(x)
#             y = int(forstring)
#         else:
#             y = int(x)
#     except:
#         try:
#             return (x // 1) + 1
#         except:
#             raise TypeError("A float is required")
#     if y == float(x):
#         return x
#     if float(x) > y:
#         return y + 1
#     else:
#         return y
#

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
    except:
        try:
            return x // 1
        except:
            raise TypeError("A float is required")
    if y < 0:
        return y - 1
    else:
        return y


#
#
# def trunc(x):
#     """
#     Return X truncated
#     :param x: any float or int
#     :return: X truncated
#     >>> trunc(5.2)
#     5
#     >>> trunc(-5.2)
#     -5
#     """
#     if x > 0:
#         y = floor(x)
#     else:
#         y = ceil(x)
#     return y


def round(x, m=0):
    """
    rounds X to nearest integer
    :param m: 
    :param x:
    :return:

    >>> round(5)
    5.0
    >>> round(2.5000000001)
    3.0
    >>> round(-2.56)
    -3.0

    If X is exactly mid way- round to even number

    >>> round(5.5)
    6.0
    >>> round(4.5)
    4.0
    """
    b = 10 ** (-m)

    def f(v):
        intx = int(floor(v))
        decx = v - intx
        if decx < 0.5:
            return intx
        elif decx > 0.5:
            return intx + 1
        elif decx == 0.5:
            if (intx + 1) % 2 == 0:
                return intx + 1
            else:
                return intx

    try:
        return f(float(x) / float(b)) * float(b)
    except ValueError:
        raise TypeError("A float, integer, or complex is required")
    except TypeError:
        return complex(f(float(x.real) / b) * b, f(float(x.imag) / b) * b)
