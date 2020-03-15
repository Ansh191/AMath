import re

from amath.algebra.Function import Function
from amath.algebra.Logarithm import Logarithm
from amath.algebra.Polynomial import Polynomial


def _check_integral(rat):
    sub = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
    if rat.bot.degree == 1 and rat.top.degree == 0:
        a = rat.bot.coe[1]
        b = rat.bot.coe[0]
        c = rat.top
        return Logarithm(Polynomial([a, b]), a=c / a)
    if rat.bot.degree == 1 and rat.top.degree == 1 and rat.top.coe[0] == 0:
        a = rat.bot.coe[1]
        b = rat.bot.coe[0]
        c = rat.top.coe[1]
        return Function([Polynomial([c / a, 0]), Logarithm(Polynomial([a, b]), a=c * b / a ** 2)])

    match = re.search(r"\((-?\d+(\.\d+)?)x \+ (-?\d+(\.\d+)?)\)(\d+)", rat.bot.factor_str().translate(sub))
    if match and rat.top.degree == 1 and rat.top.coe[0] == 0:
        a = float(match.group(1))
        b = float(match.group(3))
        c = rat.top.coe[1]
        n = float(match.group(5))
        fac = Polynomial.from_factor_str(f"({a}x + {b}){n - 1}")
        return Rational(Polynomial([c * a * (1 - n), -b * c]), a ** 2 * (n - 1) * (n - 2) * fac)

    if rat.bot.degree == 2 and rat.top.degree == 1:
        m = rat.top.coe[1]
        n = rat.top.coe[0]
        a = rat.bot.coe[2]
        b = rat.bot.coe[1]
        c = rat.bot.coe[0]
        if 4 * a * c - b ** 2 == 0:
            return Logarithm(Polynomial([a, b, c]), a=m / (2 * a)) - Rational(Polynomial([2 * a * n - b * m]),
                                                                              Polynomial([2 * a ** 2, b * a]))


class Rational(Function):
    def __init__(self, num, den):
        """Initializes Rational Function with 2 Polynomials

        :type num: Polynomial
        :type den: Polynomial
        :param num: Numerator
        :param den: Denominator

        >>> Rational(Polynomial([1, 3]), Polynomial([1, 2, -3]))
        (1x + 3)/(1x² + 2x + -3)
        >>> Rational(Polynomial([1, 2, 5]), Polynomial([-2, 3]))
        (-1x² + -2x + -5)/(2x + -3)
        """
        if den.coe[-1] < 0:
            num, den = -num, -den  # to keep top as negative
        self.top, self.bot = num, den

    def __repr__(self):
        return f"({self.top})/({self.bot})"

    def __call__(self, x):
        return self.top(x) / self.bot(x)

    def derivative(self, value=None):
        """Finds the derivative of the Rational Function

        Given value, it will return an exact value of the derivative at that point

        :param value: x-value
        :return: Rational or slope at x-value
        """
        der = Rational(self.bot * self.top.derivative() - self.top * self.bot.derivative(), self.bot * self.bot)
        if value is not None:
            return der(value)
        return der

    def integrate(self, a=None, b=None):
        test = _check_integral(self)
        if test:
            return test

        top = self.top
        bot = self.bot
        fracs = []

        if self.top.degree > self.bot.degree:
            fracs.append(top / bot)
            top = top % bot

        factors = bot.factor()
        for i in range(len(factors)):
            root = factors[i].find_root()
            coe = 1
            for j in range(len(factors)):
                if i == j:
                    continue
                coe *= factors[j](root)
            fracs.append(Rational(Polynomial([top(root) / coe]), factors[i]))

        for i in range(len(fracs)):
            fracs[i] = fracs[i].integrate()

        return Function(fracs)

    def num_roots(self):
        return self.top.num_roots()

    def get_root_bounds(self):
        return self.top.get_root_bounds()

    def find_roots(self):
        return self.top.find_roots()

    def find_root(self, *, guess=None):
        return self.top.find_root(guess=guess)

    def vertical_asymptotes(self):
        return self.bot.find_roots()

    def horizontal_asymptote(self):
        if self.top.degree > self.bot.degree:
            return None
        if self.top.degree < self.bot.degree:
            return 0
        return self.top.coe[-1] / self.bot.coe[-1]

    def oblique_asymptote(self):
        if self.top.degree - 1 == self.bot.degree:
            return self.top / self.bot
        return None

    def simplify(self):
        gcd = Polynomial.gcd(self.bot, self.top)
        print(gcd)
        return Rational(self.top / gcd, self.bot / gcd)

    def __neg__(self):
        return Rational(-self.top, self.bot)

    def __add__(self, other):
        if isinstance(other, Rational):
            lcm = Polynomial.lcm(self.bot, other.bot)
            return Rational(self.top * lcm / self.bot + other.top * lcm / other.bot, lcm)  # Not working as intended

        return Rational(self.top + self.bot * other, self.bot)

    def __sub__(self, other):
        if isinstance(other, Rational):
            lcm = Polynomial.lcm(self.bot, other.bot)
            return Rational(self.top * lcm / self.bot - other.top * lcm / other.bot, lcm)  # Not working as intended

        return Rational(self.top - self.bot * other, self.bot)

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.top * other.top, self.bot * other.bot)

        return Rational(self.top * other, self.bot)
