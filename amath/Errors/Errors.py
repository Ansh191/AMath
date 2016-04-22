class TimeoutException(Exception):
    pass


class IDEError(Exception):
    pass


class Failure(Exception):
    pass


class InterpretationError(Failure):
    pass


class TimeError(Exception):
    pass


class DateError(Exception):
    pass