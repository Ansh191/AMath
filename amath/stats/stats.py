from amath.constants import inf
from .mean import mean


def slope(x1, y1, x2, y2):
    from amath.DataTypes.Fraction import Fraction
    dx = x1 - x2
    dy = y1 - y2
    if dx == 0:
        return inf
    return Fraction(dy, dx)


def sum(f, i=None, maximum=None, step=1, l=None):
    try:
        if type(f(2)) != float:
            if type(f(2)) != int:
                raise ValueError("Function must return float or integer value")
    except TypeError:
        raise TypeError("f must be a function with only one argument")

    if i is not None:
        if maximum is not None:
            if l is not None:
                raise TypeError("Invalid Argument")
    if i is None:
        if maximum is None:
            if l is None:
                raise TypeError("Invalid Argument")

    if l is None:
        x = 0
        previous_value = 0
        while i <= maximum:
            value = f(i)
            if value == previous_value:
                break
            x += value
            i += step
        return x
    else:
        x = 0
        for y in l:
            x += f(y)
        return x


def product(f, i=None, maximum=None, step=1, l=None):
    try:
        if type(f(2)) != float:
            if type(f(2)) != int:
                raise ValueError("Function must return float or integer value")
    except TypeError:
        raise TypeError("f must be a function")

    if i is not None:
        if maximum is not None:
            if l is not None:
                raise TypeError("Invalid Argument")
    if i is None:
        if maximum is None:
            if l is None:
                raise TypeError("Invalid Argument")

    if l is None:
        x = 1
        previous_value = 1
        while i <= maximum:
            value = f(i)
            # if value == previous_value:
            #     break
            x *= value
            i += step
        return x
    elif i is not None:
        x = 1
        for y in l:
            x *= f(y)
        return x


def linregress(inp, output):
    # type: (list, list) -> Function
    from amath.DataTypes.Function import Function
    if not isinstance(inp, list):
        raise TypeError("Input must be a list")
    if not isinstance(output, list):
        raise TypeError("Input must be a list")

    if len(inp) != len(output):
        raise TypeError("Lists must be of the same size")

    if inp == output:
        return Function("x", "1.0x + 0.0")  # if list is same
    # set Defaults
    z = 0
    a = 0
    i = 0
    xm = mean(inp)  # mean of input
    ym = mean(output)  # mean of output
    for item in inp:
        z += (item - xm) * (output[i] - ym)
        i += 1

    for item in inp:
        a += (item - xm) ** 2

    m = z / a

    b = ym - (m * xm)

    return Function("x", "{0}x + {1}".format(m, b))


def expregress(inp, output):
    from amath.lists.lists import applylist, anytrue
    from amath.Computation.power import ln
    from amath.testing.types import isnan, isinf
    from amath.DataTypes.Function import Function
    logoutput = applylist(output, ln)
    if anytrue(logoutput, isnan) or anytrue(logoutput, isinf):
        raise ValueError("output cannot be negative")
    lin = linregress(inp, logoutput)
    l = lin.function.split("x + ")
    l = applylist(l, float)
    l = applylist(l, Function("a", "e**a"))
    return Function("x", "{0}*({1}**x)".format(l[1], l[0]))


def isPro(x, y):
    if type(x) != list:
        raise TypeError("x must be a list")
    if type(y) != list:
        raise TypeError("y must be a list")
    if len(x) != len(y):
        raise TypeError("length of lists must be same")
    if len(x) <= 1:
        raise ValueError("length of lists must be greater than 1")

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
