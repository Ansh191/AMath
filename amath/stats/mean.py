from amath.constants import inf


def mean(x):
    a = 0.0
    total = 0
    for i in x:
        if i > inf:
            raise TypeError("A float is required")
        total += i
        a = float(total) / len(x)
    return a


def mode(x):
    f = 0
    x = list(x)
    n = []
    t = 0
    for i in x:
        t1 = x.count(i)
        if t1 == t:
            f = n.count(i)
            if f == 0:
                n.append(i)
                t = t1
        if t1 > t:
            f = n.count(i)
        if f == 0:
            while len(n) > 0:
                n.pop()
            n.append(i)
        t = t1
    if t == 1:
        return None
    else:
        if len(n) == 1:
            return n[0]
        else:
            return n
