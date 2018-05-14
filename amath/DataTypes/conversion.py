def tocomplex(x):
    return complex(x)


def tofloat(x):
    return float(x)


def toint(x):
    return int(x)


def tolong(x):
    try:
        return long(x)
    except NameError:
        from amath.Errors.Errors import Failure
        raise Failure("Long is not supported")


def tostr(x):
    return str(x)


def tolist(x):
    return list(x)


def toset(x):
    return set(x)


def tofrozenset(x):
    return frozenset(x)


def todict(x):
    return dict(x)


def totuple(x):
    return tuple(x)


def toFraction(x):
    from .Fraction import dectofr
    return dectofr(tofloat(x))
