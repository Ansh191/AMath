from __future__ import division


def sqrt(x):
    """Returns square root of X

    Returns a float

    >>> sqrt(16)
    4.0
    >>> sqrt(25)
    5.0
    >>> sqrt(2)
    1.4142135623730951

    If X is negative, Returns a complex number

    >>> sqrt(-1)
    1j
    >>> sqrt(-16)
    4j

    Can accept Fractions and floats

    >>> sqrt(5.5)
    2.345207879911715
    >>> sqrt(Fraction(16,4))
    2
    """
    if type(x) is complex:
        return x ** (0.5)
    if type(x) is not int:
        if type(x) is not float:
            if not isinstance(x, Fraction):
                raise TypeError(str(x) + " is not a float")
    if x < 0:
        return sqrt(abs(x)) * 1j
    return x ** (0.5)


class _Infinity:
    def __init__(self, n):
        if type(n) is not bool:
            if n is not None:
                raise TypeError("n must be bool")
        self.n = n

    def __cmp__(self, other):
        if isinstance(other, _Infinity):
            if other.n == self.n:
                return 0
        if self.n:
            return 1
        elif self.n == False:
            return -1
        else:
            raise Failure("Cannot be compared")

    def __add__(self, other):
        if isinstance(other, _Infinity):
            if other.n == self.n:
                return self
        if isinstance(other, _Infinity):
            return float("NaN")
        return self

    def __sub__(self, other):
        if isinstance(other, _Infinity):
            if other.n == self.n:
                return self
        if isinstance(other, _Infinity):
            return float("NaN")
        return self

    def __truediv__(self, other):
        if isinstance(other, _Infinity):
            return float("NaN")
        else:
            return self

    def __div__(self, other):
        return self.__truediv__(other)

    def __repr__(self):
        if self.n:
            return "inf"
        elif self.n == False:
            return "-inf"
        else:
            return "Complex Infinity"


Infinity = type("Infinity", (_Infinity, object), {})


class block:
    def __init__(self):
        self.__doc__ = "Used to make blocks using the with statement"

    def __enter__(self):
        return self

    def __exit__(self, tp, value, traceback):
        try:
            del self.__doc__
            del self.__enter__
            del self.__exit__
            del self.__init__
            del self
        except:
            pass

    def __repr__(self):
        return self.__doc__


class decimal:
    def __init__(self, value):
        if value is str:
            self.v = value
        else:
            self.v = str(value)

    def __repr__(self):
        return self.v

    def __add__(self, other):
        raise SyntaxError("EOL while scanning string literal")


"""Constants"""

import sys as _sys

# _sys.tracebacklimit = 0
del _sys

e = 2.71828182845904523536028747135266249775724709369995957496696762772407
6630353547594571382178525166427427466391932003059921817413596629043572
9003342952605956307381323286279434907632338298807531952510190115738341
8793070215408914993488416750924476146066808226480016847741185374234544
2437107539077744992069551702761838606261331384583000752044933826560297
6067371132007093287091274437470472306969772093101416928368190255151086
5746377211125238978442505695369677078544996996794686445490598793163688
9230098793127736178215424999229576351482208269895193668033182528869398
4964651058209392398294887933203625094431173012381970684161403970198376
79320683282376464804295311802328782509819455815301756717361332069811250996181881593041690351598888519345807273866738589422879228499892086805
8257492796104841984443634632449684875602336248270419786232090021609902
3530436994184914631409343173814364054625315209618369088870701676839642
4378140592714563549061303107208510383750510115747704171898610687396965
5212671546889570350354021234078498193343210681701210056278802351930332
2474501585390473041995777709350366041699732972508868769664035557071622
6844716256079882651787134195124665201030592123667719432527867539855894
4896970964097545918569563802363701621120477427228364896134225164450781
8244235294863637214174023889344124796357437026375529444833799801612549
2278509257782562092622648326277933386566481627725164019105900491644998
2893150566047258027786318641551956532442586982946959308019152987211725
5634754639644791014590409058629849679128740687050489585867174798546677
5757320568128845920541334053922000113786300945560688166740016984205580
4033637953764520304024322566135278369511778838638744396625322498506549
95886234281899707733276171783928034946501434558897071942586398772754710962953741521115136835062752602326484728703920764310059584116612054529
7030236472549296669381151373227536450988890313602057248176585118063036
4428123149655070475102544650117272115551948668508003685322818315219600
37356252794495158284188294787610852639814  # e
pi = 3.14159265358979323846264338327950288419716939937510582097494459230781
6406286208998628034825342117067982148086513282306647093844609550582231
7253594081284811174502841027019385211055596446229489549303819644288109
7566593344612847564823378678316527120190914564856692346034861045432664
8213393607260249141273724587006606315588174881520920962829254091715364
3678925903600113305305488204665213841469519415116094330572703657595919
5309218611738193261179310511854807446237996274956735188575272489122793
8183011949129833673362440656643086021394946395224737190702179860943702
7705392171762931767523846748184676694051320005681271452635608277857713
4275778960917363717872146844090122495343014654958537105079227968925892
3542019956112129021960864034418159813629774771309960518707211349999998
3729780499510597317328160963185950244594553469083026425223082533446850
35261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927
8766111959092164201989380952572010654858632788659361533818279682303019
5203530185296899577362259941389124972177528347913151557485724245415069
59508295331168617278558890750983817546374649393192550604009277016711390098488240128583616035637076601047101819429555961989467678374494482553
7977472684710404753464620804668425906949129331367702898915210475216205
6966024058038150193511253382430035587640247496473263914199272604269922
7967823547816360093417216412199245863150302861829745557067498385054945
8858692699569092721079750930295532116534498720275596023648066549911988
18347977535663698074265425278625518184175746728909777727938000816470600161452491921732172147723501414419735685481613611573525521334757418494
6843852332390739414333454776241686251898356948556209921922218427255025
4256887671790494601653466804988627232791786085784383827967976681454100
9538837863609506800642251252051173929848960841284886269456042419652850
2221066118630674427862203919494504712371378696095636437191728746776465
75739624138908658326459958133904780275901  # pi
gr = goldenratio = (1 + sqrt(5)) / 2.0  # Golden Ratio
ec = EuterMascheroni = 0.5772156649015328606065120900824024310421  # Euler–Mascheroni constant
O = Omega = 0.5671432904097838729999686622103555497538157871865125081351310792230457930866  # Omega
rf = reciprocalfib = 3.35988566624317755317201130291892717968890513373196848649555381532513031899668338361541621645679008729704  # Reciprocal Fibonacci
G = 6.67408e-11
inf = infinity = Infinity(True)  # Infinity
Ninf = negativeInfinity = Infinity(False)  # Negative Infinity
Cinf = ComplexInfinity = Infinity(None)  # Complex Infinity
nan = float("nan")  # NaN
eng_words = None
# with open("words.txt") as word_list:
#     eng_words = set(word.strip().lower() for word in word_list)
ascii = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
         "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
         "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
         "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8",
         "9", "0", "`", "-", "=", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(",
         ")", "[", "]", "\\", ";", "'", ", ", ".", "/", "_", "+", "{", "}", "|", ":", "\"", " < ", ">", "?"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
           "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
           "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
           "T", "U", "V", "W", "X", "Y", "Z"]
