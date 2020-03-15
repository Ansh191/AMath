class TimeoutException(Exception):
    """
    Error passed when Timeout occurs
    """
    pass


class IDEError(Exception):
    """
    Error when IDE does not support function
    """
    pass


class Failure(Exception):
    """
    Base Failure
    """
    pass


class InterpretationError(Failure):
    """
    Thrown when interpreter encounters an invalid value
    """
    pass


class TimeError(Exception):
    """
    Basic Time Error
    """
    pass


class DateError(Exception):
    """
    Basic Date Error
    """
    pass


class Indeterminate(Exception):
    """
    The could not be determined
    """
    pass
