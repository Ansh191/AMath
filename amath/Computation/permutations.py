from .Basic import fac


def comb(n, k):
    if k > n:
        return 0
    if k < 0:
        return 0
    return float(fac(n)) / float(fac(k) * fac(n - k))


def perm(n, k):
    if k > n:
        return 0
    if k < 0:
        raise ValueError("k must be non-negative")
    return float(fac(n)) / float(fac(n - k))
