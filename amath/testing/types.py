from amath.DataTypes.Infinity import Infinity
from amath.Errors import InterpretationError


def isinf(x):
    """
    Checks if x is infinity
    :param x: suspected infinity
    :return: boolean

    >>> from amath.constants import inf, Ninf
    >>> isinf(inf)
    True
    >>> isinf(Ninf)
    True
    >>> isinf(float("inf"))
    True
    >>> isinf(float("-inf"))
    True
    >>> isinf(5)
    False
    """
    if isinstance(x, Infinity):
        return True
    elif x == float("inf"):
        return True
    elif x == float("-inf"):
        return True
    else:
        return False


def isnan(x):
    """
    Checks if X is NaN
    :param x: suspected NaN
    :return: boolean

    >>> isnan(float("NaN"))
    True
    >>> isnan(5)
    False
    """
    return x != x


def intQ(x):
    if type(x) == int:
        return True
    else:
        return False


def isReal(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


def interpreter(t, boolreturn=False):
    import inspect
    y = False
    if type(t) is not type:
        if not inspect.isclass(t):
            raise TypeError(str(t) + " is not a data type")
        elif inspect.isclass(t):
            y = True

    def inter(x):
        if y:
            if isinstance(x, t):
                if boolreturn:
                    return True
                return x
            else:
                if boolreturn:
                    return False
                raise InterpretationError(str(type(x)) + " " + str(x) + " is not a " + str(t))
        if type(x) is t:
            if boolreturn:
                return True
            return x
        else:
            if boolreturn:
                return False
            raise InterpretationError(str(type(x)) + " " + str(x) + " is not of " + str(t))

    return inter
