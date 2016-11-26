from amath.Errors import Failure, Indeterminate


class _Infinity:
    def __init__(self, n):
        if type(n) is not bool:
            if n is not None:
                raise TypeError("n must be bool")
        self.n = n

    def __cmp__(self, other):
        if isinstance(other, _Infinity):
            if other.n == self.n:
                return 0
        if self.n:
            return 1
        elif self.n is False:
            return -1
        else:
            raise Failure("Cannot be compared")

    def __add__(self, other):
        if isinstance(other, _Infinity):
            if other.n == self.n:
                return self
        if isinstance(other, _Infinity):
            return float("NaN")
        return self

    def __sub__(self, other):
        if isinstance(other, _Infinity):
            if other.n == self.n:
                return self
        if isinstance(other, _Infinity):
            return float("NaN")
        return self

    def __truediv__(self, other):
        if isinstance(other, _Infinity):
            return float("NaN")
        else:
            return self

    def __div__(self, other):
        return self.__truediv__(other)

    def __repr__(self):
        try:
            if self.n:
                return "inf"
            elif self.n is False:
                return "-inf"
            else:
                return "Complex Infinity"
        except AttributeError:
            return None

    def __neg__(self):
        if self.n:
            return Infinity(False)
        elif self.n == False:
            return Infinity(True)
        else:
            return Infinity(None)

    def __mul__(self, other):
        if isinstance(other, Infinity):
            if self.n is None:
                return Infinity(None)
            elif other.n is None:
                return Infinity(None)
            elif self.n == True:
                if other.n == True:
                    return Infinity(True)
                else:
                    return Infinity(False)
            elif self.n == False:
                if other.n == True:
                    return Infinity(False)
                else:
                    return Infinity(True)
        else:
            if isinstance(other, complex):
                if other.imag < 0:
                    return self.__neg__()
                elif other.imag > 0:
                    return Infinity(self.n)
                else:
                    return Infinity(self.n)


Infinity = type("Infinity", (_Infinity, object), {})
