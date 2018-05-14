from amath.Errors import Failure, Indeterminate


class _Infinity:
    def __init__(self, n):
        if type(n) is not bool:
            if n is not None:
                raise TypeError("n must be bool")
        self.n = n

    def __cmp__(self, other):
        """
        Compares with another value. Used by >, <, ==, and !=

        :param other:
        :return:

         >>> Infinity(True) > 5
         True
         >>> Infinity(True) < 5
         False
         >>> Infinity(False) > Infinity(True)
         False
         >>> Infinity(None) == 0
         Traceback (most recent call last):
            ...
         Failure: Cannot be compared
         >>> Infinity(True) == float("inf")
         True
         >>> float("inf") > Infinity(None)
         Traceback (most recent call last):
            ...
         Failure: Cannot be compared
         >>>
        """
        from amath.testing.types import isinf
        if isinf(other):
            if isinstance(other, Infinity):
                if other.n is None:
                    raise

                elif other.n < self.n:
                    return 1
                else:
                    return -1
            if other == float("inf"):
                if self.n:
                    return 0
                elif self.n is False:
                    return -1
            elif other == float("-inf"):
                if self.n:
                    return 1
                elif self.n is False:
                    return 0
        if self.n:
            return 1
        elif self.n is False:
            return -1
        else:
            raise Failure("Cannot be compared")

    def __add__(self, other):
        """
        Adds a value to Infinity. Used by +
        :param other:
        :return:

        >>> Infinity(True) + 5
        inf
        >>> Infinity(False) + 5
        -inf
        >>> Infinity(None) + 5
        Complex Infinity
        >>> Infinity(True) + Infinity(True)
        inf
        >>> Infinity(False) + Infinity(True)
        Traceback (most recent call last):
            ...
        Indeterminate
        """
        if isinstance(other, _Infinity):
            if other.n == self.n:
                if self.n is None:
                    raise Indeterminate
                return self
            else:
                raise Indeterminate
        return self

    __radd__ = __add__

    def __sub__(self, other):
        """
        Subtract a value from Infinity. Used by -
        :param other:
        :return:

        >>> Infinity(True) - Infinity(False)
        inf
        >>> Infinity(True) - Infinity(True)
        Traceback (most recent call last):
            ...
        Indeterminate
        >>> Infinity(True) - 5
        inf
        >>> Infinity(None) + Infinity(True)
        Traceback (most recent call last):
            ...
        Indeterminate
        """
        return self + (-other)

    def __truediv__(self, other):
        """
        Main Division function. Divides infinity by other.

        :param other:
        :return:
        """
        if isinstance(other, _Infinity):
            return Indeterminate
        else:
            if other == 0:
                raise Indeterminate
            if other > 0:
                return self
            else:
                return -self

    __div__ = __truediv__
    __floordiv__ = __truediv__

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
        if self.n is None:
            return Infinity(None)
        elif self.n:
            return Infinity(False)
        else:
            return Infinity(True)

    def __mul__(self, other):
        from amath.testing.types import isinf
        if isinstance(other, Infinity):
            if self.n is None:
                return Infinity(None)
            elif other.n is None:
                return Infinity(None)
            elif self.n:
                if other.n:
                    return Infinity(True)
                else:
                    return Infinity(False)
            elif not self.n:
                if other.n:
                    return Infinity(False)
                else:
                    return Infinity(True)
        elif isinf(other):
            if self.n is None:
                return Infinity(None)
            elif self.n:
                if other > 0:
                    return Infinity(True)
                else:
                    return Infinity(False)
            else:
                if other > 0:
                    return Infinity(False)
                else:
                    return Infinity(True)
        elif isinstance(other, complex):
            if other.imag < 0:
                return self.__neg__()
            elif other.imag > 0:
                return Infinity(self.n)
            else:
                return Infinity(self.n)
        else:
            if self.n is None:
                if other == 0:
                    raise Indeterminate("Indeterminate expression 0 * ComplexInfinity encountered")
                else:
                    return Infinity(None)
            elif self.n:
                if other == 0:
                    raise Indeterminate("Indeterminate expression 0 * inf encountered")
                elif other > 0:
                    return Infinity(True)
                else:
                    return Infinity(False)
            else:
                if other == 0:
                    raise Indeterminate("Indeterminate expression 0 * (-inf) encountered")
                elif other > 0:
                    return Infinity(False)
                else:
                    return Infinity(True)

    __rmul__ = __mul__

    def __pow__(self, power, modulo=None):
        from amath.testing.types import isinf
        if not isinf(power):
            if power == 0:
                if self.n is None:
                    raise Indeterminate("Indeterminate expression ComplexInfinity**0 encountered")
                elif self.n:
                    raise Indeterminate("Indeterminate expression inf**0 encountered")
                else:
                    raise Indeterminate("Indeterminate expression (-inf)**0 encountered")
            elif power < 0:
                return 0
            else:
                return Infinity(self.n)
        else:
            if power > 0:
                return Infinity(None)
            elif power < 0:
                return 0
            elif isinstance(power, Infinity):
                if self.n is None:
                    raise Indeterminate("Indeterminate expression ComplexInfinity**ComplexInfinity encountered")
                elif self.n:
                    raise Indeterminate("Indeterminate expression inf**ComplexInfinity encountered")
                else:
                    raise Indeterminate("Indeterminate expression (-inf)**ComplexInfinity encountered")

    def __rpow__(self, other):
        from amath.testing.types import isinf
        if not isinf(other):
            if other == 0:
                if self.n is None:
                    raise Indeterminate("Indeterminate expression 0**ComplexInfinity encountered")
                elif self.n:
                    return 0
                else:
                    return Infinity(None)
            elif (other == 1) or (other == -1):
                raise Indeterminate("Indeterminate expression ({0})**{1} encountered".format(str(other), repr(self)))
            elif other < 0:
                if self.n is None:
                    raise Indeterminate("Indeterminate expression "
                                        "({0})**ComplexInfinity encountered".format(str(other)))
                elif self.n:
                    return Infinity(None)
                else:
                    return 0
            else:
                if self.n is None:
                    raise Indeterminate("Indeterminate expression {0}**ComplexInfinity encountered".format(str(other)))
                elif self.n:
                    return Infinity(True)
                else:
                    return 0

    def __float__(self):
        if self.n is None:
            raise TypeError("Can not convert ComplexInfinity into a float")
        elif self.n:
            return float("inf")
        else:
            return float("-inf")

    def __int__(self):
        raise OverflowError("Infinity cannot be represented as a integer")


Infinity = type("Infinity", (_Infinity, object), {})
