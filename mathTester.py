# -*- coding: utf-8 -*-
from __future__ import division
import math
import cmath
import os
import datetime as dt
import time as t
import scipy
from scipy import constants as cs
import amath as m
from amath import Fraction


def test_sqrtof16():
    assert m.sqrt(16) == 4


def test_sqrtof2():
    assert m.sqrt(2) == math.sqrt(2)


def test_sqrtofminus1():
    assert m.sqrt(-1) == 1j


def test_infinitygreater():
    assert m.inf > 999999999


def test_infinityless():
    assert m.Ninf < 999999999


def test_infinityComplex():
    try:
        return m.Cinf == 5
    except ValueError:
        assert True


def test_infdata():
    assert type(m.inf) == m.Infinity


def test_e():
    assert m.e == math.e


def test_pi():
    assert m.pi == math.pi


def test_gr():
    assert m.gr == cs.golden_ratio


def test_nan():
    assert not m.nan == m.nan


def test_d():
    assert m.d(5, 2) == 2.5


def test_m():
    assert m.m(5, 2) == 10


def test_s():
    assert m.s(5, 2) == 3


def test_a():
    assert m.a(5, 2) == 7


def test_dectofr():
    assert m.dectofr(1.5) == Fraction(3, 2)


def test_frtodec():
    assert m.frtodec(Fraction(3, 2)) == 1.5


class TestFraction:
    def test_add(self):
        assert Fraction(2, 3) + Fraction(5, 3) == Fraction(7, 3)

    def test_sub(self):
        assert Fraction(5, 3) - Fraction(4, 3) == Fraction(1, 3)

    def test_mul(self):
        assert Fraction(1, 4) * Fraction(5, 4) == Fraction(5, 16)

    def test_div(self):
        assert Fraction(1, 4) / Fraction(4, 1) == Fraction(1, 16)

    def test_pow(self):
        assert Fraction(2, 3) ** 2 == Fraction(4, 9)

    def test_isint(self):
        assert Fraction(4, 2).is_int() == True

    def test_mod(self):
        assert Fraction(5, 3) % Fraction(4, 3) == Fraction(1, 3)

    def test_trunc(self):
        assert int(Fraction(6, 4)) == 1

    def test_float(self):
        assert 0.75 == float(Fraction(3, 4))

    def test_int(self):
        assert int(Fraction(5, 4)) == 1


class TestTime:
    def test_add(self):
        assert timeObject(1, 2, 3, 4) + timeObject(1, 2, 3, 4) == timeObject(2, 4, 6, 8)

    def test_sub(self):
        assert timeObject(4, 4, 4, 4) - timeObject(1, 1, 1, 1) == timeObject(3, 3, 3, 3)

    def test_greater(self):
        assert timeObject(1, 2, 3, 5) > timeObject(1, 2, 3, 4)

    def test_less(self):
        assert timeObject(1, 2, 3, 4) < timeObject(1, 2, 3, 5)

    def test_equal(self):
        assert timeObject(1, 2, 3, 4) == timeObject(1, 2, 3, 4)

    def test_to12(self):
        x = timeObject(1, 2, 3, 4)
        # assert x.to12() == '01:02:03.004 AM'


def test_abs():
    assert m.abs(-5.2) == 5.2


def test_ceil():
    assert m.ceil(5.3) == 6


def test_ceil2():
    assert m.ceil(-5.4) == -5


def test_fac():
    assert m.fac(5) == 120


def test_floor():
    assert m.floor(2.6) == 2


def test_floor2():
    assert m.floor(-2.3) == -3
