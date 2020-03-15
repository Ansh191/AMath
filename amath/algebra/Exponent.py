from amath.Computation.power import pow, ln
from amath.algebra.Function import Function
from amath.constants import e
from .Polynomial import Polynomial


class Exponent(Function):
    def __init__(self, a, b, c=0):
        self.a, self.b, self.c = a, b, c

    def __repr__(self):
        base = "e" if self.b == e else self.b
        return f"{self.a}×{base}ˣ" if self.c == 0 else f"{self.a}×{base}ˣ+{self.c}"

    def __call__(self, x):
        return self.a * pow(self.b, x) + self.c

    def __eq__(self, other):
        if isinstance(other, Exponent):
            if self.a == other.a and self.b == other.b and self.c == other.c:
                return True

        return False

    def derivative(self, value=None):
        der = Exponent(self.a * ln(self.b), self.b)
        if value is not None:
            return der(value)
        return der

    def integrate(self, a=None, b=None):
        integ = Exponent(self.a / ln(self.b), self.b) + Polynomial([self.c, 0])
        if a is not None:
            return integ(b) - integ(a)
        return integ

    def num_roots(self):
        if self.a > 0:
            if self.c < 0:
                return 1
        else:
            if self.c > 0:
                return 1
        return 0

    def find_root(self, *, guess=None):
        if self.num_roots():
            if guess is None:
                return ln(-self.c / self.a) / ln(self.b)
            return super(Exponent, self).find_root(guess=guess)
        else:
            return None

    def find_roots(self):
        x = self.find_root()
        if x is None:
            return []
        return [x]

    def get_root_bounds(self):
        return ln(-self.c / self.a) / ln(self.b), ln(-self.c / self.a) / ln(self.b)

    def __neg__(self):
        return Exponent(-self.a, self.b, -self.c)

    def __add__(self, other):
        if isinstance(other, Exponent):
            if other.b == self.b:
                return Exponent(self.a + other.a, self.b, self.c + other.c)
            else:
                return Function([self, other])
        elif issubclass(type(other), Function):
            return Function([self, other])
        else:
            return Exponent(self.a, self.b, self.c + other)

    def __sub__(self, other):
        if isinstance(other, Exponent):
            if other.b == self.b:
                return Exponent(self.a - other.a, self.b, self.c - other.c)
            else:
                return Function([self, -other])
        elif issubclass(type(other), Function):
            return Function([self, -other])
        else:
            return Exponent(self.a, self.b, self.c - other)

    def __mul__(self, other):
        if isinstance(other, Exponent):
            if other.b == self.b:
                return Function([Exponent(self.a * other.a, self.b ** 2),
                                 Exponent(self.a * other.c, self.b) + Exponent(self.c * other.a, self.b),
                                 Polynomial([self.c * other.c])])
            else:
                return Function([self, -other])
        elif issubclass(type(other), Function):
            return Function([self, -other])
        else:
            return Exponent(self.a, self.b, self.c - other)
