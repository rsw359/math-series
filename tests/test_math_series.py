from math_series import fibonacci
from math_series import lucas
from math_series import sum_series


def test_fib_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fib_two():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fib_three():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_luc_one():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_luc_two():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_sum_one():
    assert sum_series(2, 3, 25) is 28