chars = ["`", "-", "=", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(",
         ")", "[", "]", "\\", ";", "'", ", ", ".", "/", "_", "+", "{", "}", "|", ":", "\"", " < ", ">", "?"]

"""Operators"""


def d(*x):
    """
    Division
    :param x:
    :return:

    >>> d(10,2)
    5.0
    >>> d(10,2,5)
    1.0
    """
    z = []
    for i in x:
        z.append(i)
    y = z[0]
    z.remove(y)
    for i in z:
        y /= i
    return y


def a(*x):
    """
    addition
    :param x: tuple
    :return:

    >>> a(5,2)
    7
    >>> a(2,-3)
    -1

    Multiple numbers can be inputed as well

    >>> a(2,5,3)
    10
    >>> a(-2,-3,2)
    -3
    """
    z = []
    for i in x:
        z.append(i)
    y = z[0]
    z.remove(y)
    for i in z:
        y += i
    return y


def m(*x):
    z = []
    for i in x:
        z.append(i)
    y = z[0]
    z.remove(y)
    for i in z:
        y *= i
    return y


def s(*x):
    z = []
    for i in x:
        z.append(i)
    y = z[0]
    z.remove(y)
    for i in z:
        y -= i
    return y


"""Functions and Classes"""


class TimeoutException(Exception):
    """docstring for TimeoutException"""
    pass


class IDEError(Exception):
    pass


class Failure(Exception):
    pass


class InterpretationError(Failure):
    pass


class TimeError(Exception):
    pass


class DateError(Exception):
    pass


def dectofr(x, error = 0.0000001):
    """
    Converts decimals to fractions
    :param x: decimal to convert
    :param error: just error
    :return: Fraction

    >>> dectofr(2.5)
    5/2
    >>> dectofr(0.25)
    1/4

    Repeating decimals must have many digits

    >>> dectofr(0.333333333333333333333)
    1/3

    Does work for int

    >>> dectofr(5)
    5
    """
    n = int(floor(x))
    x -= n
    if x < error:
        # return (n, 1)
        return Fraction(n, 1)
    elif 1 - error < x:
        # return (n+1, 1)
        return Fraction(n + 1, 1)

    # The lower fraction is 0/1
    lower_n = 0
    lower_d = 1
    # The upper fraction is 1/1
    upper_n = 1
    upper_d = 1
    while True:
        # The middle fraction is (lower_n + upper_n) / (lower_d + upper_d)
        middle_n = lower_n + upper_n
        middle_d = lower_d + upper_d
        # If x + error < middle
        if middle_d * (x + error) < middle_n:
            # middle is our new upper
            upper_n = middle_n
            upper_d = middle_d
        # Else If middle < x - error
        elif middle_n < (x - error) * middle_d:
            # middle is our new lower
            lower_n = middle_n
            lower_d = middle_d
        # Else middle is our best fraction
        else:
            # return (n * middle_d + middle_n, middle_d)
            # return "{0}/{1}".format(n*middle_d+middle_n,middle_d)
            return Fraction(n * middle_d + middle_n, middle_d)


def frtodec(x):
    """
    Converts Fraction to decimal
    :param x: Fraction to be converted
    :return: Decimal

    >>> frtodec(Fraction(1,2))
    0.5
    >>> frtodec(Fraction(1,3))
    0.3333333333333333
    """
    if not isinstance(x, Fraction):
        raise TypeError("Argument must be a fraction")
    return float(x.numerator) / float(x.denominator)


class _Fraction():
    """
    Fraction Class. Used to create a data type
    """

    def __init__(self, n, d):
        """
        Fraction initilization
        :param n: numerator
        :param d: denomenator
        :return:
        :raises ZeroDivisionError:

        Create a Fraction

        >>> Fraction(5,2)
        5/2
        >>> Fraction(-5,2)
        -5/2
        >>> Fraction(5,-2)
        -5/2
        >>> Fraction(4,10)
        2/5
        """
        self.onum = n
        self.oden = d
        self.numerator = n / gcd(abs(n), abs(d))
        self.denominator = d / gcd(abs(n), abs(d))
        self.whole = 0
        if type(self.denominator) is not complex:
            self.denominator = int(self.denominator)
        if type(self.numerator) is not complex:
            self.numerator = int(self.numerator)
        if (type(self.numerator) is not complex) and (type(self.denominator) is not complex):
            if self.denominator < 0:
                self.denominator = abs(self.denominator)
                self.numerator = -1 * self.numerator
        if self.denominator == 0:
            raise ZeroDivisionError
        self.whole = trunc(frtodec(self))

    def __add__(self, other):
        """
        Adds to values
        :param other:
        :return:

        >>> Fraction(1,4) + Fraction(2,4)
        3/4
        >>> Fraction(1,2) + Fraction(3,4)
        5/4
        >>> Fraction(1,2) + 2
        5/2
        >>> Fraction(1,2) + 2.5
        3
        """
        ax = other
        if type(other) is float:
            ax = dectofr(other)
        return Fraction(self.numerator * ax.denominator + self.denominator * ax.numerator,
                        self.denominator * ax.denominator)

    def __sub__(self, other):
        dx = other
        if type(other) is float:
            dx = dectofr(other)
        return Fraction(self.numerator * dx.denominator - self.denominator * dx.numerator,
                        self.denominator * dx.denominator)

    def __mul__(self, other):
        """
        Multiplication
        :param other:
        :return:

        >>> Fraction(1,2) * Fraction(5,4)
        5/8
        >>> Fraction(1,2) * 4
        2
        >>> Fraction(1,3) * 2.5
        5/6
        """
        mx = other
        if type(other) is float:
            mx = dectofr(other)
        return Fraction(self.numerator * mx.numerator, self.denominator * mx.denominator)

    def __truediv__(self, other):
        dx = other
        if type(other) is float:
            dx = dectofr(other)
        return Fraction(self.numerator * dx.denominator, self.denominator * dx.numerator)

    def __div__(self, other):
        """
        Division
        :param other:
        :return:

        Uses truediv

        >>> Fraction(1,2) / Fraction(3,4)
        2/3
        >>> Fraction(1,2) / 2
        1/4
        >>> Fraction(1,4) / 0.5
        1/2
        """
        return self.__truediv__(other)

    def __pow__(self, x):
        y = pow(self.numerator, x)
        z = pow(self.denominator, x)
        return Fraction(y, z)

    def __str__(self):
        if type(self) is tuple:
            if self[1] < 0:
                return "%s/%s" % (self[0], -1 * self[1])
            else:
                return "%s/%s" % (self[0], self[1])
        elif self.denominator == 1:
            return str(self.numerator)
        else:
            return "%s/%s" % (self.numerator, self.denominator)

    def __cmp__(self, other):
        """
        compare two values
        :param other:
        :return:

        >>> Fraction(1,2) < Fraction(2,3)
        True
        >>> Fraction(2,3) == Fraction(4,6)
        True
        >>> Fraction(1,3) < 1
        True
        >>> Fraction(5,2) > 2.5
        False
        """
        if type(other) is float:
            other = dectofr(other)
        a = Fraction(self.numerator * other.denominator, self.denominator * other.denominator)
        b = Fraction(other.numerator * self.denominator, self.denominator * other.denominator)
        if a.onum > b.onum:
            return 1
        elif a.onum is b.onum:
            return 0
        else:
            return -1

    def __nonzero__(self):
        """
        Non Zero
        :return:

        """
        if self != 0:
            return True
        else:
            return False

    def __repr__(self):
        try:
            return self.__str__()
        except AttributeError:
            return str(None)

    def __abs__(self):
        if self.numerator < 0:
            return Fraction(-(self.numerator), self.denominator)
        else:
            return self

    def digits(self):
        x = frtodec(self)
        return digits(x)

    def is_int(self):
        if self.denominator == 1:
            return True
        else:
            return False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            del self.denominator
            del self.numerator
            del self.oden
            del self.onum
            del self.whole
            del self.__add__
            del self.__cmp__
            del self.__div__
            del self.digits
            del self.is_int
        except:
            pass

    def __trunc__(self):
        return self.whole

    def __float__(self):
        """
        Convert to float
        :return:

        >>> float(Fraction(1,2))
        0.5
        >>> float(Fraction(1,25))
        0.04
        >>> float(Fraction(5,2))
        2.5
        """
        return frtodec(self)

    def __mod__(self, other):
        """
        Modulus
        :param other:
        :return:

        >>> Fraction(1,2) % 2
        1/2
        >>> Fraction(1,2) % Fraction(1,3)
        1/6
        """
        z = trunc(float(self) / float(other))
        a = self - (float(other) * float(z))
        return a

    def __neg__(self):
        return Fraction(-(self.numerator), self.denominator)

    def __pos__(self):
        return Fraction(self.numerator, self.denominator)


Fraction = type("Fraction", (_Fraction, object), {})


class _timeObject:
    def __init__(self, h = None, m = None, s = None, ms = 0):
        import datetime as dt

        self.h = 0
        self.m = 0
        self.s = 0
        if h is None:
            if m is None:
                if s != None:
                    raise TypeError("Invalid Argument")
            else:
                raise TypeError("Invalid Argument")
        else:
            if m is None:
                raise TypeError("Invalid Argument")
            else:
                if s is None:
                    raise TypeError("Invalid Argument")

        if h is None:
            x = dt.datetime.now()
            self.h = x.hour
            if self.h < 10:
                self.h = "0{0}".format(self.h)
            self.m = x.minute
            if self.m < 10:
                self.m = "0{0}".format(self.m)
            self.s = x.second
            if self.s < 10:
                self.s = "0{0}".format(self.s)
            self.ms = (x.microsecond) / 1000.0
            if self.ms.is_integer():
                self.ms = int(self.ms)
        else:
            if h > 23:
                raise TimeError("Hour value is too high")
            if m > 59:
                raise TimeError("Minute value is too high")
            if s > 59:
                raise TimeError("Second value is too high")
            if ms > 999:
                raise TimeError("Millisecond value is too high")
            if h < 0:
                raise TimeError("Hour value is too low")
            if m < 0:
                raise TimeError("Minute value is too low")
            if s < 0:
                raise TimeError("Second value is too low")
            if ms < 0:
                raise TimeError("Second value is too low")
            self.h = h
            self.m = m
            self.s = s
            self.ms = ms
            if self.h < 10:
                self.h = "0{0}".format(self.h)
            if self.m < 10:
                self.m = "0{0}".format(self.m)
            if self.s < 10:
                self.s = "0{0}".format(self.s)

    def __repr__(self):
        return "{0}:{1}:{2}.{3}".format(self.h, self.m, self.s, self.ms)

    def to12(self):
        h = int(self.h)
        if h > 12:
            h = h - 12
            return "0{0}:{1}:{2}.{3} PM".format(h, self.m, self.s, self.ms)
        else:
            return "0{0}:{1}:{2}.{3} AM".format(h, self.m, self.s, self.ms)

    def __cmp__(self, other):
        if not isinstance(other, timeObject):
            raise TypeError("Cannot compare non-time values")
        if self.h > other.h:
            return 1
        elif self.h == other.h:
            if self.m > other.m:
                return 1
            elif self.m == other.m:
                if self.s > other.s:
                    return 1
                elif self.s == other.s:
                    if self.ms > other.ms:
                        return 1
                    elif self.ms == other.ms:
                        return 0
                    else:
                        return -1
                else:
                    return -1
            else:
                return -1
        else:
            return -1

    def __add__(self, other):
        if not isinstance(other, timeObject):
            raise TypeError("cannot add non-timeObject values")
        h = int(self.h) + int(other.h)
        m = int(self.m) + int(other.m)
        s = int(self.s) + int(other.s)
        ms = self.ms + other.ms
        if h > 23:
            h = h - 24
        if m > 59:
            m = m - 60
        if s > 59:
            s = s - 60
        if ms > 999:
            ms = ms - 1000
        return timeObject(h, m, s, ms)

    def __sub__(self, other):
        if not isinstance(other, timeObject):
            raise TypeError("cannot add non-timeObject values")
        h = int(self.h) - int(other.h)
        m = int(self.m) - int(other.m)
        s = int(self.s) - int(other.s)
        ms = int(self.ms) - int(other.ms)
        if h < 0:
            h = h + 24
        if m < 0:
            m = m + 60
        if s < 0:
            s = s + 60
        if ms < 0:
            ms = ms + 1000
        return timeObject(h, m, s, ms)

    @staticmethod
    def now(self):
        import datetime as dt

        x = dt.datetime.now()
        return timeObject(x.hour, x.minute, x.second, x.microsecond / 1000)


timeObject = type("timeObject", (_timeObject, object), {})


class _dateObject:
    def __init__(self, m = None, d = None, y = None):
        if d is None:
            if m is None:
                if y != None:
                    raise TypeError("Invalid Argument")
            else:
                raise TypeError("Invalid Argument")
        else:
            if m is None:
                raise TypeError("Invalid Argument")
            else:
                if y is None:
                    raise TypeError("Invalid Argument")

        if d is None:
            import datetime as dt

            x = dt.datetime.now()
            self.d = x.day
            self.m = x.month
            self.y = x.year
        else:
            if type(m) is not int:
                raise TypeError("Please enter number values")
            if type(d) is not int:
                raise TypeError("Please enter number values")
            if type(y) is not int:
                raise TypeError("Please enter number values")
            if m > 12:
                raise ValueError("Invalid Month value")
            elif m < 1:
                raise ValueError("Invalid Month value")
            if m == 1:
                if d > 31:
                    raise ValueError("Invalid Day value")
                elif d < 1:
                    raise ValueError("Invalid Day value")
            if m == 2:
                leap = False
                if y % 4 == 0:
                    leap = True
                if y % 100 == 0:
                    leap = False
                if y % 400 == 0:
                    leap = True
                if leap:
                    if d > 29:
                        raise ValueError("Invalid Day value")
                    elif d < 0:
                        raise ValueError("Invalid Day value")
                else:
                    if d > 28:
                        raise ValueError("Invalid Day value")
                    elif d < 0:
                        raise ValueError("Invalid Day value")
            if m == 3:
                if d > 31:
                    raise ValueError("Invalid Day value")
                elif d < 1:
                    raise ValueError("Invalid Day value")
            if m == 4:
                if d > 30:
                    raise ValueError("Invalid Day value")
                elif d < 1:
                    raise ValueError("Invalid Day value")
            if m == 5:
                if d > 31:
                    raise ValueError("Invalid Day value")
                elif d < 1:
                    raise ValueError("Invalid Day value")
            if m == 6:
                if d > 30:
                    raise ValueError("Invalid Day value")
                elif d < 1:
                    raise ValueError("Invalid Day value")
            if m == 7:
                if d > 31:
                    raise ValueError("Invalid Day value")
                elif d < 1:
                    raise ValueError("Invalid Day value")
            if m == 8:
                if d > 31:
                    raise ValueError("Invalid Day value")
                elif d < 1:
                    raise ValueError("Invalid Day value")
            if m == 9:
                if d > 30:
                    raise ValueError("Invalid Day value")
                elif d < 1:
                    raise ValueError("Invalid Day value")
            if m == 10:
                if d > 31:
                    raise ValueError("Invalid Day value")
                elif d < 1:
                    raise ValueError("Invalid Day value")
            if m == 11:
                if d > 30:
                    raise ValueError("Invalid Day value")
                elif d < 1:
                    raise ValueError("Invalid Day value")
            if m == 12:
                if d > 31:
                    raise ValueError("Invalid Day value")
                elif d < 1:
                    raise ValueError("Invalid Day value")

            self.d = d
            self.m = m
            self.y = y
            if self.d < 10:
                self.sd = "0{0}".format(self.d)
            if self.m < 10:
                self.sm = "0{0}".format(self.m)
            if self.y < 1000:
                if self.y < 100:
                    if self.y < 10:
                        if self.y < 0:
                            raise DateError("Please don't use negative years")
                        self.sy = "000{0}".format(self.s)
                    else:
                        self.sy = "00{0}".format(self.s)
                else:
                    self.sy = "0{0}".format(self.s)

    def __repr__(self):
        return "{2}-{0}-{1}".format(self.m, self.d, self.y)

    def __cmp__(self, other):
        if not isinstance(other, dateObject):
            raise DateError("Results in non-Date value")
        if self.y > other.y:
            return 1
        elif self.y == other.y:
            if self.m > other.m:
                return 1
            elif self.m == other.m:
                if self.d > other.d:
                    return 1
                elif self.d == other.d:
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1

    def __add__(self, other):
        if not isinstance(other, dateObject):
            raise TypeError("Cannot add non-date value")
        y = self.y + other.y
        m = self.m + other.m
        d = self.d + other.d
        return dateObject(m, d, y)

    @staticmethod
    def now(self):
        import datetime as dt

        x = dt.datetime.now()
        return dateObject(x.month, x.day, x.year)


dateObject = type("dateObject", (_dateObject, object), {})


class _dateTime:
    def __init__(self, y = None, m = None, d = None, h = None, min = None, s = None, ms = None):
        self.date = dateObject(m, d, y)
        self.time = timeObject(h, min, s, ms)
        self.y = self.date.y
        self.m = self.date.m
        self.d = self.date.d
        self.h = self.time.h
        self.min = self.time.m
        self.s = self.time.s
        self.ms = self.time.ms


datetime = type("datetime", (_dateTime, object), {})


def abs(x):
    """
    Returns the absolute value of a float
    :param x: float, int, complex
    :return: absolute value of x

    >>> abs(5)
    5
    >>> abs(-5)
    5
    >>> abs(-5.2)
    5.2
    >>> abs(5.2)
    5.2

    Complex is different

    >>> abs(1j)
    1.0
    >>> abs(-532j)
    532.0
    """
    if type(x) is not float:
        if type(x) is not int:
            if type(x) is not complex:
                if type(x) is not Fraction:
                    raise TypeError("A float is required")
    if type(x) is complex:
        return sqrt(pow(x.real, 2) + pow(x.imag, 2))
    if x > 0:
        return x
    else:
        return -x


def ceil(x):
    """
    Returns the ceiling of a number
    :param x: float
    :return: integer

    >>> ceil(5.3)
    6
    >>> ceil(6)
    6
    >>> ceil(-5.3)
    -5
    """
    y = 0
    try:
        if type(x) == str:
            forstring = float(x)
            y = int(forstring)
        else:
            y = int(x)
    except ValueError:
        raise TypeError("A float is required")
    if y == float(x):
        return x
    if float(x) > y:
        return y + 1
    else:
        return y


def fac(x):
    """
    Finds x factorial
    :param x: integer
    :return: x factorial

    >>> fac(0)
    1
    >>> fac(5)
    120
    """
    if type(x) is not int:
        raise TypeError("A integer is required")
    if x == 0:
        return 1
    elif x < 0:
        raise TypeError("Not for negative values")
    else:
        return x * fac(x - 1)


def floor(x):
    """
    floors float
    :param x: float
    :return: floor of x

    >>> floor(5.3)
    5
    >>> floor(-5.3)
    -6
    >>> floor(0)
    0
    >>> floor("hi")
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: 'hi'

    """
    y = int(x)
    if y < 0:
        return y - 1
    else:
        return y


def fsum(n):
    """
    Returns sum of numbers inputed
    :param n: list
    :return: integer or float

    >>> fsum([1,2,3])
    6
    >>> fsum([-1,2,-3])
    -2
    >>> fsum(["hi",2,3])
    Traceback (most recent call last):
    TypeError: A float is required
    """
    x = 0
    for i in n:
        if type(i) is not int and type(i) is not float and type(i) is not Fraction:
            raise TypeError("A float is required")
        x += i
    return x


def isinf(x):
    """
    Checks if x is infinity
    :param x: suspected infinity
    :return: boolean

    >>> isinf(inf)
    True
    >>> isinf(Ninf)
    True
    >>> isinf(float("inf"))
    True
    >>> isinf(float("-inf"))
    True
    >>> isinf(5)
    False
    """
    if x == inf:
        return True
    elif x == Ninf:
        return True
    elif x == float("inf"):
        return True
    elif x == float("-inf"):
        return True
    else:
        return False


def isnan(x):
    """
    Checks if X is NaN
    :param x: suspected NaN
    :return: boolean

    >>> isnan(float("NaN"))
    True
    >>> isnan(5)
    False
    """
    return x != x


def exp(x):
    """
    returns e^X
    :param x: exponent
    :return: float
    >>> exp(1)
    2.718281828459045
    """
    return e ** x


def pow(x, y):
    """
    X to the Y power
    :param x:
    :param y:
    :return:

    >>> pow(2,3)
    8
    >>> pow(5,-1)
    0.2
    >>> pow(25,0.5)
    5.0
    """
    return x ** y


def trunc(x):
    """
    Return X truncated
    :param x: any float or int
    :return: X truncated
    >>> trunc(5.2)
    5
    >>> trunc(-5.2)
    -5
    """
    y = 0
    if x > 0:
        y = floor(x)
    else:
        y = ceil(x)
    return y


def fmod(x, y):
    """
    Returns modulus of x and y
    :param x:
    :param y:
    :return:
    >>> fmod(5,2)
    1.0
    >>> fmod(20,5)
    0.0
    >>> fmod(5,2.5)
    0.0
    >>> fmod(-10,2)
    0.0
    """
    z = trunc(float(x) / float(y))
    a = x - (float(y) * float(z))
    return a


def root(x, y):
    """
    Returns y Root of X
    :param x:
    :param y:
    :return:
    >>> root(8,3)
    2.0
    >>> root(4,-2)
    0.5
    >>> root(0,2)
    0.0
    >>> root(2,0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    return x ** d(1, y)


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


def frexp(x):
    """
    power of 2 times number to equal X
    :param x:
    :return:
    >>> frexp(0)
    (0.0, 0)
    >>> frexp(8)
    (0.5, 4)
    """
    p = pow(2, 0)
    i = 0
    m = 0.0
    correct = False
    if x == 0:
        correct = True
    while not correct:
        p = pow(2, i)
        m = d(x, p)
        if abs(m) >= 0.5 and abs(m) < 1:
            correct = True
        else:
            i = i + 1
        if i == 10:
            correct == True
    return (m, i)


def ldexp(x, i):
    """
    opposite of frexp
    :param x:
    :param i:
    :return:

    >>> ldexp(0.5,4)
    8.0

    """
    return float(x * (2 ** i))


def fround(x):
    """
    Rounds X to nearest integer
    :param x:
    :return:

    >>> fround(5)
    5
    >>> fround(2.5000000001)
    3
    >>> fround(-2.56)
    -3

    If X is exactly mid way- round to even number

    >>> fround(5.5)
    6
    >>> fround(4.5)
    4
    """
    try:
        intx = int(floor(x))
        decx = x - intx
        if decx < 0.5:
            return intx
        elif decx > 0.5:
            return intx + 1
        elif decx == 0.5:
            if evenQ(intx + 1):
                return intx + 1
            else:
                return intx
    except ValueError:
        raise TypeError("A float or integer is required")


def modf(x):
    """
    Splits X into integer and decimal peices
    :param x:
    :return:

    >>> modf(5.2)
    (0.2, 5)
    >>> modf(53.34)
    (0.34, 53)

    Works with integers

    >>> modf(5)
    (0.0, 5)

    even works with long floats

    >>> modf(5.349293430359)
    (0.349293430359, 5)
    """
    a1 = str(x).find(".")
    a2 = len(str(x)[a1 + 1:])
    intx = floor(x)
    decx = round(x - int(intx), a2 + 1)
    return decx, intx


def copysign(x, y):
    """
    Copy"s the sign of y onto x
    :param x:
    :param y:
    :return:

    >>> copysign(5,3)
    5
    >>> copysign(5,-3)
    -5
    >>> copysign(-5,3)
    5
    >>> copysign(-5,-3)
    -5
    """
    if y < 0:
        return -1 * abs(x)
    elif y >= 0:
        return abs(x)


def expm1(x):
    if abs(x) < 1e-5:
        return x + 0.5 * x * x
    else:
        return expm1(x) - 1.0


def log(x, base = e):
    """Returns log of x"""
    i = pow(base, 0)
    o = 0
    _ = 0
    while True:
        if i > x:
            break

        _ = _ + 1000000
        o = _ - 1000000
        i = pow(base, _)

    while True:
        return 5


def factors(x):
    """Returns factors of x"""
    f = []
    for i in range(1, x):
        if x % i == 0:
            f.append(i)
    f.append(x)
    return f


def sign(x):
    """Returns sign of X. Returns either -1, 0, or 1"""
    if x < 0:
        return -1
    elif x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        raise TypeError("A float is required")


def intQ(x):
    """Checks if X is a integer"""
    if type(x) == type(1):
        return True
    else:
        return False


def min(x):
    """finds the minimum of the values given"""
    smallest = inf
    for i in x:
        if i > inf:
            raise TypeError("A float is required")
        if i < smallest:
            smallest = i
    return smallest


def max(x):
    """finds the maximum of the values given"""
    largest = Ninf
    for i in x:
        if i > inf:
            raise TypeError("A float is required")
        if i > largest:
            largest = i
    return largest


def clip(x):
    """
    Clips x in between -1 and 1
    :param x:
    :return:

    >>> clip(5)
    1
    >>> clip(-2)
    -1
    >>> clip(0.4)
    0.4
    """
    if x > 1.0:
        return 1
    elif x < -1.0:
        return -1
    else:
        return x


def reorder(x, gtol = False):
    """reorders the list from least to greatest"""
    o = list(x)
    o.sort()
    if gtol:
        o.reverse()
    return o


def median(x):
    """finds the median"""
    r = reorder(x)
    half = len(r) / 2.0
    if not half.is_integer():
        return r[int(half)]
    elif half.is_integer():
        a = r[int(half)]
        b = r[int(half) - 1]
        return mean([a, b])


def frange(x):
    """Gives the range of given list"""
    high = max(x)
    low = min(x)
    r = high - low
    return r


def mean(x):
    """Returns mean"""
    total = 0
    for i in x:
        if i > inf:
            raise TypeError("A float is required")
        total += i
        a = float(total) / len(x)
    return a


def mode(x):
    """Returns mode"""
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


def rescale(x, small, large):
    """Rescales X"""
    pass


# TODO-everyone fix sin
def sin(a):
    """Returns sin(a)"""
    return (e ** (a * 1j)).imag


# TODO-everyone fix cos
def cos(a):
    """
    Return the Cosine of x
    :param a:
    :return:
    """
    return (e ** (a * 1j)).real


def tan(a):
    """Returns tan(a)"""
    answer = (sin(a)) / cos(a)
    return answer


def cot(a):
    """Returns cotangent(a)"""
    answer = (cos(a)) / (sin(a))
    return answer


def sec(a):
    """Returns secant(a)"""
    answer = 1.00 / cos(a)
    return answer


def csc(a):
    """Returns the cosecant of a"""
    return 1.00 / sin(a)


def asin(a):
    """Returns the arcsine of a"""
    pass
    if a > 1.00 or a < -1.00:
        raise ValueError("math domain error")
    return rad(a)


def deg(x):
    """
    Converts X to degrees
    :param x:
    :return:

    >>> deg(5)
    286.4788975654116
    >>> deg(pi)
    180.0
    >>> deg(pi/2)
    90.0
    """
    return x * (180.00 / pi)


def rad(x):
    return x * (pi / 180.00)


def square(x):
    """checks if x is a square number"""
    sq = sqrt(x)
    if type(sq) == type(5):
        return True
    else:
        return False


def cube(x):
    """
    Checks if X is a cube number
    :param x:
    :return:

    >>> cube(2)
    False
    >>> cube(9)
    False
    >>> cube(8)
    True
    """
    c = root(x, 3)
    if float.is_integer(c):
        return True
    else:
        return False


def perfect(x):
    """Checks if x is a perfect number"""
    fac = factors(x)
    y = 0
    for i in fac:
        y += i
        y -= x
    if y == x:
        return True
    else:
        return False


def gcd(x, y):
    if type(x) is not int:
        if type(x) is not float:
            if type(x) is not Fraction:
                raise TypeError("{0} is not an integer, float, or fraction".format(x))
    if type(y) is not int:
        if type(y) is not float:
            if type(x) is not Fraction:
                raise TypeError("{0} is not an integer or float".format(y))
    x = abs(x)
    y = abs(y)
    while x != 0 or y != 0:
        if x < y:
            f = x
            x = y
            y = f
        if x == 0:
            return int(y)
        elif y == 0:
            return int(x)
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
    if answer.is_integer() == True:
        return int(answer)
    else:
        return answer


def divisible(x, y):
    try:
        if float(x) % y == 0:
            return True
        else:
            return False
    except TypeError:
        raise TypeError("A float is required")


def coprime(x, y):
    """
    Tests if x and y are coprime
    :param x:
    :param y:
    :return: boolean

    >>> coprime(10,2)
    False
    >>> coprime(16,15)
    True
    >>> coprime(-4, -2)
    False
    >>> coprime(-5, -2)
    True
    """
    if gcd(x, y) == 1:
        return True
    else:
        return False


def evenQ(x):
    if type(x) != int:
        raise ValueError("A integer is required")
    if x % 2 == 0:
        return True
    else:
        return False


def oddQ(x):
    if x != int:
        raise ValueError("A integer is required")
    if x % 2 == 1:
        return True
    else:
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


def fib(n):
    return int((pow(gr, n) - pow(1 - gr, n)) / sqrt(5))


def prime(n):
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
    while n2 != n:
        test = primeQ(f)
        if test == True:
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
        if test == True:
            n2 += 1
        if f >= n:
            break
        f += 1
    return n2


def nextprime(n):
    f = n + 1
    test = False
    if n <= 0:
        raise ValueError("n must be greater than 0")
    while not test:
        test = primeQ(f)
        if test:
            break
        f += 1
    return f


def sample(pop, k, seed = None):
    from random import sample as s
    from random import seed as se

    if seed != None:
        se(seed)
    return s(pop, k)


def Rdiagonal(s1, s2):
    return sqrt(pow(s1, 2) + pow(s2, 2))


def Sdiagonal(s):
    return sqrt(2) * s


def Tsemiper(a, b, c):
    return (a + b + c) / 2.0


def Tarea(a, b, c):
    p = Tsemiper(a, b, c)
    return sqrt(p * (p - a) * (p - b) * (p - c))


def hyp(a, b):
    return sqrt(pow(a, 2) + pow(b, 2))


def Tgamma(a):
    pass


def TRarea(a, b, h):
    return ((a + b) / 2.00) * h


def Harea(a):
    return ((3 * sqrt(3)) / 2.0) * pow(a, 2)


def Carea(r):
    """
    Return the area of a circle with given radius
    :param r: radius
    :return:

    >>> Carea(1)
    3.141592653589793
    >>> Carea(2)
    12.566370614359172
    """
    return pi * pow(r, 2)


def Cir(r):
    """
    Returns Circumference of circle with given radius
    :param r:
    :return:

    >>> Cir(2)
    12.566370614359172
    >>> Cir(10)
    62.83185307179586
    """
    return 2 * pi * r


def gamma(n):
    return fac(n - 1)


def unitConvert(n, unit, target):
    t = str.lower(target)
    u = str.lower(unit)
    if u == "mi":
        if t == "km":
            return n * 1.60934
        if t == "m":
            return n * 1609.34
        if t == "in":
            return n * 63360
        if t == "ft":
            return n * 5280
        if t == "cm":
            return n * 160934
        if t == "yd":
            return n * 1760
        if t == "nm":
            return n * 0.868976


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
        if f(x) == True:
            o.append(x)
    return o


def fac2(x):
    """Returns double factorial"""
    if x == -1 or x == 0:
        return 1
    return x * fac2(x - 2)


def per(n, p):
    """p percent of n"""
    x = p / 100.0
    return x * n


def allTrue(l, f):
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
        if f(x) == False:
            return False
    return True


def anyTrue(l, f):
    """
    Tests if ANY object in l is true with the function f
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
        if f(x) == True:
            return True
    return False


def noneTrue(l, f):
    try:
        if type(f(2)) != bool:
            raise ValueError("Function must return Boolean value")
    except TypeError:
        raise TypeError("f must be a function")
    for x in l:
        if f(x) == True:
            return False
    return True


def nearest(l, x):
    n = None
    nl = []
    v = inf
    for i in l:
        if abs(i - x) < v:
            n = i
            v = abs(i - x)
            del nl[:]
            nl.append(i)
        if abs(i - x) == v:
            nl.append(i)
            nl = filter(lambda a: a != 2, nl)
            nl.remove(nl[0])
    if len(nl) > 1:
        return nl
    else:
        return n


def sd(l):
    x = mean(list(l))
    sl = []
    for y in l:
        z = y - x
        z2 = pow(z, 2)
        sl.append(z2)
        m2 = mean(sl)
    return sqrt(m2)


def ssd(l):
    x = mean(list(l))
    sl = []
    for y in l:
        z = y - x
        z2 = pow(z, 2)
        sl.append(z2)
        a = fsum(sl)
    return sqrt(float(a) / (len(sl) - 1))


def Sum(f, i = None, maximum = None, step = 1, l = None):
    try:
        if type(f(2)) != float:
            if type(f(2)) != int:
                raise ValueError("Function must return float or integer value")
    except TypeError:
        raise TypeError("f must be a function")

    if i != None:
        if maximum != None:
            if l != None:
                raise TypeError("Invalid Argument")
            else:
                raise TypeError("Invalid Argument")
    if i == None:
        if maximum == None:
            if l == None:
                raise TypeError("Invalid Argument")
            else:
                raise TypeError("Invalid Argument")

    if l == None:
        x = 0
        while i <= maximum:
            x += f(i)
            i += step
        return x
    elif i != None:
        x = 0
        for y in l:
            x += f(y)
        return x


def Product(f, i = None, maximum = None, step = 1, l = None):
    try:
        if type(f(2)) != float:
            if type(f(2)) != int:
                raise ValueError("Function must return float or integer value")
    except TypeError:
        raise TypeError("f must be a function")

    if i != None:
        if maximum != None:
            if l != None:
                raise TypeError("Invalid Argument")
            else:
                raise TypeError("Invalid Argument")
    if i == None:
        if maximum == None:
            if l == None:
                raise TypeError("Invalid Argument")
            else:
                raise TypeError("Invalid Argument")

    if l == None:
        x = 0
        while i <= maximum:
            x *= f(i)
            i += step
        return x
    elif i != None:
        x = 0
        for y in l:
            x *= f(y)
        return x


def var(l):
    x = mean(l)
    sl = []
    for i in l:
        z = i - x
        z2 = pow(z, 2)
        sl.append(z2)
    return mean(sl)


def svar(l):
    x = mean(l)
    sl = []
    for i in l:
        z = i - x
        z2 = pow(z, 2)
        sl.append(z2)
    m2 = fsum(sl)
    return m2 / (len(sl) - 1)


def md(l):
    x = mean(l)
    sl = []
    for i in l:
        z = abs(i - x)
        sl.append(z)
    return mean(sl)


def comb(n, r):
    """
    returns Combination. C(n,r)
    :param n:
    :param r:
    :return:

    >>> comb(15,4)
    1365
    >>> comb(5, 0)
    1
    >>> comb(0, 5)
    0
    """
    if r > n:
        return 0
    return int(float(fac(n)) / (fac(r) * fac(n - r)))


def perm(n, k):
    if k > n:
        return 0
    return float(fac(n)) / fac(n - k)


def exppro(p, n, sd = None):
    from random import randint
    from random import seed

    p = p * 100
    if sd != None:
        seed(sd)
    suc = 0
    fail = 0
    for i in range(0, n):
        x = randint(0, 100)
        if x <= p:
            suc += 1
        else:
            fail += 1
    del randint, seed
    return suc, fail


def inttobin(x):
    """
    Returns integer to binary
    :param x:
    :return:

    >>> inttobin(0)
    '0'
    >>> inttobin(1)
    '1'
    >>> inttobin(5)
    '101'
    >>> inttobin(9001)
    '10001100101001'
    """
    if not isinstance(x, int):
        raise Exception("Invalid value")
    return "{0:b}".format(x)


def isReal(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


def isPro(x, y):
    """Returns whether the inputed points are proportional"""
    if type(x) != list:
        raise TypeError("x must be a list")
    if type(y) != list:
        raise TypeError("y must be a list")
    if len(x) < 2:
        raise ValueError("length of lists must be greater than 1")
    if len(x) != len(y):
        raise TypeError("lenght of lists must be greater than one")

    s = 0
    f = False

    for i in range(len(x)):
        n = x[i]
        n2 = y[i]
        if n == 0:
            if n2 == 0:
                continue
            else:
                return False
        else:
            if n2 == 0:
                return False

        cs = n2 / n
        if not f:
            s = cs
            f = True

        if cs != s:
            return False
    return True


def slope(x1, y1, x2, y2):
    """Calculates slope of two points"""
    dx = x1 - x2
    dy = y1 - y2
    if dx == 0:
        return inf
    return Fraction(dy, dx)


def NFactors(x):
    y = 0
    nl = factors(x)
    for i in nl:
        y += 1
    return y


def ln(x):
    if x <= 0:
        raise ValueError("math domain error")
    y = 0
    for i in range(1, 999999999):
        z = (1.0 / i) * (float(x - 1) / x) ** i
        y += z
    return y


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
        if f(i) == False:
            p.append(i)
    return p


def delCases(l, f):
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
        if f(i) == False:
            p.append(i)
    return p


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


def applyList(l, f):
    """
    Applies what ever f returns onto list
    :param l: list
    :param f: function
    :return:

    >>> applyList([1,2,3,4], fac)
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


def interpreter(t, boolreturn = False):
    y = False
    if type(t) is not type(type):
        if type(t) is not type(Fraction):
            raise TypeError(str(t) + " is not a data type")
        elif type(t) is type(Fraction):
            y = True

    def inter(x):
        if y:
            if isinstance(x, t):
                if boolreturn:
                    return True
                return x
            else:
                if boolreturn:
                    return False
                raise InterpretationError(str(type(x)) + " " + str(x) + " is not a " + str(t))
        if type(x) is t:
            if boolreturn:
                return True
            return x
        else:
            if boolreturn:
                return False
            raise InterpretationError(str(type(x)) + " " + str(x) + " is not of " + str(t))

    return inter


def whitespace(s):
    if type(s) != str:
        raise TypeError("s must be a string")
    return " ".join(s.split())


def reverse(l):
    if type(l) != list:
        raise TypeError("l must be a list")
    return l.reverse()


def word(word):
    from urllib import urlencode
    from urllib2 import urlopen

    if type(word) is not str:
        raise TypeError("s must be a string")
    fixed = whitespace(word)
    if fixed.lower() in eng_words:
        return True

    def wolfram_cloud_call(**args):
        arguments = dict([(key, arg) for key, arg in args.iteritems()])
        try:
            result = urlopen("http://www.wolframcloud.com/objects/bdf9bbc4-6b59-4821-9053-9d453f7a9b39",
                             urlencode(arguments))
        except:
            raise Failure("Internet connection required for full dictionary, only providing small dictionary currently")
        return result.read()

    textresult = wolfram_cloud_call(x = fixed)
    if textresult == "{}":
        return False
    else:
        return True


def wordcount(s):
    if type(s) is not str:
        raise TypeError("s must be a string")
    fixed = whitespace(s)
    all_words = fixed.split()
    return len(all_words)


def pGenerator(length, words = False):
    if type(length) is not int:
        raise TypeError("length must be an integer")
    if not words:
        import random as _r
        import os as _os

        _r.seed(_os.urandom(1024))
        return "".join(_r.choice(ascii) for i in range(length))
    elif words:
        import random as _r
        import os as _os

        _r.seed(_os.urandom(1024))
        return whitespace("".join("{0} ".format(_r.choice(list(eng_words))) for i in range(length)))
    else:
        raise TypeError("words must be a bool value")


def normalDist(x = None, u = 0, o = 1):
    def normal(y):
        return (exp((-1 / 2.0) * pow((float(y - u) / o), 2))) / (o * sqrt(2 * pi))

    if x is None:
        return normal
    else:
        return (exp((-1 / 2.0) * pow((float(x - u) / o), 2))) / (o * sqrt(2 * pi))


def digits(x):
    if type(x) is str:
        print type(x)
        return x + " is not a number"
    if isinstance(x, Fraction):
        return x.digits()
    if int(x) == x:
        return len(str(x))
    else:
        return len(str(x)) - 1


def now():
    return 1


def day(m, d, y):
    """
    Returns day of the week of the specific date
    :param m: month
    :param d: day
    :param y: year
    :return:

    >>> day(3,15,16)
    'Tuesday'
    >>> day(2,29,16)
    'Wednesday'
    >>> day(2,29,15)
    Traceback (most recent call last):
    ValueError: Invalid Day value
    """
    if type(m) is not int:
        raise TypeError("Please enter number values")
    if type(d) is not int:
        raise TypeError("Please enter number values")
    if type(y) is not int:
        raise TypeError("Please enter number values")
    if m > 12:
        raise ValueError("Invalid Month value")
    elif m < 1:
        raise ValueError("Invalid Month value")
    if m == 1:
        if d > 31:
            raise ValueError("Invalid Day value")
        elif d < 1:
            raise ValueError("Invalid Day value")
        m = 11
        y -= 1
    if m == 2:
        leap = False
        if y % 4 == 0:
            leap = True
        if y % 100 == 0:
            leap = False
        if y % 400 == 0:
            leap = True
        if leap:
            if d > 29:
                raise ValueError("Invalid Day value")
            elif d < 0:
                raise ValueError("Invalid Day value")
        else:
            if d > 28:
                raise ValueError("Invalid Day value")
            elif d < 0:
                raise ValueError("Invalid Day value")
        m = 12
        y -= 1
    if m == 3:
        if d > 31:
            raise ValueError("Invalid Day value")
        elif d < 1:
            raise ValueError("Invalid Day value")
        m = 1
    if m == 4:
        if d > 30:
            raise ValueError("Invalid Day value")
        elif d < 1:
            raise ValueError("Invalid Day value")
        m = 2
    if m == 5:
        if d > 31:
            raise ValueError("Invalid Day value")
        elif d < 1:
            raise ValueError("Invalid Day value")
        m = 3
    if m == 6:
        if d > 30:
            raise ValueError("Invalid Day value")
        elif d < 1:
            raise ValueError("Invalid Day value")
        m = 4
    if m == 7:
        if d > 31:
            raise ValueError("Invalid Day value")
        elif d < 1:
            raise ValueError("Invalid Day value")
        m = 5
    if m == 8:
        if d > 31:
            raise ValueError("Invalid Day value")
        elif d < 1:
            raise ValueError("Invalid Day value")
        m = 6
    if m == 9:
        if d > 30:
            raise ValueError("Invalid Day value")
        elif d < 1:
            raise ValueError("Invalid Day value")
        m = 7
    if m == 10:
        if d > 31:
            raise ValueError("Invalid Day value")
        elif d < 1:
            raise ValueError("Invalid Day value")
        m = 8
    if m == 11:
        if d > 30:
            raise ValueError("Invalid Day value")
        elif d < 1:
            raise ValueError("Invalid Day value")
        m = 9
    if m == 12:
        if d > 31:
            raise ValueError("Invalid Day value")
        elif d < 1:
            raise ValueError("Invalid Day value")
        m = 10

    y1 = y % 100
    c = int(str(y)[:2])
    x = (d + floor(2.6 * m - 0.2) + y1 + floor(y1 / 4.0) + floor(c / 4.0) - 2 * c) % 7
    if x == 0:
        return "Sunday"
    elif x == 1:
        return "Monday"
    elif x == 2:
        return "Tuesday"
    elif x == 3:
        return "Wednesday"
    elif x == 4:
        return "Thursday"
    elif x == 5:
        return "Friday"
    elif x == 6:
        return "Saturday"
    else:
        raise Failure()


def formulaLookup(x):
    """Lookup formulas"""
    from urllib import urlencode
    from urllib2 import urlopen

    def wolfram_cloud_call(**args):
        arguments = dict([(key, arg) for key, arg in args.iteritems()])
        try:
            result = urlopen("http://www.wolframcloud.com/objects/5c991864-3fbd-4b30-8200-d1a398aee0e2",
                             urlencode(arguments))
        except:
            raise Failure("Cannot connect to servers")
        return result.read()

    textresult = wolfram_cloud_call(x = x)
    return textresult


__VERSION__ = "0.1.0"
__name__ = "AMath"

"""Raise an error when run alone"""
if __name__ == "__main__":
    raise Exception("Please do not run alone")
