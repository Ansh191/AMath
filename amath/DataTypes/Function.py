from amath.testing.types import isReal, isComplex, isNatural, isWhole, intQ


class _Function(object):
    def __init__(self, variables, function):
        # type: (dict, str) -> None
        # type: (list, str) -> None
        # type: (str, str) -> None
        self.vars = {}
        if isinstance(variables, str):
            self.vars[variables] = "Real"
        elif isinstance(variables, list):
            for i in variables:
                if not isinstance(i, str):
                    raise TypeError("Invalid variable")
                else:
                    self.vars[i] = "Real"
        elif isinstance(variables, dict):
            for var in variables:
                if not isinstance(var, str):
                    raise TypeError("Invalid variable")
                if not (self.vars[var] in ["Imaginary", "Real", "Integer", "Whole", "Natural"]):
                    raise TypeError("Invalid variable type")
        else:
            raise TypeError("Invalid variable declaration")

        for var in self.vars:
            if var not in function:
                self.vars.pop(var)
                continue

            index = function.find(var)
            if index == -1:
                self.vars.pop(vars)
                continue

            function.replace(" ", "")

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
        run = None
        __call__ = None
        vl = []
        for var in self.vars:
            vl.append(var)
        v = ", ".join(vl)
        string = "def run(self, " + v + """):
                    self.check(""" + v + """)
                    return """ + function
        string2 = "def __call__(self, " + v + """):
                    return self.run(""" + v + ")"
        exec string
        exec string2
        setattr(Function, run.__name__, run)
        setattr(Function, __call__.__name__, __call__)

    def check(self, *args):
        if len(args) != len(self.vars):
            raise TypeError("check takes exactly {0} arguments ({1} given)".format(len(self.vars), len(args)))
        i = 0
        for var in self.vars:
            tp = self.vars[var]
            value = args[i]
            if tp == "Imaginary":
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


Function = type("Function", (_Function, object), {})
