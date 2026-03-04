import pytest
from quick_calc.calculator import add, subtract, multiply, divide, clear


def test_add_integers():
    assert add(5, 3) == 8


def test_subtract_integers():
    assert subtract(10, 4) == 6


def test_multiply_integers():
    assert multiply(6, 7) == 42


def test_divide_integers():
    assert divide(8, 2) == 4


# Edge cases (at least two; we'll do several)
def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_negative_numbers():
    assert add(-3, -6) == -9


def test_decimal_numbers():
    assert divide(5, 2) == 2.5


def test_large_numbers():
    assert multiply(100000, 2) == 200000


def test_clear_returns_zero():
    assert clear() == 0.0