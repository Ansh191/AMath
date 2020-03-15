from .Fraction import Fraction
from .Infinity import Infinity
from ..Errors import Indeterminate


class _Integer:

    def __new__(cls, n: int):
        self = object.__new__(cls)
        self.n = int(n)
        self.numerator = +self.n
        self.denominator = 1
        return self

    def __repr__(self):
        return f"Integer({self.n})"

    def __add__(self, other):
        return Integer(self.n + other)

    __radd__ = __add__

    def __sub__(self, other):
        return Integer(self.n - other)

    def __rsub__(self, other):
        return Integer(other - self.n)

    def __mul__(self, other):
        return Integer(self.n * other)

    __rmul__ = __mul__

    def __truediv__(self, other):
        try:
            return Fraction(self.n, other)
        except ZeroDivisionError:
            if self.n == 0:
                return Indeterminate("Indeterminate expression 0/0 encountered")
            else:
                return Infinity(None)

    def __rtruediv__(self, other):
        try:
            return Fraction(other, self.n)
        except ZeroDivisionError:
            if other == 0:
                return Indeterminate("Indeterminate expression 0/0 encountered")
            else:
                return Infinity(None)

    def __floordiv__(self, other):
        from ..Computation.rounding import floor
        return Integer(floor(self / other))

    def __rfloordiv__(self, other):
        from ..Computation.rounding import floor
        return Integer(floor(other / self))

    def __abs__(self):
        if self.n < 0:
            return -self
        else:
            return self

    def __neg__(self):
        return Integer(-self.n)

    def __eq__(self, other):
        if isinstance(other, Integer):
            if self.n == other.n:
                return True
        elif self.n == other:
            return True

        return False

    def __gt__(self, other):
        if isinstance(other, Integer):
            if self.n > other.n:
                return True
        elif self.n > other:
            return True

        return False

    def __lt__(self, other):
        if isinstance(other, Integer):
            if self.n < other.n:
                return True
        elif self.n < other:
            return True

        return False

    def __float__(self):
        return float(self.n)

    def __int__(self):
        return self.n

    def __complex__(self):
        return complex(self.n)


Integer = type("Integer", (_Integer, object), {})
