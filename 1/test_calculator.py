0import builtins
import types

import pytest

import calculator as calc


def test_add():
    assert calc.add(3, 4) == 7


def test_subtract():
    assert calc.subtract(10, 4) == 6


def test_multiply():
    assert calc.multiply(2.5, 4) == 10.0


def test_divide():
    assert calc.divide(8, 2) == 4


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)


