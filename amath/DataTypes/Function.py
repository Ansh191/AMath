from collections import OrderedDict


class _Function(object):
    __slots__ = ('run', '__call__', 'vars', 'function', 'v')

    def __init__(self, variables, function):
        # type: (object, str) -> None
        self.vars = {}
        self.function = function
        # print(variables)
        if isinstance(variables, str):
            self.vars[variables] = "Value"
        elif isinstance(variables, list):
            for i in variables:
                if not isinstance(i, str):
                    raise TypeError("Invalid variable")
                else:
                    self.vars[i] = "Value"
        elif isinstance(variables, dict):
            for var in variables:
                if not isinstance(var, str):
                    raise TypeError("Invalid variable")
                if not (variables[var] in ["Value", "Number", "Imaginary", "Real", "Integer", "Whole", "Natural"]):
                    raise TypeError("Invalid variable type")
            self.vars = variables
        elif isinstance(variables, OrderedDict):
            for var in variables:
                if not isinstance(var, str):
                    raise TypeError("Invalid variable")
                if not (variables[var] in ["Value", "Number", "Imaginary", "Real", "Integer", "Whole", "Natural"]):
                    raise TypeError("Invalid variable type")
            self.vars = variables
        else:
            raise TypeError("Invalid variable declaration")
        # print(self.vars)
        for var in self.vars:
            if var not in function:
                self.vars.pop(var)
                continue

            function.replace(" ", "")

            times = function.count(var)
            if times == 0:
                self.vars.pop(var)
                continue
            i = 0
            while i < times:
                index = function.find(var, function.find(var) + i)
                before = function[index - 1]
                con = False
                if index - 1 == -1:
                    con = True
                try:
                    int(before)
                except ValueError:
                    con = True

                if not con:
                    function = function[:index] + "*" + function[index:]
                i += 1

            times = function.count('(')
            if times == 0:
                continue
            i = 0
            while i < times:
                index = function.find('(', function.find('(') + i)
                before = function[index - 1]
                con = False
                if index - 1 == -1:
                    con = True
                try:
                    int(before)
                except ValueError:
                    con = True

                if not con:
                    function = function[:index] + "*" + function[index:]
                i += 1

        vl = []
        for var in self.vars:
            vl.append(var)
        v = ", ".join(vl)
        self.v = v
        # print(self.v)
        from amath import __all__
        c = (str(__all__)[1:-1]).replace("'", "")
        string = "def run(self, " + v + """):
                    from amath import """ + c + """
                    from collections import OrderedDict as OD
                    self.check(""" + v + """)
                    return """ + function
        string2 = "def __call__(self, " + v + """):
                    return self.run(""" + v + ")"
        exec(string)
        exec(string2)
        exec("setattr(Function, run.__name__, run)")
        exec("setattr(Function, __call__.__name__, __call__)")

    def check(self, *args):
        from amath.testing.types import isReal, isComplex, isNatural, isWhole, intQ, isNumber, isValue
        if len(args) != len(self.vars):
            raise TypeError("check takes exactly {0} arguments ({1} given)".format(len(self.vars), len(args)))
        i = 0
        for var in self.vars:
            tp = self.vars[var]
            value = args[i]
            if tp == "Value":
                if not isValue(value):
                    raise TypeError("{0} must be a value".format(var))
            elif tp == "Number":
                if not isNumber(value):
                    raise TypeError("{0} must be a number".format(var))
            elif tp == "Imaginary":
                if not isComplex(value):
                    raise TypeError("{0} must be an Imaginary number".format(var))
            elif tp == "Real":
                if not isReal(value):
                    raise TypeError("{0} must be a Real number".format(var))
            elif tp == "Integer":
                if not intQ(value):
                    raise TypeError("{0} must be an Integer".format(var))
            elif tp == "Whole":
                if not isWhole(value):
                    raise TypeError("{0} must be a Whole number".format(var))
            elif tp == "Natural":
                if not isNatural(value):
                    raise TypeError("{0} must be a Natural number".format(var))
            else:
                raise Exception("Internal Error")
            i += 1

    def __repr__(self):
        return "f({0}) = {1}".format(self.v, self.function)


Function = type("Function", (_Function, object), {})
