from amath.DataTypes import LambdaType


class _Function(object):
    def __init__(self, variables, function):
        # type: (dict, LambdaType) -> None
        # type: (list, LambdaType) -> None
        # type: (str, LambdaType) -> None
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
                if not (self.vars[var] in ["Imaginary", "Real", "Irrational", "Rational",
                                           "Integer", "Whole", "Natural"]):
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
            try:
                int(before)
            except ValueError:
                con = True

            if not con:
                function = function[:index] + "*" + function[index:]
        _do = None
        vl = []
        for var in self.vars:
            vl.append(var)
        v = ", ".join(vl)
        print(v)
        string = "def _do(self, " + v + """):
                    return """ + function
        print(string)
        exec string
        setattr(Function, _do.__name__, _do)


Function = type("Function", (_Function, object), {})
