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
    except TypeError as tp:
        if "callable" in str(tp.args):
            raise TypeError("f must be a function")
        elif "arguments" in str(tp.args):
            raise TypeError("f must take only 1 argument")
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
    >>> from amath.Computation.prime import primeQ
    >>> delcases([1,2,3,4,5], primeQ)
    [1, 4]
    """
    p = []
    try:
        if type(f(2)) != bool:
            raise TypeError("Function must return Boolean value")
    except TypeError as tp:
        if "callable" in str(tp.args):
            raise TypeError("f must be a function")
        elif "arguments" in str(tp.args):
            raise TypeError("f must take only 1 argument")
        else:
            raise
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

    >>> from amath.Computation.prime import primeQ
    >>> cases([2,3,4], primeQ)
    [4]
    >>> cases([4,6,8], primeQ)
    [4, 6, 8]
    """
    p = []
    try:
        if type(f(2)) != bool:
            raise TypeError("Function must return Boolean value")
    except TypeError as tp:
        if "callable" in str(tp.args):
            raise TypeError("f must be a function")
        elif "arguments" in str(tp.args):
            raise TypeError("f must take only 1 argument")
        else:
            raise
    if type(l) != list:
        raise TypeError("l must be a list")
    for i in l:
        if not f(i):
            p.append(i)
    return p


def nonetrue(l, f):
    try:
        if type(f(2)) != bool:
            raise TypeError("Function must return Boolean value")
    except TypeError as tp:
        if "callable" in str(tp.args):
            raise TypeError("f must be a function")
        elif "arguments" in str(tp.args):
            raise TypeError("f must take only 1 argument")
        else:
            raise
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

    >>> from amath.Computation.prime import primeQ
    >>> anytrue([1,4,6,9], primeQ)
    False
    >>> anytrue([1,4,6,13], primeQ)
    True
    """
    try:
        if type(f(2)) != bool:
            raise TypeError("Function must return Boolean value")
    except TypeError as tp:
        if "callable" in str(tp.args):
            raise TypeError("f must be a function")
        elif "arguments" in str(tp.args):
            raise TypeError("f must take only 1 argument")
        else:
            raise
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

    >>> from amath.Computation.prime import primeQ
    >>> alltrue([2,3,5], primeQ)
    True
    >>> alltrue([2,3,4], primeQ)
    False
    """
    try:
        if type(f(2)) != bool:
            raise TypeError("Function must return Boolean value")
    except TypeError as tp:
        if "callable" in str(tp.args):
            raise TypeError("f must be a function")
        elif "arguments" in str(tp.args):
            raise TypeError("f must take only 1 argument")
        else:
            raise
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

    >>> from amath.Computation.prime import primeQ
    >>> choose([1,2,3], primeQ)
    [2, 3]
    """
    try:
        if type(f(2)) != bool:
            raise TypeError("Function must return Boolean value")
    except TypeError as tp:
        if "callable" in str(tp.args):
            raise TypeError("f must be a function")
        elif "arguments" in str(tp.args):
            raise TypeError("f must take only 1 argument")
        else:
            raise
    o = []
    for x in l:
        if f(x):
            o.append(x)
    return o


def reorder(x, tp="quicksort", r=False):
    # type: (list, str, bool) -> list
    """
    Reorders the list
    :param x: list to be reordered
    :param tp: method used to sort
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


def selectionsort(l: list):
    array = list(l)
    for i in range(0, len(array) - 1):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest]:
                smallest = j

        if smallest != i:
            array[i], array[smallest] = array[smallest], array[i]

    return array


def insertionsort(l: list):
    array = list(l)
    for i in range(1, len(array)):

        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return array


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) / 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
