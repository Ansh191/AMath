from random import uniform


class Function:
    def __init__(self, parts):
        self.parts = parts

    def __repr__(self):
        return ' + '.join(repr(x) for x in self.parts)

    def __call__(self, x):
        return sum(func(x) for func in self.parts)

    def derivative(self, value=None):
        total = 0
        for func in self.parts:
            total += func.derivative()
        if value is not None:
            return total(value)
        return total

    def integrate(self, a=None, b=None):
        total = 0
        for func in self.parts:
            total += func.integrate()

        if a is not None:
            return total(b) - total(a)

        return total

    def find_roots(self):
        pass

    def find_root(self, *, guess=None):
        if self.num_roots() > 0:
            fprime = self.derivative()
            guess = uniform(*self.get_root_bounds()) if guess is None else guess
            while round(self(guess), 14) != 0:
                try:
                    guess = guess - self(guess) / fprime(guess)
                except ZeroDivisionError:
                    guess -= 1

            return guess
        return None

    def num_roots(self):
        return 0

    def get_root_bounds(self):
        return -100, 100
