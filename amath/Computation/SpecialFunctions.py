from .Basic import sqrt, gamma, fac, rising_factorial
from .Calculus import Integrate
from .complex import arg
from .permutations import binomial
from .power import ln, exp
from .rounding import floor
from .trig import cos, sin
from ..constants import e, pi, inf, EulerMascheroni, Cinf
from ..testing.types import intQ, isWhole

try:
    import amath.ext._specialf as _s
except ImportError:
    print("Special Function extension failed")
    pass

GammaN = 10

GammaR = 10.900511

GammaDk = [2.48574089138753565546e-5, 1.05142378581721974210, -3.45687097222016235469, 4.51227709466894823700,
           -2.98285225323576655721, 1.05639711577126713077, -1.95428773191645869583e-1, 1.70970543404441224307e-2,
           -5.71926117404305781283e-4, 4.63399473359905636708e-6, -2.71994908488607703910e-9]


def gammaLn(z):
    try:
        return _s.gammaLn(z)
    except (TypeError, NameError):
        pass

    try:
        s = GammaDk[0]
        i = 1
        while i <= GammaN:
            s += GammaDk[i] / (z + i - 1.0)
            i += 1

        return ln(s) + ln(2 * sqrt(e / pi)) + ((z - 0.5) * ln((z - 0.5 + GammaR) / e))
    except OverflowError:
        raise


def facLn(x):
    try:
        return _s.facLn(x)
    except (TypeError, NameError):
        return gammaLn(x + 1)


def binomialLn(n, k):
    try:
        return _s.binomialLn(n, k)
    except (TypeError, NameError):
        return facLn(n) - facLn(k) - facLn(n - k)


def multinomial(n, k):
    if n < 0:
        raise ValueError("n must be positive")
    sum = 0
    ret = facLn(n)
    for i in k:
        if i < 0:
            raise ValueError("all values of k must be positive")
        ret -= facLn(i)
        sum += i

    if sum != n:
        raise ValueError("sum of all values of k must equal n")

    return floor(.5 + exp(ret))


def logistic(x):
    try:
        return _s.logistic(x)
    except (TypeError, NameError):
        return 1.0 / (exp(-x) + 1.0)


def logit(x):
    try:
        return _s.logit(x)
    except (TypeError, NameError):
        pass

    if x == 1:
        return inf

    return ln(x / (1.0 - x))


def erf(x):
    if x == 0:
        return 0
    t = 1 / (1 + 0.5 * abs(x))
    tau = t * exp(
        -x ** 2 - 1.26551223 + 1.00002368 * t + 0.37409196 * t ** 2 + 0.09678418 * t ** 3 - 0.18628806 * t ** 4 +
        0.27886807 * t ** 5 - 1.13520398 * t ** 6 + 1.48851587 * t ** 7 - 0.82215223 * t ** 8 + 0.17087277 * t ** 9)
    if x > 0:
        return 1 - tau
    return tau - 1


def erfc(x):
    return 1 - erf(x)


def lower_gamma(s, x):
    if s == 1:
        return 1 - exp(-x)
    if s == 0.5:
        return sqrt(pi) * erf(sqrt(x))
    return Integrate(lambda t: pow(t, s - 1) * exp(-t), 0, x)


def upper_gamma(s, x):
    if x == 0 and s.real > 0:
        return gamma(s)
    if s == 0 and x.real > 0:
        return expIntegralE(1, x)
    if s == 1:
        return exp(-x)
    if s == 0.5:
        return sqrt(pi) * erfc(sqrt(x))
    if s.real < 0:
        total = 0
        n = -s
        for k in range(n):
            total += pow(-1, k) * fac(n - k - 1) * pow(x, k) + pow(-1, n) * upper_gamma(0, x)
        return (1 / fac(n)) * (exp(-x) / pow(x, n)) * total
    return gamma(s) - lower_gamma(s, x)


def digamma(z):
    if z < 6:
        return digamma(z + 1) - 1 / z
    return ln(z) - (1 / (2 * z)) - (1 / (12 * z ** 2)) + (1 / (120 * z ** 4)) - (1 / (252 * z ** 6)) + (1 / (
            240 * z ** 8)) - (5 / (660 * z ** 10)) + (691 / (32760 * z ** 12)) - (1 / (12 * z ** 14))


def exp_integral(n, x):
    return pow(x, n - 1) * upper_gamma(1 - n, x)


