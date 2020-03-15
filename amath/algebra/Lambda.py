class Lambda:
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

    def __repr__(self):
        return f"Lambda({self.var}, {self.expr})"

    def __call__(self, *args):
        pass
