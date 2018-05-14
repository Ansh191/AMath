class _Array:
    def __init__(self, *args):
        if len(args) > 2:
            raise ValueError("Only takes 2 arguments")

        if len(args) == 0:
            self.value = None
            self.type = object

        if len(args) == 1:
            try:
                self.value = [x for x in args[0]]
            except TypeError:
                self.value = args[0]

            try:
                tp = type(self.value[0])
                for i in self.value:
                    if type(i) == tp:
                        continue
                    else:
                        tp = object
                        break
            except TypeError:
                tp = type(self.value)
            self.type = tp

        else:
            if not isinstance(args[1], type):
                raise TypeError("'type' must be a type")
            try:
                self.value = [x for x in args[0]]
            except TypeError:
                self.value = args[0]

            try:
                x = []
                for i in args[0]:
                    x.append(args[1](i))
                self.value = x
            except TypeError:
                self.value = args[1](self.value)
            self.type = args[1]

    def __repr__(self):
        return "Array({0}, {1})".format(self.value, self.type)

    def __iter__(self):
        return iter(self.value)

    def __recompute(self):
        pass

    def astype(self, tp):
        if not isinstance(tp, type):
            raise TypeError("'tp' must be a type")

        try:
            x = []
            for i in self.value:
                x.append(tp(i))
            self.value = x
        except TypeError:
            self.value = tp(self.value)
        self.type = tp

    def list(self, tp):
        if not isinstance(tp, type):
            raise TypeError("'tp' must be a type")

        try:
            return tp(self)
        except TypeError:
            raise TypeError("'tp' must be a str, list, set, frozenset, or tuple")
        except AttributeError:
            raise TypeError("'tp' must be a str, list, set, frozenset, or tuple")

    def append(self, value):
        if isinstance(self.value, list):
            self.value.append(value)


Array = type("Array", (_Array, object), {})