def besselJ(n, x):
    total = 0
    for m in range(100):
        total += pow(-1, m) / (fac(m) * gamma(m + n + 1)) * pow(x / 2, 2 * m + n)
    return total


def besselY(n, x):
    if intQ(n):
        n += 0.00001
    return (besselJ(n, x) * cos(n * pi) - besselJ(-n, x)) / sin(n * pi)


def hankelH1(n, x):
    return besselJ(n, x) + besselY(n, x) * 1j


def hankelH2(n, x):
    return besselJ(n, x) - besselY(n, x) * 1j


def besselI(n, z):
    total = 0
    for m in range(100):
        total += 1 / (fac(m) * gamma(m + n + 1)) * pow(z / 2, 2 * m + n)
    return total


def besselK(n, z):
    if intQ(n):
        n += 0.00001
    return (pi / 2) * (besselI(-n, z) - besselI(n, z)) / sin(n * pi)


def sphericalbesselJ(n, x):
    return sqrt(pi / (2 * x)) * besselJ(n + 0.5, x)


def sphericalbesselY(n, x):
    return sqrt(pi / (2 * x)) * besselY(n + 0.5, x)


def sphericalhankelH1(n, x):
    return sphericalbesselJ(n, x) + sphericalbesselY(n, x) * 1j


def sphericalhankelH2(n, x):
    return sphericalbesselJ(n, x) - sphericalbesselY(n, x) * 1j


def hypergeometric1F1(a, b, z):
    total = 0
    for n in range(100):
        total += (rising_factorial(a, n) * pow(z, n)) / (rising_factorial(b, n) * fac(n))
    return total


def expIntegralEin(z):
    total = 0
    for k in range(1, 100):
        total += (pow(-1, k + 1) * pow(z, k)) / (k * fac(k))
    return total


def expIntegralEi(x):
    if x.real > 0:
        return EulerMascheroni + ln(x) - expIntegralEin(-x)
    # total = 0
    # for n in range(100):
    #     total += fac(n) / pow(x, n)
    # return exp(x) * total / x

    # return EulerMascheroni + ln(x) + exp(x / 2) * sum(pow(-1, n-1) * pow(x, n) / (fac(n) * pow(2, n - 1)) * sum(1 / (2 * k + 1) for k in range(0, int((n - 1) / 2))) for n in range(1, 100))


def li(x, prec=5):
    """
    Calculate Logarithmic Integral
    Integral over the interval from 0 to x of 1/ln(x) with respect to x

    :param x: Number
    :param prec: desired precision of Integral (number of steps)
    :return: Logarithmic Integral of x

    >>> li(1)
    -inf
    >>> li(0)
    0
    >>> li(100)
    30.124684616781
    >>> li(.5)
    -0.37867041071746765
    """
    if x == 0:
        return 0
    elif x == 1:
        return float('-inf')

    # return Integrate(lambda k: 1 / ln(k), 0, x, 10 ** prec, skip=1)
    # return expIntegralEi(ln(x))
    return EulerMascheroni + ln(abs(x)) + sum(pow(x, n) / (n * fac(n)) for n in range(1, prec))


def expIntegralE(n, z):
    if n == 1 and abs(arg(z)) < pi:
        return -EulerMascheroni - ln(z) + expIntegralEin(z)


def zeta(s):
    if s == 0:
        return -0.5
    if s == 1:
        return Cinf
    if s == 2:
        return pi ** 2 / 6
    if s == 4:
        return pi ** 4 / 90
    if s == 6:
        return pi ** 6 / 945
    if s < 0 and s % 2 == 0:
        return 0
    if s < 0 and intQ(s):
        return bernoulliB(-s + 1) / (-s + 1)
    return sum(pow(n, -s) for n in range(1, 1000))


def bernoulliB(n, x=0):
    if not isWhole(n):
        raise TypeError("n must be an non-negative integer")
    if x == 0:
        if n == 0:
            return 1
        if n == 1:
            return -0.5
        if n % 2 == 1:
            return 0
        return pow(-1, n // 2 + 1) * 2 * fac(n) / pow(2 * pi, n) * zeta(n)
    return sum(binomial(n, k) * bernoulliB(k) * pow(x, n - k) for k in range(0, n + 1))
    # total = 0
    # for k in range(n+1):
    #     total += binomial(n, k) * bernoulliB(k) * pow(x, n - k)
    # return total
