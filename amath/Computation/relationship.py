def gcd(*n):
    """
    Find the greatest common denominator.
    :param n: list of numbers to find GCD of
    :return:

    >>> gcd(10,2)
    2.0
    >>> gcd(240, 99)
    3.0
    >>> gcd(5,234)
    1.0
    >>> gcd(23, 81)
    1.0
    """
    if len(n) < 1:
        raise TypeError("gcd() takes a minimum of 1 arguments")
    if len(n) == 1:
        return n[0]
    result = n[0]
    for i in range(1, len(n)):
        result = _gcd(result, n[i])
    return result


def _gcd(x, y):
    try:
        x = int(x)
        y = int(y)
    except:
        raise TypeError("{0} or {1} are not numbers".format(str(x), str(y)))

    x = abs(x)
    y = abs(y)
    while x != 0 or y != 0:
        if x < y:
            f = x
            x = y
            y = f
        if x == 0:
            return y
        elif y == 0:
            return x
        z = x % y
        x = z
    return 0


def lcm(*n):
    if len(n) < 1:
        raise TypeError("lcm() takes a minimum of 1 arguments")
    if len(n) == 1:
        return n[0]
    result = n[0]
    for i in range(1, len(n)):
        result = _lcm(result, n[i])
    return result


def _lcm(x, y):
    try:
        return int(abs(x * y) / _gcd(x, y))
    except ZeroDivisionError:
        raise ValueError("Both x and y cannot be 0")
