from amath.Computation.rounding import trunc, floor
from amath.Computation.relationship import gcd
from amath.Computation.num_properties import digits


class _Fraction:
    """
    Fraction Class. Used to create a data type
    """

    def __init__(self, n, d):
        """
        Fraction initilization
        :param n: numerator
        :param d: denomenator
        :return:
        :raises ZeroDivisionError:

        Create a Fraction

        >>> Fraction(5,2)
        5/2
        >>> Fraction(-5,2)
        -5/2
        >>> Fraction(5,-2)
        -5/2
        >>> Fraction(4,10)
        2/5
        """
        self.onum = n
        self.oden = d
        self.numerator = n / gcd(abs(n), abs(d))
        self.denominator = d / gcd(abs(n), abs(d))
        self.whole = 0
        if type(self.denominator) is not complex:
            self.denominator = int(self.denominator)
        if type(self.numerator) is not complex:
            self.numerator = int(self.numerator)
        if (type(self.numerator) is not complex) and (type(self.denominator) is not complex):
            if self.denominator < 0:
                self.denominator = abs(self.denominator)
                self.numerator *= -1
        if self.denominator == 0:
            raise ZeroDivisionError
        self.whole = trunc(frtodec(self))

    def __add__(self, other):
        """
        Adds to values
        :param other:
        :return:

        >>> Fraction(1,4) + Fraction(2,4)
        3/4
        >>> Fraction(1,2) + Fraction(3,4)
        5/4
        >>> Fraction(1,2) + 2
        5/2
        >>> Fraction(1,2) + 2.5
        3
        """
        ax = other
        if type(other) is float:
            ax = dectofr(other)
        return Fraction(self.numerator * ax.denominator + self.denominator * ax.numerator,
                        self.denominator * ax.denominator)

    def __sub__(self, other):
        dx = other
        if type(other) is float:
            dx = dectofr(other)
        return Fraction(self.numerator * dx.denominator - self.denominator * dx.numerator,
                        self.denominator * dx.denominator)

    def __mul__(self, other):
        """
        Multiplication
        :param other:
        :return:

        >>> Fraction(1,2) * Fraction(5,4)
        5/8
        >>> Fraction(1,2) * 4
        2
        >>> Fraction(1,3) * 2.5
        5/6
        """
        mx = other
        if type(other) is float:
            mx = dectofr(other)
        return Fraction(self.numerator * mx.numerator, self.denominator * mx.denominator)

    def __truediv__(self, other):
        dx = other
        if type(other) is float:
            dx = dectofr(other)
        return Fraction(self.numerator * dx.denominator, self.denominator * dx.numerator)

    def __div__(self, other):
        """
        Division
        :param other:
        :return:

        Uses truediv

        >>> Fraction(1,2) / Fraction(3,4)
        2/3
        >>> Fraction(1,2) / 2
        1/4
        >>> Fraction(1,4) / 0.5
        1/2
        """
        return self.__truediv__(other)

    def __pow__(self, power, modulo = None):
        y = pow(self.numerator, power)
        z = pow(self.denominator, power)
        if modulo is not None:
            return Fraction(y, z) % modulo
        return Fraction(y, z)

    def __str__(self):
        if type(self) is tuple:
            if self[1] < 0:
                return "%s/%s" % (self[0], -1 * self[1])
            else:
                return "%s/%s" % (self[0], self[1])
        elif self.denominator == 1:
            return str(self.numerator)
        else:
            return "%s/%s" % (self.numerator, self.denominator)

    def __cmp__(self, other):
        """
        compare two values
        :param other:
        :return:

        >>> Fraction(1,2) < Fraction(2,3)
        True
        >>> Fraction(2,3) == Fraction(4,6)
        True
        >>> Fraction(1,3) < 1
        True
        >>> Fraction(5,2) > 2.5
        False
        """
        if type(other) is float:
            other = dectofr(other)
        a = Fraction(self.numerator * other.denominator, self.denominator * other.denominator)
        b = Fraction(other.numerator * self.denominator, self.denominator * other.denominator)
        if a.onum > b.onum:
            return 1
        elif a.onum is b.onum:
            return 0
        else:
            return -1

    def __nonzero__(self):
        """
        Non Zero
        :return:

        """
        if self != 0:
            return True
        else:
            return False

    def __repr__(self):
        try:
            return self.__str__()
        except AttributeError:
            return str(None)

    def digits(self):
        x = frtodec(self)
        return digits(x)

    def is_int(self):
        if self.denominator == 1:
            return True
        else:
            return False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            del self.denominator
            del self.numerator
            del self.oden
            del self.onum
            del self.whole
            del self.__add__
            del self.__sub__
            del self.__cmp__
            del self.__div__
            del self.digits
            del self.is_int
        except:
            pass

    def __trunc__(self):
        return self.whole

    def __float__(self):
        """
        Convert to float
        :return:

        >>> float(Fraction(1,2))
        0.5
        >>> float(Fraction(1,25))
        0.04
        >>> float(Fraction(5,2))
        2.5
        """
        return frtodec(self)

    def __mod__(self, other):
        """
        Modulus
        :param other:
        :return:

        >>> Fraction(1,2) % 2
        1/2
        >>> Fraction(1,2) % Fraction(1,3)
        1/6
        """
        z = trunc(float(self) / float(other))
        a = self - (float(other) * float(z))
        return a

    def __abs__(self):
        if self.numerator < 0:
            return Fraction(-self.numerator, self.denominator)
        else:
            return self

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __pos__(self):
        return Fraction(self.numerator, self.denominator)


Fraction = type("Fraction", (_Fraction, object), {})


def dectofr(x, error = 0.00000001):
    """
    Converts decimals to fractions
    :param x: decimal to convert
    :param error: just error
    :return: Fraction

    >>> dectofr(2.5)
    5/2
    >>> dectofr(0.25)
    1/4

    Repeating decimals must have many digits

    >>> dectofr(0.333333333333333333333)
    1/3

    Does work for int

    >>> dectofr(5)
    5
    """
    n = int(floor(x))
    x -= n
    if x < error:
        # return (n, 1)
        return Fraction(n, 1)
    elif 1 - error < x:
        # return (n+1, 1)
        return Fraction(n + 1, 1)

    # The lower fraction is 0/1
    lower_n = 0
    lower_d = 1
    # The upper fraction is 1/1
    upper_n = 1
    upper_d = 1
    while True:
        # The middle fraction is (lower_n + upper_n) / (lower_d + upper_d)
        middle_n = lower_n + upper_n
        middle_d = lower_d + upper_d
        # If x + error < middle
        if middle_d * (x + error) < middle_n:
            # middle is our new upper
            upper_n = middle_n
            upper_d = middle_d
        # Else If middle < x - error
        elif middle_n < (x - error) * middle_d:
            # middle is our new lower
            lower_n = middle_n
            lower_d = middle_d
        # Else middle is our best fraction
        else:
            # return (n * middle_d + middle_n, middle_d)
            # return "{0}/{1}".format(n*middle_d+middle_n,middle_d)
            return Fraction(n * middle_d + middle_n, middle_d)


def frtodec(x):
    """
    Converts Fraction to decimal
    :param x: Fraction to be converted
    :return: Decimal

    >>> frtodec(Fraction(1,2))
    0.5
    >>> frtodec(Fraction(1,3))
    0.3333333333333333
    """
    if not isinstance(x, Fraction):
        raise TypeError("Argument must be a fraction")
    return float(x.numerator) / float(x.denominator)
