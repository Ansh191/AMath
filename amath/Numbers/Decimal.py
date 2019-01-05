from .backend import *
from ..Computation.num_properties import sign
from ..testing.types import isReal


class _ArbitraryPrecision:
    def __init__(self, man, exp, value=None):
        self.man = man
        self.exp = exp
        self.sign = sign(man)
        if value is None:
            self.value = man * 2 ** exp
        else:
            self.value = value
        if self.sign < 0:
            self.man = -self.man

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        if self.sign > 0:
            return "ArbitraryPrecision({0}, {1}) = {2}".format(self.man, self.exp, self.value)
        else:
            return "ArbitraryPrecision({0}, {1}) = {2}".format(-self.man, self.exp, self.value)

    def __add__(self, other):
        man, exp = dec_add(self, other)
        return _ArbitraryPrecision(man, exp)

    def __sub__(self, other):
        man, exp = dec_sub(self, other)
        return _ArbitraryPrecision(man, exp)

    def __mul__(self, other):
        man, exp = dec_mul(self, other)
        return _ArbitraryPrecision(man, exp)

    def __truediv__(self, other):
        man, exp = dec_truediv(self, other)
        return _ArbitraryPrecision(man, exp)

    def __floordiv__(self, other):
        return dec_floordiv(self, other)

    def __mod__(self, other):
        return dec_mod(self, other)

    def floor(self):
        man, exp = dec_floor(self)
        return _ArbitraryPrecision(man, exp)


class _MachinePrecision:
    pass


class _UnlimitedPrecision:
    pass


class Decimal:
    def __init__(self, value):
        if intQ(value):
            man, exp = from_int(value)
        elif isReal(value):
            man, exp = from_float(value)
        self.value = _ArbitraryPrecision(man, exp, value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)

    def __add__(self, other):
        if isinstance(self.value, _ArbitraryPrecision):
            if isinstance(other.value, _ArbitraryPrecision):
                return Decimal((self.value + other.value).value)

    def __sub__(self, other):
        if isinstance(self.value, _ArbitraryPrecision):
            if isinstance(other.value, _ArbitraryPrecision):
                return Decimal((self.value - other.value).value)

    def __mul__(self, other):
        if isinstance(self.value, _ArbitraryPrecision):
            if isinstance(other.value, _ArbitraryPrecision):
                return Decimal((self.value * other.value).value)

    def __truediv__(self, other):
        if isinstance(self.value, _ArbitraryPrecision):
            if isinstance(other.value, _ArbitraryPrecision):
                return Decimal((self.value / other.value).value)

    def __floordiv__(self, other):
        if isinstance(self.value, _ArbitraryPrecision):
            if isinstance(other.value, _ArbitraryPrecision):
                return Decimal((self.value // other.value).value)

    def __mod__(self, other):
        if isinstance(self.value, _ArbitraryPrecision):
            if isinstance(other.value, _ArbitraryPrecision):
                return Decimal((self.value % other.value).value)

    def floor(self):
        if isinstance(self.value, _ArbitraryPrecision):
            return Decimal(self.value.floor().value)