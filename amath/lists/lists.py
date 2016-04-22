from amath.testing import primeQ


def reverse(l):
    if type(l) != list:
        raise TypeError("l must be a list")
    return l.reverse()


def applylist(l, f):
    """
    Applies what ever f returns onto list
    :param l: list
    :param f: function
    :return:

    >>> from amath.Computation.Basic import fac
    >>> applylist([1,2,3,4], fac)
    [1, 2, 6, 24]
    """
    try:
        f(2)
    except TypeError:
        raise TypeError("f must be a function")
    if type(l) is not list:
        raise TypeError("l must be a list")
    x = []
    for i in l:
        x.append(f(i))
    return x


def deldup(l):
    """
    Delete duplicates
    :param l:
    :return:

    WARNING:
        DOES NOT RETAIN ORDER

    >>> deldup([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    >>> deldup([1,1,1,1,1])
    [1]
    >>> deldup([1,1,3,5,6,3,5])
    [1, 3, 5, 6]
    """
    x = list(set(l))
    return x


def delcases(l, f):
    """
    Delete all cases that match abide with X
    :param l:
    :param f:
    :return:

    >>> delcases([1,2,3,4,5], primeQ)
    [1, 4]
    """
    p = []
    try:
        if type(f(2)) != bool:
            raise ValueError("Function must return Boolean value")
    except TypeError:
        raise TypeError(str(f) + " is not a function")
    if type(l) != list:
        raise TypeError(str(l) + " is not a list")
    for i in l:
        if not f(i):
            p.append(i)
    return p


def cases(l, f):
    """
    Returns list where objects don't abide by f
    :param l:
    :param f:
    :return:

    >>> cases([2,3,4], primeQ)
    [4]
    >>> cases([4,6,8], primeQ)
    [4, 6, 8]
    """
    p = []
    try:
        if type(f(2)) != bool:
            raise ValueError("Function must return Boolean value")
    except TypeError:
        raise TypeError("f must be a function")
    if type(l) != list:
        raise TypeError("l must be a list")
    for i in l:
        if not f(i):
            p.append(i)
    return p


def nonetrue(l, f):
    try:
        if type(f(2)) != bool:
            raise ValueError("Function must return Boolean value")
    except TypeError:
        raise TypeError("f must be a function")
    for x in l:
        if f(x):
            return False
    return True


def anytrue(l, f):
    """
    Tests if ANY object in l is true with the function f
    :type f: function
    :type l: list
    :param l: list
    :param f: function that returns a boolean
    :return:

    >>> anytrue([1,4,6,9], primeQ)
    False
    >>> anytrue([1,4,6,13], primeQ)
    True
    """
    try:
        if type(f(2)) != bool:
            raise ValueError("Function must return Boolean value")
    except TypeError:
        raise TypeError("f must be a function")
    for x in l:
        if f(x):
            return True
    return False


def alltrue(l, f):
    """
    Tests if ALL objects in l is true with the function f
    :param l: list
    :param f: function that returns a boolean value
    :return: boolean

    >>> alltrue([2,3,5], primeQ)
    True
    >>> alltrue([2,3,4], primeQ)
    False
    """
    try:
        if type(f(2)) != bool:
            raise ValueError("Function must return Boolean value")
    except TypeError:
        raise TypeError("f must be a function")
    for x in l:
        if not f(x):
            return False
    return True


def choose(l, f):
    """
    Look at cases. Opposite
    :param l:
    :param f:
    :return:

    >>> choose([1,2,3], primeQ)
    [2, 3]
    """
    try:
        if type(f(2)) != bool:
            raise ValueError("Function must return Boolean value")
    except TypeError:
        raise TypeError("f must be a function")
    o = []
    for x in l:
        if f(x):
            o.append(x)
    return o


def reorder(x, r = False):
    # type: (list, bool) -> list
    """
    Reorders the list
    :param x: list to be reordered
    :param r: reverse
    :return: ordered list

    >>> reorder([1,3,2])
    [1, 2, 3]
    """
    o = list(x)
    o.sort()
    if r:
        o.reverse()
    return o
