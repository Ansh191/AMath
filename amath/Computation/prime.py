from amath.Errors import TimeoutException, IDEError
from amath.testing.number import primeQ


def prime(n):
    f = 2
    n2 = 0
    if n <= 0:
        raise ValueError("n must be greater than 0")
    if n > 1e6:
        try:
            z = raw_input("Are you sure you want to continue? This will take a while:(y or n) ")
            if z == "n":
                raise TimeoutException()
        except EOFError:
            raise IDEError("Please use another IDE as this one doesn't support raw_input")
    while n2 != n:
        test = primeQ(f)
        if test:
            n2 += 1
        if n2 == n:
            break
        f += 1
    return f


def primepi(n):
    f = 2
    n2 = 0
    if n <= 0:
        raise ValueError("n must be greater than 0")
    if n > 1000000:
        try:
            z = raw_input("Are you sure you want to continue? This will take a while:(y or n) ")
            if z == "n":
                raise TimeoutException()
        except EOFError:
            raise IDEError("Please use another IDE as this one doesn't support raw_input")
    while f < n:
        test = primeQ(f)
        if test:
            n2 += 1
        if f >= n:
            break
        f += 1
    return n2


def nextprime(n):
    f = n + 1
    test = False
    if n < 0:
        raise ValueError("n must be greater than 0")
    while not test:
        test = primeQ(f)
        if test:
            break
        f += 1
    return f


del TimeoutException, IDEError, primeQ
