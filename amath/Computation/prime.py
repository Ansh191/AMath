from amath.Errors import TimeoutException, IDEError


def primeQ(x):
    """
    Checks if X is prime
    :param x: suspected prime
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
    >>> primeQ(5.5)
    Traceback (most recent call last):
    TypeError: 5.5 is not an integer
    """
    if type(x) is not int:
        raise TypeError(str(x) + " is not an integer")
    if x > 1:
        if int(x) == x:
            for i in range(2, x):
                if (x % i) == 0:
                    return False
            return True
    return False



def compositeQ(x):
    """
    Tests if X is compisite
    :param x:
    :return: boolean

    >>> compositeQ(5)
    False
    >>> compositeQ(2.5)
    False
    >>> compositeQ(6)
    True
    >>> compositeQ(0)
    False
    >>> compositeQ(-2)
    False
    """
    if type(x) is int:
        if x > 0:
            if not primeQ(x):
                return True
            else:
                return False
    return False


def prime(n):
    f = 2
    n2 = 0
    if n <= 0:
        raise ValueError("n must be greater than 0")
    if n > 1e6:
        try:
            # noinspection PyCompatibility
            z = raw_input("Are you sure you want to continue? This will take a while:(y or n) ")
            if z == "n":
                raise TimeoutException()
        except EOFError:
            raise IDEError("Please use another IDE as this one doesn't support raw_input")
        except NameError:
            z = input("Are you sure you want to continue? This will take a while:(y or n) ")
            if z == "n":
                raise TimeoutException()
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
            # noinspection PyCompatibility
            z = raw_input("Are you sure you want to continue? This will take a while:(y or n) ")
            if z == "n":
                raise TimeoutException()
        except EOFError:
            raise IDEError("Please use another IDE as this one doesn't support raw_input")
        except NameError:
            z = input("Are you sure you want to continue? This will take a while:(y or n) ")
            if z == "n":
                raise TimeoutException()
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

# def primeFactorize(n):
#    if
