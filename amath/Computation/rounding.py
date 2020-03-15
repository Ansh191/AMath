import amath.ext._rounding as r

ROUND_TRUNC = 'ROUND_TRUNC'  # Round towards 0
ROUND_CEILING = 'ROUND_CEILING'  # Round towards Infinity
ROUND_FLOOR = 'ROUND_FLOOR'  # Round towards -Infinity
ROUND_UP = 'ROUND_UP'  # Round away from zero
ROUND_HALF_UP = 'ROUND_HALF_UP'  # Round to nearest with ties going towards Infinity
ROUND_HALF_AWAY = 'ROUND_HALF_AWAY'  # Round to nearest with ties going away from 0
ROUND_HALF_EVEN = 'ROUND_HALF_EVEN'  # Round to nearest with ties going to nearest even
ROUND_HALF_IN = 'ROUND_HALF_IN'  # Round to nearest with ties going towards 0
ROUND_HALF_DOWN = 'ROUND_HALF_DOWN'  # Round to nearest with ties going towards -Infinity


def round(n, d=0, *, tp=ROUND_HALF_AWAY):
    if tp == ROUND_TRUNC:
        return r.trunc(n, d)
    if tp == ROUND_CEILING:
        return r.ceil(n, d)
    if tp == ROUND_FLOOR:
        return r.floor(n, d)
    if tp == ROUND_UP:
        return r.away(n, d)
    if tp == ROUND_HALF_UP:
        return r.half_up(n, d)
    if tp == ROUND_HALF_AWAY:
        return r.half_away(n, d)
    if tp == ROUND_HALF_EVEN:
        return r.half_even(n, d)
    if tp == ROUND_HALF_IN:
        return r.half_in(n, d)
    if tp == ROUND_HALF_DOWN:
        return r.half_down(n, d)
    else:
        raise ValueError("Rounding Type not given")


def floor(n, d=0):
    return round(n, d, tp=ROUND_FLOOR)


def ceil(n, d=0):
    return round(n, d, tp=ROUND_CEILING)


def trunc(n, d=0):
    return round(n, d, tp=ROUND_TRUNC)


def chop(x, max=1e-10):
    if type(x) is complex:
        if abs(x.imag) <= max:
            x = x.real
        if abs(x.real) <= max:
            x = x.imag
        return x
    return x if abs(x) > max else 0
