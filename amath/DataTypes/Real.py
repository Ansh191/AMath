from .Fraction import Fraction


class _Real:
    def __init__(self, value):
        if type(value) != int:
            if type(value) != float:
                if type(value) != Fraction:
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            raise ValueError("invalid literal for real: {0}".format(str(value)))
                else:
                    float(Fraction)

        self.value = value

    def __abs__(self):
        return abs(self.value)

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __div__(self, other):
        return self.value / other

    def __mod__(self, other):
        return self.value % other

    def __pow__(self, power, modulo=None):
        return pow(self.value, power, modulo)

    def __cmp__(self, other):
        if type(other) == Real:
            if self.value > other.value:
                return 1
            elif self.value == other.value:
                return 0
            else:
                return -1
        else:
            try:
                other = Real(other)
            except ValueError:
                raise ValueError(other + " is not of the correct type")
            if self.value > other.value:
                return 1
            elif self.value == other.value:
                return 0
            else:
                return -1


Real = type("Real", [_Real, object], {})
