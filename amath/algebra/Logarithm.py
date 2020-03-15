from amath.Computation.power import log
from amath.constants import e
from .Function import Function
from .Polynomial import Polynomial


class Logarithm(Function):
    def __init__(self, inside: Polynomial, base=e, c=0):
        self.inside = inside
        self.b = base
        self.c = c

    def __repr__(self):
        sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        base = "ₑ" if self.b == e else str(self.b)
        if self.c != 0:
            return f"log{base}(x)+c".translate(sub).replace("c", str(self.c)).replace("x", str(self.inside))
        return f"log{base}(x)".translate(sub).replace("x", str(self.inside))

    def __call__(self, x):
        return log(x, self.b) + self.c

    def derivative(self, value=None):
        pass

    def integrate(self, a=None, b=None):
        pass

    def num_roots(self):
        if self.inside.degree == 0:
            return 0
        return self.inside.degree

    def find_root(self, *, guess=None):
        return super(Logarithm, self).find_root(guess=guess)

    def find_roots(self):
        return (self.inside - pow(self.b, self.c)).find_roots()

    def get_root_bounds(self):
        return pow(self.b, -self.c / self.a), pow(self.b, -self.c / self.a)

    def __neg__(self):
        return Logarithm(self.b, -self.a, -self.c)

    def __add__(self, other):
        if isinstance(other, Logarithm):
            if other.b == self.b:
                return Logarithm(self.b, self.a + other.a, other.c + self.c)
            else:
                return Function([self, other])
        elif issubclass(type(other), Function):
            return Function([self, other])
        else:
            return Logarithm(self.b, self.a, self.c + other)

    def __sub__(self, other):
        if isinstance(other, Logarithm):
            if other.b == self.b:
                return Logarithm(self.b, self.a - other.a, self.c - other.c)
            else:
                return Function([self, -other])
        elif issubclass(type(other), Function):
            return Function([self, -other])
        else:
            return Logarithm(self.b, self.a, self.c - other)

    def __mul__(self, other):
        if isinstance(other, Logarithm):
            if other.b == self.b:
                return Function([
                    Logarithm(self.b, self.a * other.a), Logarithm(self.b, self.a * other.c),
                    Logarithm(self.b, self.c * other.a), Polynomial([self.c * other.c])
                ])
