from amath.Computation.Basic import fac
from .Function import Function
from .Polynomial import Polynomial


def Derivative(func, value=None):
    """Finds the derivative of a function

    If value is given, the derivative at that point will be returned.

    :type func: Function
    :param func:
    :param value:
    :return:
    """
    return func.derivative(value)


def Integrate(func, a=None, b=None):
    return func.integrate(a, b)


def Limit(func, value):
    pass


def TaylorSeries(func, value, num=5):
    poly = []
    func_der = func.derivative()
    for i in range(num):
        poly.append((func_der(value) / fac(i)))
    return Polynomial(poly[::-1])
