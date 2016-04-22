from amath.Errors import DateError


# noinspection PyUnresolvedReferences
class _DateObject:
    def __init__(self, m=None, d=None, y=None):
        if d is None:
            if m is None:
                if y is not None:
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
                        self.sy = "000{0}".format(self.y)
                    else:
                        self.sy = "00{0}".format(self.y)
                else:
                    self.sy = "0{0}".format(self.y)

    def __repr__(self):
        return "{2}-{0}-{1}".format(self.m, self.d, self.y)

    def __cmp__(self, other):
        if not isinstance(other, DateObject):
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
        if not isinstance(other, DateObject):
            raise TypeError("Cannot add non-date value")
        y = self.y + other.y
        m = self.m + other.m
        d = self.d + other.d
        return DateObject(m, d, y)

    @staticmethod
    def now():
        import datetime as dt
        x = dt.datetime.now()
        return DateObject(x.month, x.day, x.year)


DateObject = type("DateObject", (_DateObject, object), {})
