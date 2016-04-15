

def gcd(x, y):
    try:
        x = float(x)
        y = float(y)
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


def lcm(x, y):
    try:
        answer = float(abs(x * y)) / gcd(x, y)
    except ZeroDivisionError:
        raise ValueError("both x and y cannot be 0")
    except TypeError:
        raise TypeError("A float is required")
    if answer.is_integer():
        return int(answer)
    else:
        return answer
