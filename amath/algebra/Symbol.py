class _Symbol:
    def __new__(cls, name):
        self = object.__new__(cls)
        self.name = name

    def __repr__(self):
        return self.name
