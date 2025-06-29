import pytest
from lib.calculator import sum, minus, multiply, divide

def test_sum():
    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    assert sum(0, 0) == 0

def test_minus():
    assert minus(5, 3) == 2
    assert minus(0, 0) == 0
    assert minus(-1, -1) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(0, 1) == 0

    with pytest.raises(ValueError):
        divide(20, 0)