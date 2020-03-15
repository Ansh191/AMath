import re
from random import uniform

import amath.Computation.relationship as _gcd
import amath.Computation.trig as _trig
import amath.constants as const
from amath.Computation.Basic import sqrt
from amath.Computation.num_properties import factors
from amath.Computation.rounding import round
from amath.algebra.Function import Function

_superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹"}

_trans = str.maketrans(
    ''.join(_superscript_map.keys()),
    ''.join(_superscript_map.values()))


def _format(coe):
    coe = coe[::-1]
    string = ""
    if coe == [0]:
        return "0"
    for i in range(len(coe)):
        exp = str(len(coe) - i - 1).translate(_trans)
        if exp == _superscript_map['1']:
            exp = ''
        if coe[i] == 0:
            # if i == len(coe) - 1:
            #     string += "  "
            continue
        string += f"{coe[i]}x{exp} + "

    return string[:-5]


def _duplicates(seq):
    dupes = [i for n, i in enumerate(seq) if i not in seq[:n]]
    return [(x, seq.count(x)) for x in dupes]


class Polynomial(Function):
    def __init__(self, coe):
        """Initializes Polynomial with list of coefficients

        List of coef goes from largest to smallest degree
        3x³ + 2x² - 5x - 3 -> [3, 2, -5, -3]

        :param coe: list of Coefficients of polynomial
        :type coe: list
        """
        self.coe = coe[::-1]  # Stored from smallest to largest degree
        self.normalize()
        if self.coe == [0]:
            self.degree = -1
        else:
            self.degree = len(self.coe) - 1

    def __repr__(self):
        return _format(self.coe)

    def __call__(self, x):
        return sum(self.coe[i] * pow(x, i) for i in range(self.degree + 1))

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            if self.coe == other.coe:
                return True
        return False

    def normalize(self):
        """Normalizes Polynomial to remove extra degrees with 0 as coefficient"""
        while self.coe and self.coe[-1] == 0:
            self.coe.pop()
        if not self.coe:
            self.coe.append(0)

    def find_roots(self):
        """Finds all roots of Polynomial

        Uses Aberth Method for polynomials of degree 4 or above. Otherwise uses formulas for polynomials of
        degree 1, 2, or 3.

        :return: list of all roots of polynomial
        :rtype: list

        Uses Formulas for low degrees

        >>> Polynomial([1, 3, -4]).find_roots()
        [-4.0, 1.0]
        >>> Polynomial([2, -9, 4, 15]).find_roots()
        [3.0, -1.0, 2.5]

        Uses Aberth's method for higher degrees

        >>> Polynomial([1, -8, 17, 14, -84, 72]).find_roots()
        [3.0, 2.0, 2.0, -2.0, 3.0]
        """
        if self.degree == 0:
            return []
        if self.degree == 1:
            return [-self.coe[0] / self.coe[1]]
        if self.degree == 2:
            a = self.coe[2]
            b = self.coe[1]
            c = self.coe[0]
            return [(0.5 * (-b - sqrt(b ** 2 - 4. * a * c))) / a, (0.5 * (-b + sqrt(b ** 2 - 4. * a * c))) / a]
        if self.degree == 3:
            a = self.coe[3]
            b = self.coe[2]
            c = self.coe[1]
            d = self.coe[0]
            r1 = -b / (3. * a) - (2 ** (1 / 3) * (-b ** 2 + 3 * a * c)) / (3. * a * (
                    -2 * b ** 3 + 9 * a * b * c - 27 * a ** 2 * d + sqrt(4 * (-b ** 2 + 3 * a * c) ** 3 + (
                    -2 * b ** 3 + 9 * a * b * c - 27 * a ** 2 * d) ** 2)) ** (1 / 3)) + (
                         -2 * b ** 3 + 9 * a * b * c - 27 * a ** 2 * d + sqrt(
                     4 * (-b ** 2 + 3 * a * c) ** 3 + (
                             -2 * b ** 3 + 9 * a * b * c - 27 * a ** 2 * d) ** 2)) ** (1 / 3) / (
                         3. * 2 ** (1 / 3) * a)
            r2 = -b / (3. * a) + ((1 + 1j * sqrt(3)) * (-b ** 2 + 3 * a * c)) / (
                    3. * 2 ** (2 / 3) * a * (-2 * b ** 3 + 9 * a * b * c - 27 * a ** 2 * d + sqrt(
                4 * (-b ** 2 + 3 * a * c) ** 3 + (
                        -2 * b ** 3 + 9 * a * b * c - 27 * a ** 2 * d) ** 2)) ** (1 / 3)) - (
                         (1 - 1j * sqrt(3)) * (-2 * b ** 3 + 9 * a * b * c - 27 * a ** 2 * d + sqrt(
                     4 * (-b ** 2 + 3 * a * c) ** 3 + (
                             -2 * b ** 3 + 9 * a * b * c - 27 * a ** 2 * d) ** 2)) ** (1 / 3)) / (
                         6. * 2 ** (1 / 3) * a)
            r3 = -b / (3. * a) + ((1 - 1j * sqrt(3)) * (-b ** 2 + 3 * a * c)) / (
                    3. * 2 ** (2 / 3) * a * (-2 * b ** 3 + 9 * a * b * c - 27 * a ** 2 * d + sqrt(
                4 * (-b ** 2 + 3 * a * c) ** 3 + (
                        -2 * b ** 3 + 9 * a * b * c - 27 * a ** 2 * d) ** 2)) ** (1 / 3)) - (
                         (1 + 1j * sqrt(3)) * (-2 * b ** 3 + 9 * a * b * c - 27 * a ** 2 * d + sqrt(
                     4 * (-b ** 2 + 3 * a * c) ** 3 + (
                             -2 * b ** 3 + 9 * a * b * c - 27 * a ** 2 * d) ** 2)) ** (1 / 3)) / (
                         6. * 2 ** (1 / 3) * a)

            r1, r2, r3 = complex(round(r1.real, 12), round(r1.imag, 12)), \
                         complex(round(r2.real, 12), round(r2.imag, 12)), \
                         complex(round(r3.real, 12), round(r3.imag, 12))

            return [r1 if abs(r1.imag) > 0 else r1.real, r2 if abs(r2.imag) > 0 else r2.real,
                    r3 if abs(r3.imag) > 0 else r3.real]

        roots = []
        lower, upper = self.get_root_bounds()
        for i in range(self.degree):
            radius = uniform(lower, upper)
            angle = uniform(0, const.pi * 2)
            roots.append(complex(radius * _trig.cos(angle), radius * _trig.sin(angle)))

        derivative = self.derivative()

        while True:
            valid = 0
            for k, r in enumerate(roots):
                ratio = self(r) / derivative(r)
                offset = ratio / (1 - (ratio * sum(1 / (r - x) for j, x in enumerate(roots) if j != k)))
                if offset.real == 0 and offset.imag == 0:
                    valid += 1
                roots[k] -= offset
            if valid == len(roots):
                break

        return [complex(round(r.real, 6), round(r.imag, 6)) if round(r.imag, 6) != 0 else round(r.real, 6) for r in
                roots]

    def find_root(self, *, guess=None):
        """Finds singular root of function

        If no initial guess given, uses Ratinal Roots Theorem to attempt to find a root, otherwise uses
        Newton's method initialized with random value within root range.
        If guess given, uses Netwon's method.

        :param guess: Initial guess for Netwon's method
        :type guess: float
        :return: A root of the polynomial
        :rtype: float
        """
        if self.num_roots() > 0:
            if guess is None:
                a0 = factors(abs(self.coe[0]))
                an = factors(abs(self.coe[-1]))
                for f in a0:
                    for f2 in an:
                        if self(f / f2) == 0:
                            return f / f2
                        if self(-f / f2) == 0:
                            return -f / f2

            return super(Polynomial, self).find_root(guess=guess)
        return None

    def get_root_bounds(self):
        """Finds the bounds at which the roots can be in

        :return: tuple of negative bound and positive bound
        :rtype: tuple
        """
        u = 1 + max(abs(self.coe[self.degree - i] / self.coe[-1]) for i in range(1, self.degree + 1))
        return -u, u

    def derivative(self, value=None):
        """Finds the derivative of the Polynomial

        Given value, it will return an exact value of the derivative at that point

        :param value: x-value
        :return: Polynomial or slope at x-value

        >>> Polynomial([1, 3, 3]).derivative()
        2x + 3
        >>> Polynomial([4, 3, 2, 1, 4, 3]).derivative()
        20x⁴ + 12x³ + 6x² + 2x + 4
        >>> Polynomial([1, 4, 5]).derivative(5)
        14
        """
        final = []
        for i in range(1, self.degree + 1):
            final.append(self.coe[i] * i)
        der = Polynomial(final[::-1])
        if value is not None:
            return der(value)
        return der

    def integrate(self, a=None, b=None):
        """Finds the integral of the Polynomial

        Given a AND b, it will return a definite integral from a to b

        :param a: lower bound
        :param b: upper bound
        :return: Integral or result of definite integral

        >>> Polynomial([2, 3]).integrate()
        1.0x² + 3.0x
        >>> Polynomial([6, 2, 1]).integrate()
        2.0x³ + 1.0x² + 1.0x
        >>> Polynomial([5, 6]).integrate(0, 10)
        310.0
        """
        final = []
        for i in range(self.degree + 1):
            final.append(self.coe[i] / (i + 1))
        final.insert(0, 0)
        integ = Polynomial(final[::-1])

        if a is not None:
            return integ(b) - integ(a)

        return integ

    def isNumber(self):
        """Checks is Polynomial is just a number

        :rtype: bool
        :return: true or false

        >>> Polynomial([2, 3]).isNumber()
        False
        >>> Polynomial([2]).isNumber()
        True
        """
        if len(self.coe) == 1:
            return True
        return False

    @staticmethod
    def _combine_list(l1: list, l2: list, f) -> list:
        final = l1.copy() if len(l1) >= len(l2) else l2.copy()
        other = l2.copy() if len(l1) >= len(l2) else l1.copy()
        for i in range(len(final)):
            try:
                final[i] = f(final[i], other[i])
            except IndexError:
                pass
        return final

    def __add__(self, other):
        """Adds Polynomials

        :param other: Polynomial or numeric value
        :return: Polynomial

        >>> Polynomial([2, 3]) + Polynomial([3, 4])
        5x + 7
        >>> Polynomial([2, 3, 5]) + Polynomial([2, 4])
        2x² + 5x + 9
        >>> Polynomial([4, 5]) + 7
        4x + 12
        """
        if isinstance(other, Polynomial):
            return Polynomial(self._combine_list(self.coe, other.coe, lambda x, y: x + y)[::-1])
        else:
            return Polynomial(self._combine_list(self.coe, [other], lambda x, y: x + y)[::-1])

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            return Polynomial(self._combine_list(self.coe, other.coe, lambda x, y: x - y)[::-1])
        else:
            return Polynomial(self._combine_list(self.coe, [other], lambda x, y: x - y)[::-1])

    def __rsub__(self, other):
        if isinstance(other, Polynomial):
            return Polynomial(self._combine_list(other.coe, self.coe, lambda x, y: x - y)[::-1])
        else:
            return Polynomial(self._combine_list([other], self.coe, lambda x, y: x - y)[::-1])

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            final = []
            for i in range(self.degree + 1):
                iteration = [0] * (i + other.degree + 1)
                for j in range(other.degree + 1):
                    iteration[i + j] = self.coe[i] * other.coe[j]
                final = self._combine_list(final, iteration, lambda x, y: x + y)
            return Polynomial(final[::-1])
        else:
            final = self.coe.copy()
            for i in range(self.degree + 1):
                final[i] *= other
            return Polynomial(final[::-1])

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, Polynomial):
            num = self.coe[:]
            den = other.coe[:]

            if len(num) >= len(den):
                shiftlen = len(num) - len(den)
                den = [0] * shiftlen + den
            else:
                return Polynomial([0])

            q = []
            divisor = float(den[-1])
            for i in range(shiftlen + 1):
                mult = num[-1] / divisor
                q = [mult] + q

                if mult != 0:
                    d = [mult * u for u in den]
                    num = [u - v for u, v in zip(num, d)]

                num.pop()
                den.pop(0)

            return Polynomial(q[::-1])
        else:
            return self * (1 / other)

    def __mod__(self, other):
        if isinstance(other, Polynomial):
            num = self.coe[:]
            den = other.coe[:]

            if len(num) >= len(den):
                shiftlen = len(num) - len(den)
                den = [0] * shiftlen + den
            else:
                return Polynomial(num[::-1])

            q = []
            divisor = float(den[-1])
            for i in range(shiftlen + 1):
                mult = num[-1] / divisor
                q = [mult] + q

                if mult != 0:
                    d = [mult * u for u in den]
                    num = [u - v for u, v in zip(num, d)]

                num.pop()
                den.pop(0)

            return Polynomial(num[::-1])
        else:
            return self * (1 / other)

    def __abs__(self):
        final = [-x if x < 0 else x for x in self.coe]
        return Polynomial(final[::-1])

    def __pow__(self, power, modulo=None):
        result = self
        for i in range(power - 1):
            result *= self

        return result

    def limit(self, direction=True):
        if self.degree % 2 == 0:
            if self.coe[-1] > 0:
                return float("inf")
            else:
                return float("-inf")
        else:
            if self.coe[-1] > 0:
                if direction:
                    return float("inf")
                else:
                    return float("-inf")
            else:
                if direction:
                    return float("-inf")
                else:
                    return float("inf")

    def num_roots(self):
        changes = 0
        current = True if self.coe[-1] > 0 else False
        for i in range(self.degree, -1, -1):
            if (self.coe[i] > 0) != current:
                current = True if self.coe[i] > 0 else False
                changes += 1

        coe = self.coe[:]
        for i in range(self.degree + 1):
            if i % 2 == 1:
                coe[i] = -coe[i]

        current = True if coe[-1] > 0 else False
        for i in range(self.degree, -1, -1):
            if (coe[i] > 0) != current:
                current = True if coe[i] > 0 else False
                changes += 1

        return changes

    def absmax(self):
        if self.limit(True) == float("inf") or self.limit(False) == float("inf"):
            return float("inf")
        fprime = self.derivative()
        critical_points = [x for x in fprime.find_roots() if not isinstance(x, complex)]
        curmax = [0, float("-inf")]
        for cp in critical_points:
            if self(cp) > curmax[1]:
                curmax = [cp, self(cp)]

        return curmax[0], curmax[1]

    def absmin(self):
        if self.limit(True) == float("-inf") or self.limit(False) == float("-inf"):
            return float("-inf")
        fprime = self.derivative()
        critical_points = [x for x in fprime.find_roots() if not isinstance(x, complex)]
        curmin = [0, float("inf")]
        for cp in critical_points:
            if self(cp) < curmin[1]:
                curmin = [cp, self(cp)]

        return curmin[0], curmin[1]

    def max(self, a, b):
        fprime = self.derivative()
        critical_points = [x for x in fprime.find_roots() if not isinstance(x, complex) and a < x < b]
        critical_points += [a, b]
        curmax = [0, float("-inf")]
        for cp in critical_points:
            if self(cp) > curmax[1]:
                curmax = [cp, self(cp)]

        return curmax[0], curmax[1]

    def min(self, a, b):
        fprime = self.derivative()
        critical_points = [x for x in fprime.find_roots() if not isinstance(x, complex) and a < x < b]
        critical_points += [a, b]
        curmin = [0, float("inf")]
        for cp in critical_points:
            if self(cp) < curmin[1]:
                curmin = [cp, self(cp)]

        return curmin[0], curmin[1]

    def factor(self):
        p = Polynomial(self.coe[::-1])

        poly = []
        while p.degree >= 1:
            root = p.find_root()
            poly.append(Polynomial([1, -root]))
            p = p / poly[-1]

        if p.coe != [1]:
            poly.append(p)

        return poly

    def factor_str(self):
        facs = self.factor()
        fac_set = _duplicates(facs)
        string = ""
        for i in range(len(fac_set)):
            exponent = str(fac_set[i][1]).translate(_trans) if fac_set[i][1] > 1 else ""
            string += f"({fac_set[i][0]}){exponent}"

        return string

    @staticmethod
    def from_string(string: str):
        sub = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
        string = string.translate(sub).split(' + ')
        try:
            length = string[0].split('x')[1]
        except IndexError:
            return Polynomial([float(string[0])])
        l = [0] * (2 if length == '' else int(length) + 1)
        for term in string:
            try:
                coe, exp = term.split('x')
            except ValueError:
                coe, exp = term, 0

            try:
                coe, exp = float(coe), int(exp)
            except ValueError:
                coe, exp = float(coe), 1

            l[exp] = coe

        return Polynomial(l[::-1])

    @staticmethod
    def from_factors(facs):
        p = Polynomial([1])
        for f in facs:
            p *= f

        return p

    @staticmethod
    def from_factor_str(facs):
        matches = re.findall(r"(\(.+?\))(\d+)?", facs.translate(str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")))
        p = Polynomial([1])
        for match in matches:
            if match[-1] != '':
                matches.extend([(match[0], '')] * int(match[1]))
                continue
            p *= Polynomial.from_string(match[0][1:-1])

        return p

    @staticmethod
    def gcd(a, b):
        while b.coe != [0]:
            a, b = b, a % b
        return a / Polynomial._gcd(a)

    @staticmethod
    def lcm(a, b):
        return abs(a * b) / Polynomial.gcd(a, b)

    @staticmethod
    def _gcd(a):
        if any([x >= 0 for x in a.coe]):
            return _gcd.gcd(*a.coe)
        else:
            return -_gcd.gcd(*a.coe)

    def __neg__(self):
        return Polynomial([-x for x in self.coe[::-1]])

    def monomial_list(self):
        poly = []
        for i in range(self.degree + 1):
            monomial = [0] * (self.degree + 1)
            monomial[i] = self.coe[i]
            poly.append(Polynomial(monomial[::-1]))
        return poly[::-1]

    def discriminant(self):
        if self.degree == 0:
            return None
        if self.degree == 1:
            return 1
        if self.degree == 2:
            a = self.coe[2]
            b = self.coe[1]
            c = self.coe[0]
            return b ** 2 - 4 * a * c
        if self.degree == 3:
            a = self.coe[3]
            b = self.coe[2]
            c = self.coe[1]
            d = self.coe[0]
            return b ** 2 * c ** 2 - 4 * a * c ** 3 - 4 * b ** 3 * d + 18 * a * b * c * d - 27 * a ** 2 * d ** 2
        if self.degree == 4:
            a = self.coe[4]
            b = self.coe[3]
            c = self.coe[2]
            d = self.coe[1]
            e = self.coe[0]
            return b ** 2 * c ** 2 * d ** 2 - 4 * a * c ** 3 * d ** 2 - 4 * b ** 3 * d ** 3 + 18 * a * b * c * d ** 3 - 27 * a ** 2 * d ** 4 - 4 * b ** 2 * c ** 3 * e + \
                   16 * a * c ** 4 * e + 18 * b ** 3 * c * d * e - 80 * a * b * c ** 2 * d * e - 6 * a * b ** 2 * d ** 2 * e + 144 * a ** 2 * c * d ** 2 * e - \
                   27 * b ** 4 * e ** 2 + 144 * a * b ** 2 * c * e ** 2 - 128 * a ** 2 * c ** 2 * e ** 2 - 192 * a ** 2 * b * d * e ** 2 + 256 * a ** 3 * e ** 3
        if self.degree == 5:
            a = self.coe[5]
            b = self.coe[4]
            c = self.coe[3]
            d = self.coe[2]
            e = self.coe[1]
            f = self.coe[0]
            return b ** 2 * c ** 2 * d ** 2 * e ** 2 - 4 * a * c ** 3 * d ** 2 * e ** 2 - 4 * b ** 3 * d ** 3 * e ** 2 + 18 * a * b * c * d ** 3 * e ** 2 - \
                   27 * a ** 2 * d ** 4 * e ** 2 - 4 * b ** 2 * c ** 3 * e ** 3 + 16 * a * c ** 4 * e ** 3 + 18 * b ** 3 * c * d * e ** 3 - 80 * a * b * c ** 2 * d * e ** 3 - \
                   6 * a * b ** 2 * d ** 2 * e ** 3 + 144 * a ** 2 * c * d ** 2 * e ** 3 - 27 * b ** 4 * e ** 4 + 144 * a * b ** 2 * c * e ** 4 - 128 * a ** 2 * c ** 2 * e ** 4 - \
                   192 * a ** 2 * b * d * e ** 4 + 256 * a ** 3 * e ** 5 - 4 * b ** 2 * c ** 2 * d ** 3 * f + 16 * a * c ** 3 * d ** 3 * f + 16 * b ** 3 * d ** 4 * f - \
                   72 * a * b * c * d ** 4 * f + 108 * a ** 2 * d ** 5 * f + 18 * b ** 2 * c ** 3 * d * e * f - 72 * a * c ** 4 * d * e * f - 80 * b ** 3 * c * d ** 2 * e * f + \
                   356 * a * b * c ** 2 * d ** 2 * e * f + 24 * a * b ** 2 * d ** 3 * e * f - 630 * a ** 2 * c * d ** 3 * e * f - 6 * b ** 3 * c ** 2 * e ** 2 * f + \
                   24 * a * b * c ** 3 * e ** 2 * f + 144 * b ** 4 * d * e ** 2 * f - 746 * a * b ** 2 * c * d * e ** 2 * f + 560 * a ** 2 * c ** 2 * d * e ** 2 * f + \
                   1020 * a ** 2 * b * d ** 2 * e ** 2 * f - 36 * a * b ** 3 * e ** 3 * f + 160 * a ** 2 * b * c * e ** 3 * f - 1600 * a ** 3 * d * e ** 3 * f - \
                   27 * b ** 2 * c ** 4 * f ** 2 + 108 * a * c ** 5 * f ** 2 + 144 * b ** 3 * c ** 2 * d * f ** 2 - 630 * a * b * c ** 3 * d * f ** 2 - \
                   128 * b ** 4 * d ** 2 * f ** 2 + 560 * a * b ** 2 * c * d ** 2 * f ** 2 + 825 * a ** 2 * c ** 2 * d ** 2 * f ** 2 - 900 * a ** 2 * b * d ** 3 * f ** 2 - \
                   192 * b ** 4 * c * e * f ** 2 + 1020 * a * b ** 2 * c ** 2 * e * f ** 2 - 900 * a ** 2 * c ** 3 * e * f ** 2 + 160 * a * b ** 3 * d * e * f ** 2 - \
                   2050 * a ** 2 * b * c * d * e * f ** 2 + 2250 * a ** 3 * d ** 2 * e * f ** 2 - 50 * a ** 2 * b ** 2 * e ** 2 * f ** 2 + 2000 * a ** 3 * c * e ** 2 * f ** 2 + \
                   256 * b ** 5 * f ** 3 - 1600 * a * b ** 3 * c * f ** 3 + 2250 * a ** 2 * b * c ** 2 * f ** 3 + 2000 * a ** 2 * b ** 2 * d * f ** 3 - \
                   3750 * a ** 3 * c * d * f ** 3 - 2500 * a ** 3 * b * e * f ** 3 + 3125 * a ** 4 * f ** 4
