from amath.constants import inf
from amath.testing.types import isReal


# from range import range

class count:
    def __init__(self, start, step=1):
        if not isReal(start):
            raise TypeError("A number is required")
        if not isReal(step):
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
            for _ in p:
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
        from amath.DataTypes.Infinity import Infinity
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


class range:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            raise TypeError("range() takes exactly 1, 2 or 3 arguments ({0} given)".format(len(args)))

        if self.start > self.stop:
            raise TypeError("Start should be less than stop")
        if self.step < 0:
            lo, hi = self.stop, self.start
        else:
            lo, hi = self.start, self.stop
        self.length = ((hi - lo - 1) // abs(self.step)) + 1

    def __repr__(self):
        if self.step == 1:
            return "range({0}, {1})".format(self.start, self.stop)
        else:
            return "range({0}, {1}, {2})".format(self.start, self.stop, self.step)

    def __iter__(self):
        current = self.start
        if self.step < 0:
            while current > self.stop:
                yield current
                current += self.step
        else:
            while current < self.stop:
                yield current
                current += self.step

    def __len__(self):
        return self.length

    def __getitem__(self, item):

        if isinstance(item, slice):
            start = 0
            stop = self.stop
            if 0 <= item.start < self.length:
                start = self.start + item.start * self.step
            if 0 <= item.stop < self.length:
                stop = self.start + item.stop * self.step
            if item.step is None:
                return range(start, stop)
            else:
                return range(start, stop, item.step)

        if 0 <= item < self.length:
            return self.start + item * self.step
        raise IndexError("Index out of range: {}".format(item))

    def __contains__(self, num):
        if self.step < 0:
            if not (self.stop < num <= self.start):
                return False
        else:
            if not (self.start <= num < self.stop):
                return False
        return (num - self.start) % self.step == 0
