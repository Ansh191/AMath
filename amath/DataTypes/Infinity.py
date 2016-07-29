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



Infinity = type("Infinity", (_Infinity, object), {})
