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
            for var, tp in variables:
                if not isinstance(var, str):
                    raise TypeError("Invalid variable")
                if not (tp in ["Imaginary", "Real", "Irrational", "Rational", "Integer", "Whole", "Natural"]):
                    raise TypeError("Invalid variable type")
        else:
            raise TypeError("Invalid variable declaration")

        if not isinstance(function, LambdaType):
            for var, tp in self.vars:
                if var not in function:
                    self.vars.pop(var)
                    continue

                index = function.find(var)
                if index == -1:
                    self.vars.pop(vars)
                    continue

                function.replace(" ", "")

                l = list(function)
                index = l.index(var)

