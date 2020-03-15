from .Basic import sqrt
from .power import exp, ln


def sinh(x):
    return (exp(x) - exp(-x)) / 2


def cosh(x):
    return (exp(x) + exp(-x)) / 2


def tanh(x):
    return (exp(2 * x) - 1) / (exp(2 * x) + 1)


def coth(x):
    return (exp(2 * x) + 1) / (exp(2 * x) - 1)


def sech(x):
    return 1 / cosh(x)


def csch(x):
    return 1 / sinh(x)


def arcsinh(x):
    return ln(x + sqrt(x * x + 1))


def arccosh(x):
    return ln(x + sqrt(x * x - 1))


def arctanh(x):
    return 0.5 * ln((1 + x) / (1 - x))


def arccoth(x):
    return 0.5 * ln((x + 1) / (x - 1))


def arcsech(x):
    return ln((1 + sqrt(1 - x * x)) / x)


def arccsch(x):
    return ln(1 / x + sqrt(1 / x ** 2 + 1))
