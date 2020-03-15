import amath as m

functions = dict(zip(m.__all__, [getattr(m, x) for x in m.__all__]))


class _Function:
    def __init__(self, expression, variables):
        self.vars = {}
        if isinstance(variables, dict):
            for var in variables:
                if not isinstance(var, str):
                    raise TypeError("Invalid variable")
                variables[var] = variables[var].lower()
                if not (variables[var] in ["value", "number", "imaginary", "real", "integer", "whole", "natural"]):
                    try:
                        if not variables[var].__name__ == "_interpreter":
                            raise AttributeError()
                    except AttributeError:
                        raise TypeError("Invalid variable type")
            self.vars = variables
        elif isinstance(variables, list):
            for var in variables:
                if not isinstance(var, str):
                    raise TypeError("Invalid variable")
                else:
                    self.vars[var] = "value"
        elif isinstance(variables, str):
            self.vars[variables] = "value"
        else:
            raise TypeError("Invalid Variable Declaration")

        self.expression = expression

    def check_expression(self, expr: str):
        expr.find()

    def __repr__(self):
        return "f({0}) = {1}".format(self.vars, self.expression)

    def __call__(self, *args):
        variables = self.vars.copy()
        i = 0
        if len(args) != len(variables):
            raise TypeError(f"Function takes exactly {len(variables)} arguments ({len(args)} given)")
        for key in variables:
            variables[key] = args[i]
            i += 1

        self.check(variables)

        variables = {**variables, **functions}

        return eval(self.expression, variables)

    def check(self, variables):
        for key in variables:
            tp = self.vars[key]
            value = variables[key]

            if tp == "value":
                if not m.isValue(value):
                    raise TypeError("{0} must be a value".format(key))
            elif tp == "number":
                if not m.isNumber(value):
                    raise TypeError("{0} must be a number".format(key))
            elif tp == "imaginary":
                if not m.isComplex(value):
                    raise TypeError("{0} must be an Imaginary number".format(key))
            elif tp == "real":
                if not m.isReal(value):
                    raise TypeError("{0} must be a Real number".format(key))
            elif tp == "integer":
                if not m.intQ(value):
                    raise TypeError("{0} must be an Integer".format(key))
            elif tp == "whole":
                if not m.isWhole(value):
                    raise TypeError("{0} must be a Whole number".format(key))
            elif tp == "natural":
                if not m.isNatural(value):
                    raise TypeError("{0} must be a Natural number".format(key))
            else:
                try:
                    tp(value)
                except TypeError:
                    raise Exception("Internal Error")

    def getvars(self):
        return self.vars


class Expression:
    def __init__(self, expr: str):
        self.expr = expr
        self.first, self.second = self.find_operator()

    def find_operator(self):
        operators = ['**', '*', '/', '+', '-']
        index = None
        for operator in operators:
            index = self.expr.find(operator)
            if index != -1:
                break

        x = self.expr.split(operator, 1)
        return x

    def check_number(self):
        pass


Function = type("Function", (_Function, object), {})
