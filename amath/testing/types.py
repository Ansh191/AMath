from amath.DataTypes.types import FunctionType
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
    from amath.DataTypes.Infinity import Infinity
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
    try:
        x = float(x)
    except (ValueError, TypeError):
        return False
    try:
        if int(x) == x:
            return True
        else:
            return False
    except OverflowError:
        return False


def isReal(x):
    try:
        float(x)
    except ValueError:
        return False
    except TypeError:
        return False
    return True


def isWhole(x):
    t = intQ(x)
    if not t:
        return False
    if x < 0:
        return False
    return True


def isNatural(x):
    t = intQ(x)
    if not t:
        return False
    if x <= 0:
        return False
    return True


def isComplex(x):
    if isinstance(x, complex):
        return True
    return False


def isNumber(x):
    try:
        complex(x)
        return True
    except TypeError:
        return False
    except ValueError:
        return False


def isValue(x):
    try:
        x + 2
        x - 2
        x * 2
        x / 2
        x ** 2
        return True
    except AttributeError:
        return False


def interpreter(t, boolreturn=False):
    # type: (type, bool) -> FunctionType
    import inspect
    if not isinstance(boolreturn, bool):
        raise TypeError("boolreturn must be a bool value")
    y = False
    if type(t) is not type:
        if not inspect.isclass(t):
            raise TypeError(str(t) + " is not a data type")
        elif inspect.isclass(t):
            y = True

    def _interpreter(x):
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

    return _interpreter
