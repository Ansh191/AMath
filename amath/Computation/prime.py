from amath.Computation.power import ln
from .SpecialFunctions import li

try:
    import amath.ext._prime as _p
except ModuleNotFoundError:
    print("_prime failed to import")

known_primes = [2, 3]


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True


def primeQ(n: int, prec: int = 30) -> bool:
    """
    Checks if X is prime using Miller-Rabin primality Test
    Uses c-api

    :param prec: precision for very large number( > 3317044064679887385961980 or 3.317e24)
    :param n: suspected prime
    :return: boolean

    >>> primeQ(5)
    True
    >>> primeQ(2)
    True
    >>> primeQ(1)
    False
    >>> primeQ(-5)
    False
    >>> primeQ(20)
    False
    >>> primeQ(29996224275833)
    True
    """
    # from amath.Computation.Basic import sqrt
    # try:
    #     n = int(n)
    # except (ValueError, TypeError):
    #     raise TypeError(str(n) + " is not an integer")
    # if n > 1:
    #     if int(n) == x:
    #         for i in range(2, int(sqrt(n)) + 1):
    #             if (n % i) == 0:
    #                 return False
    #         return True
    # return False

    # from .power import ln
    # from .rounding import floor
    # from .num_properties import frexp
    # from ..testing.types import intQ
    #
    # d, s = frexp(n-1)
    # while not intQ(d):
    #     d *= 2
    #     s -= 1
    # for a in range(2, 3):
    #     if (a**d) % n == 1:
    #         for r in range(1, s - 1):
    #             if (a**((2**r)*d)) % n == n-1:
    #                 return True
    # return False
    # n = abs(n)
    # if n < 10:
    #     if n == 1:
    #         return False
    #     elif n == 0:
    #         return False
    #     for a in range(2, n - 1):
    #         if (a ** (n - 1)) % n != 1:
    #             return False
    # elif n < 58000:
    #     for a in range(2, int(n ** 0.5)):
    #         if (a ** (n - 1)) % n != 1:
    #             return False
    # else:
    #     for a in range(2, int(2 * (ln(n) ** 2))):
    #         if (a ** (n - 1)) % n != 1:
    #             return False
    # return True

    # if n in known_primes:
    #     return True
    # if any((n % p) == 0 for p in known_primes):
    #     return False

    try:
        return _p.primeQ(n)
    except (ValueError, TypeError, AttributeError):
        pass

    if n < 2:
        return False
    if n in known_primes:
        return True
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1

    # print(s)
    # print(d)

    if n < 1373653:
        # print(any(_try_composite(a, d, n, s) for a in (2, 3)))
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    if n < 3825123056546413051:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17, 19, 23))
    if n < 318665857834031151167461:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37))
    if n < 3317044064679887385961981:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41))

    return not any(_try_composite(a, d, n, s) for a in known_primes[:prec])


known_primes += [x for x in range(5, 1000, 2) if primeQ(x)]


def compositeQ(x, prec=30):
    """
    Tests if X is composite

    :param prec:
    :param x:
    :return: boolean

    >>> compositeQ(5)
    False
    >>> compositeQ(6)
    True
    >>> compositeQ(0)
    False
    >>> compositeQ(-2)
    False
    """
    if x == 0:
        return False

    try:
        return _p.compositeQ(x)
    except (ValueError, TypeError, AttributeError):
        pass

    if x > 0:
        if not primeQ(x, prec):
            return True
        else:
            return False
    return False


# def _ln(x):
#     man = None
#     pass


# def prime_generator(lower, upper):
#     if lower % 2 == 0:
#         lower -= 1
#     i = lower
#     current = None
#     while i < upper:
#         if i < 996:
#             i = [j for n, j in enumerate(known_primes) if j > i][0]
#             if i != current:
#                 yield i
#         if not any(i % n == 0 for n in known_primes):
#             print(i)
#             if primeQ(i):
#                 yield i
#         i += 2


