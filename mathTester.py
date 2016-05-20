import amath as m


def test_a():
    assert m.a(5, 2) == 7


def test_a2():
    assert m.a(5, -2) == 3


def test_a3():
    assert m.a(5, 2.3) == 7.3


def test_abs():
    assert m.abs(5) == 5.0


def test_abs2():
    assert m.abs(-5) == 5.0


def test_abs3():
    assert m.abs(2j) == 2.0


def test_alltrue():
    assert m.alltrue([1, 3, 5], m.evenQ)

def test_alltrue():
    assert m.alltrue([2,4,6], m.evenQ)


