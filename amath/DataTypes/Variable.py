from amath.string_proccessing.strings import chars, numbers


class Variable:
    def __init__(self, name):
        self.name = ""
        self.coefficent = 1
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if " " in name:
            raise ValueError("Name must be one word")
        if len(name) == 0:
            raise ValueError("Name must be at least one character long")
        for c in chars:
            if c in name:
                raise ValueError("Name cannot contain: {0}".format(chars))
        for n in numbers:
            if n in name:
                raise ValueError("Name cannot contain: {0}".format(numbers))

        self.name = name
        self.coefficent = 1
        self.exponent = 1

    def __repr__(self):
        if self.exponent is 1:
            return "{0}{1}".format(self.coefficent, self.name)
        else:
            return "{0}{1}**{2}".format(self.coefficent, self.name, self.exponent)

    def __mul__(self, other):
        if isinstance(other, Variable):
            if other.name == self.name:
                exp = self.exponent + other.exponent
                coe = self.coefficent * other.coefficent
                v = Variable(self.name)
                v.exponent = exp
                v.coefficent = coe
                return v
            else:
                pass
        coefficient = other
        v = Variable(self.name)
        v.coefficent = coefficient
        return v

    def __rmul__(self, other):
        self.__mul__(other)

    def __add__(self, other):
        if isinstance(other, Variable):
            if other.name == self.name:
                coefficent = self.coefficent + other.coefficent
                return Variable(self.name) * coefficent
