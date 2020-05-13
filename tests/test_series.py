from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series 

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_three():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_four():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_lucas_one():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_two():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_three():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected