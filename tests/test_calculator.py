"""Test suite for the Calculator class."""

import pytest  # type: ignore
from calculator.calculator import Calculator

def test_add():
    """Tests the addition functionality of the calculator."""
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(0, 0) == 0

def test_subtract():
    """Tests the subtraction functionality of the calculator."""
    assert Calculator.subtract(10, 4) == 6
    assert Calculator.subtract(5, 10) == -5
    assert Calculator.subtract(0, 0) == 0

def test_multiply():
    """Tests the multiplication functionality of the calculator."""
    assert Calculator.multiply(3, 3) == 9
    assert Calculator.multiply(-1, 5) == -5
    assert Calculator.multiply(0, 10) == 0

def test_divide():
    """Tests the division functionality of the calculator, including division by zero."""
    assert Calculator.divide(10, 2) == 5
    assert Calculator.divide(-10, 2) == -5
    assert Calculator.divide(1, 1) == 1
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(10, 0)
