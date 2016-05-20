from amath.constants import inf
from amath.DataTypes.Infinity import Infinity


class count:
    def __init__(self, start, step=1):
        try:
            start + step
        except TypeError:
            raise TypeError("A number is required")
        self.start = start
        self.step = step
        self.value = start

    def __repr__(self):
        return "count({0}, {1})".format(self.value, self.step)

    def next(self):
        v = self.value
        self.value += self.step
        return v

    def reset(self):
        self.value = self.start

    def __iter__(self):
        return self

    def __next__(self):
        v = self.value
        self.value += self.step
        return v


class cycle:
    def __init__(self, p):
        try:
            for i in p:
                break
        except TypeError:
            raise
        self.iter = p
        self.c = 0

    def __repr__(self):
        return "cycle({0})".format(self.iter)

    def next(self):
        c = self.c
        if c+1 < len(self.iter):
            self.c += 1
        else:
            self.c = 0
        return self.iter[c]

    def __iter__(self):
        return self

    def __next__(self):
        c = self.c
        if c + 1 < len(self.iter):
            self.c += 1
        else:
            self.c = 0
        return self.iter[c]


class repeat:
    def __init__(self, p, n=inf):
        import sys
        if not isinstance(n, int):
            if not isinstance(n, Infinity):
                if sys.version_info[0] > 3:
                    raise TypeError("An integer is required")
                else:
                    if not isinstance(n, long):
                        raise TypeError("An integer is required")

        self.x = p
        self.n = n
        del sys

    def __repr__(self):
        return "repeat({0}, {1})".format(self.x, self.n)

    def next(self):
        if self.n <= 0:
            raise StopIteration
        else:
            self.n -= 1
            return self.x

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        else:
            self.n -= 1
            return self.x
