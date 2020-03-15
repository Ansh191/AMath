from amath.constants import epsilon
from .Basic import fac
from .permutations import binomial


def derivative(func, value, step=None):
    if step is None:
        step = epsilon ** 0.5 * (epsilon ** 0.5 + abs(value))
    return round((func(value + step) - func(value - step)) / (2 * step), 6)


def nth_derivative(func, n, value, step=None):
    if step is None:
        step = 2 ** -10

    sum = 0
    for k in range(0, n + 1):
        sum += pow(-1, k + n) * binomial(n, k) * func(value + k * step)

    return sum / pow(step, n)


def TaylorSeries(func, value, num=5):
    def Taylor(x):
        sum = 0
        for n in range(num + 1):
            sum += nth_derivative(func, n, value) * pow(x - value, n) / fac(n)

        return sum

    return Taylor


def Limit(func, value, step=None):
    try:
        result1 = func(value)
        return result1
    except:
        pass

    if step is None:
        step = epsilon ** 0.5 * (epsilon ** 0.5 + abs(value))

    result2 = func(value + step)

    return round(result2, 5)


def Integrate(f, a, b, steps=1000, *, skip=None, ignore=False, ignoreA=False, ignoreB=False):
    h = (b - a) / steps
    a1 = a + h / 2
    if skip is not None:
        s1 = sum(f(a1 + i * h) for i in (x for x in range(0, steps) if a1 + x * h != skip))
        s2 = sum(f(a + i * h) for i in (x for x in range(1, steps) if a + x * h != skip))
    else:
        s1 = sum(f(a1 + i * h) for i in range(0, steps))
        s2 = sum(f(a + i * h) for i in range(1, steps))
    try:
        return (h / 6) * (f(a) + f(b) + 4 * s1 + 2 * s2)
    except ZeroDivisionError:
        if ignore:
            a += h
            b -= h
            return (h / 6) * (f(a) + f(b) + 4 * s1 + 2 * s2)
        if ignoreA:
            a += h
            return (h / 6) * (f(a) + f(b) + 4 * s1 + 2 * s2)
        if ignoreB:
            b -= h
            return (h / 6) * (f(a) + f(b) + 4 * s1 + 2 * s2)
        raise
