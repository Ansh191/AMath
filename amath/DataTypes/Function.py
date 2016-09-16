class _Function(object):
    def __init__(self, variables, function):
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


