from amath.constants import inf


def mean(x):
    total = 0
    for i in x:
        total += i
    a = float(total) / len(x)
    return a


def mode(x):
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
