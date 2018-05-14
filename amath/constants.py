from functools import total_ordering

from .Computation.Basic import sqrt
from .DataTypes.Infinity import Infinity


@total_ordering
class _Constant:
    def __init__(self, name, value=None, description=None):
        self.name = name
        self.value = value
        self.description = description

    def __str__(self):
        if self.value is None:
            return self.name
        else:
            return self.value

    def __lt__(self, other):
        return self.value < other

    def __eq__(self, other):
        return self.value == other

    def __add__(self, other):
        if isinstance(other, Constant):
            return self.value + other.value
        else:
            temp = Constant("Temp", other)
            return self.value + temp.value

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, Constant):
            return self.value - other.value
        else:
            temp = Constant("Temp", other)
            return self.value - temp.value

    __rsub__ = __sub__

    def __mul__(self, other):
        if isinstance(other, Constant):
            return self.value * other.value
        else:
            temp = Constant("Temp", other)
            return self.value * temp.value

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, Constant):
            return self.value / other.value
        else:
            temp = Constant("Temp", other)
            return self.value / temp.value

    __rtruediv__ = __truediv__

    def __floordiv__(self, other):
        if isinstance(other, Constant):
            return self.value // other.value
        else:
            temp = Constant("Temp", other)
            return self.value // temp.value

    __rfloordiv__ = __floordiv__

    def __mod__(self, other):
        if isinstance(other, Constant):
            return self.value % other.value
        else:
            temp = Constant("Temp", other)
            return self.value % temp.value

    __rmod__ = __mod__

    def __divmod__(self, other):
        if isinstance(other, Constant):
            return self.value // other.value, self.value % other.value
        else:
            temp = Constant("Temp", other)
            return self.value // temp.value, self.value % other.value

    __rdivmod__ = __divmod__

    def __pow__(self, power, modulo=None):
        if modulo is None:
            if isinstance(power, Constant):
                return self.value ** power.value
            else:
                temp = Constant("Temp", power)
                return self.value ** temp.value
        else:
            if isinstance(power, Constant):
                if isinstance(modulo, Constant):
                    return (self.value ** power.value) % modulo.value
                else:
                    modulo_temp = Constant("Modulo Temp", modulo)
                    return (self.value ** power.value) % modulo_temp.value
            else:
                power_temp = Constant("Power Temp", power)
                if isinstance(modulo, Constant):
                    return (self.value ** power_temp.value) % modulo.value
                else:
                    modulo_temp = Constant("Modulo Temp", modulo)
                    return (self.value ** power_temp.value) % modulo_temp.value

    def __neg__(self):
        if self.value is None:
            return Constant(self.description, None)
        else:
            return


Constant = type("Constant", (_Constant, object), {})

e = 2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466  # e
pi = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214  # pi
gr = goldenRatio = (1 + sqrt(5)) / 2.0  # Golden Ratio
ec = EulerMascheroni = 0.5772156649015328606065120900824024310421  # Euler-Mascheroni constant
O = Omega = 0.5671432904097838729999686622103555497538157871865125081351310792230457930866  # Omega
rf = reciprocalFib = 3.3598856662431775531720113029189271796889051337319684864955538153251303189  # Reciprocal Fibonacci
G = 6.67408e-11
feigenbaum1 = 4.669201609102990671853203821578
feigenbaum2 = 2.502907875095892822283902873218
inf = infinity = Infinity(True)  # Infinity
Ninf = negativeInfinity = Infinity(False)  # Negative Infinity
Cinf = ComplexInfinity = Infinity(None)  # Complex Infinity
nan = float("nan")  # NaN
c = 299792458
