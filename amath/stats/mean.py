import amath.ext._statistics as s


def mean(x):
    # type: (list) -> float
    return s.mean(list(x))


def mode(x):
    # type: (list) -> object
    x = list(x)
    t = 0
    w = None
    for i in x:
        t1 = x.count(i)
        if t1 > t:
            w = i
            t = t1
            while True:
                try:
                    x.remove(i)
                except ValueError:
                    break
        elif t1 == t:
            if isinstance(w, list):
                w.append(i)
            else:
                v = w
                w = [v, i]
    return w


def median(x):
    # type: (list) -> float
    """

    :type x: list
    """
    return s.median(list(x))
