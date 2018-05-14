class RepeatingDecimal(object):
    def __new__(cls, v, rep=None):
        from amath.testing.types import intQ, isReal
        self = object.__new__(cls)
        if rep is not None:
            if not intQ(v):
                raise TypeError("If repeating decimal is defined, value must have an integer value")
            if not isReal(rep):
                raise TypeError("Repeating decimal must be a float or a string")

        else:
            if not isReal(v):
                raise TypeError("value must be a float or a string")
            self.value = int(v)
            v = str(v)
            index = v.find('.')
            if index == -1:
                raise ValueError("Value must be a float or a string, not an int")
            self.rep = v[index + 1:]

        return self
