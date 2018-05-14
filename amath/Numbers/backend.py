from ..Computation.num_properties import frexp
from ..testing.types import intQ


def from_exp(man, exp):
    if intQ(man):
        while intQ(man):
            man /= 2
            exp += 1
        man *= 2
        exp -= 1
    else:
        while not intQ(man):
            man *= 2
            exp -= 1
    return int(man), int(exp)


def from_int(x):
    man, exp = frexp(x)
    while not intQ(man):
        man *= 2
        exp -= 1
    return int(man), int(exp)


def from_float(x):
    man, exp = frexp(x)
    while not intQ(man):
        man *= 2
        exp -= 1
    return int(man), int(exp)


# ---------------------------------------------------------------- #
#                            OPERATIONS                            #
# ---------------------------------------------------------------- #

def dec_add(x, y, sub=False):
    """

    :rtype: Tuple[int, int]
    """
    xman, xexp, xsign = x.man, x.exp, x.sign
    yman, yexp, ysign = y.man, y.exp, y.sign
    if sub:
        ysign = -ysign

    offset = xexp - yexp
    if offset:
        if offset > 0:
            if xsign == ysign:
                man = yman + (xman << offset)
                exp = yexp
            else:
                if xsign < 0:
                    man = yman - (xman << offset)
                else:
                    man = (xman << offset) - yman
                exp = yexp
        else:
            if xsign == ysign:
                man = xman + (yman << -offset)
                exp = xexp
            else:
                if ysign < 0:
                    man = xman - (yman << -offset)
                else:
                    man = (yman << -offset) - xman
                exp = xexp
    else:
        if xsign == ysign:
            man = xman + yman
            exp = xexp
        else:
            if ysign < 0:
                man = xman - yman
            else:
                man = yman - xman
            exp = xexp

    return from_exp(man, exp)


def dec_sub(x, y):
    return dec_add(x, y, True)


def dec_mul(x, y):
    xman, xexp, xsign = x.man, x.exp, x.sign
    yman, yexp, ysign = y.man, y.exp, y.sign

    if xsign < 0:
        xman = -xman
    if ysign < 0:
        yman = -yman

    return from_exp(xman * yman, xexp + yexp)


def dec_truediv(x, y):
    xman, xexp, xsign = x.man, x.exp, x.sign
    yman, yexp, ysign = y.man, y.exp, y.sign

    if xsign < 0:
        xman = -xman
    if ysign < 0:
        yman = -yman

    return from_exp(xman / yman, xexp - yexp)


def dec_floordiv(x, y):
    return (x / y).floor()


def dec_mod(x, y):
    z = x // y
    print(type(z))
    z *= y
    print(z)
    z = x - z
    print(z)
    return z


# ---------------------------------------------------------------- #
#                            ROUNDING                              #
# ---------------------------------------------------------------- #

def dec_floor(x):
    xman, xexp, xsign = x.man, x.exp, x.sign

    if xsign < 0:
        xman = -xman

    if xexp < 0:
        exp = -xexp
        man = xman >> exp
        return from_exp(man, 0)
    else:
        return from_exp(xman, xexp)
