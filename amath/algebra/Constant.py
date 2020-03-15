from .Polynomial import Polynomial


class Constant:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return self.name

    def __add__(self, other):
        return Polynomial([])