def prime(n):
    # f = 2
    # n2 = 0

    try:
        return _p.prime(n)
    except (ValueError, TypeError, AttributeError):
        pass

    if n <= 0:
        raise ValueError("n must be greater than 0")
    elif n < len(known_primes):
        return known_primes[n - 1]

    # while n2 != n:
    #     test = primeQ(f)
    #     if test:
    #         n2 += 1
    #     if n2 == n:
    #         break
    #     f += 1
    # return f
    # a = 2
    # b = int(n * (log(n, e) + log(log(n, e), e)))
    #
    # while a < b:
    #     mid = (a + b) >> 1
    #     if li(mid) > n:
    #         b = mid
    #     else:
    #         a = mid + 1
    # n_primes = primepi(a - 1)
    # while n_primes < n:
    #     if primeQ(a):
    #         n_primes += 1
    #     a += 1
    # return a - 1

    lower = int(n * ln(n) + n * (ln(ln(n)) - 1))
    if lower % 2 == 0:
        lower += 1
    upper = int(n * ln(n) + n * ln(ln(n)))
    print(lower, upper)
    for i in range(lower, upper, 2):
        if not primeQ(i):
            continue
        if primepi(i) == n:
            return i


def _unitstep(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1
    else:
        return


def primepi(n, *, approx=2 ** 40):
    """
    Prime Counting function
    Counts number of prime numbers less than or equal to n
    Will approximate using Prime Number Theorem if n is greater than approx

    :param n: Integer to find the number of primes less than or equal to
    :param approx: Cutoff to start approximating instead of finding exact answers
    :return: Number of primes less than or equal to n

    >>> primepi(100)
    25
    >>> primepi(10000)
    1229
    >>> primepi(61)
    18
    >>> primepi(60)
    17

    Will approximate after approx
    >>> primepi(100, 50)
    29
    >>> primepi(10000, 1000)
    1244
    """
    if n > approx:
        return int(li(n) - li(2))

    try:
        return _p.primepi(int(n))
    except (ValueError, TypeError, AttributeError):
        pass

    n = int(n)
    if n < 2:
        return 0
    # if n <= sieve._list[-1]:
    #     return sieve.search(n)[0]
    lim = int(n ** 0.5)
    lim -= 1
    lim = max(lim, 0)
    while lim * lim <= n:
        lim += 1
    lim -= 1
    arr1 = [0] * (lim + 1)
    arr2 = [0] * (lim + 1)
    for i in range(1, lim + 1):
        arr1[i] = i - 1
        arr2[i] = n // i - 1
    for i in range(2, lim + 1):
        # Presently, arr1[k]=phi(k,i - 1),
        # arr2[k] = phi(n // k,i - 1)
        if arr1[i] == arr1[i - 1]:
            continue
        p = arr1[i - 1]
        for j in range(1, min(n // (i * i), lim) + 1):
            st = i * j
            if st <= lim:
                arr2[j] -= arr2[st] - p
            else:
                arr2[j] -= arr1[n // st] - p
        lim2 = min(lim, i * i - 1)
        for j in range(lim, lim2, -1):
            arr1[j] -= arr1[j // i] - p
    return arr2[1]


def nextprime(n):
    test = False
    try:
        n = int(n)
    except (ValueError, TypeError):
        raise TypeError(str(n) + " is not an integer")
    f = n + 1
    if n < 0:
        raise ValueError("n must be greater than 0")
    while not test:
        test = primeQ(f)
        if test:
            break
        f += 1
    return f


def primenumber(n):
    if not primeQ(n):
        raise ValueError(str(n) + " is not a prime number")
    return primepi(n) + 1


def prime_factor(n):
    if n <= 0:
        raise ValueError("n must be greater than 0")
    try:
        return _p.prime_factor(n)
    except (TypeError, NameError):
        pass

    primes = []
    while n != 1:
        for i in range(1, primepi(n) + 1):
            x = prime(i)
            if n % x == 0:
                n //= x
                primes.append(x)
                break
    return primes
