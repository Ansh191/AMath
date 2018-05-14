from .power import root


def geomean(l):
    if len(l) < 2:
        raise ValueError("l must have at least 2 items")
    x = 1
    for n in l:
        x *= n

    return root(abs(x), len(l))


def harmonicmean(l):
    if len(l) < 2:
        raise ValueError("l must have at least 2 items")

    t = 0
    for n in l:
        t += 1 / n

    return n / t


def quadmean(l):
    if len(l) < 2:
        raise ValueError("l must have at least 2 items")

    t = 0
    for n in l:
        t += n * n

    return root(t / n, 2)
