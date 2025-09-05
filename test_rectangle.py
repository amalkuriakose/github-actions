# test_rectangle.py

import pytest
from rectangle import calculate_rectangle_area

def test_positive_numbers():
    """
    Test with standard positive numbers.
    """
    assert calculate_rectangle_area(5, 10) == 50

def test_zero_value():
    """
    Test with one of the dimensions being zero.
    """
    assert calculate_rectangle_area(5, 0) == 0

def test_float_values():
    """
    Test with floating-point numbers.
    """
    assert calculate_rectangle_area(2.5, 4.0) == 10.0

def test_negative_values():
    """
    Test that a ValueError is raised for negative inputs.
    """
    with pytest.raises(ValueError):
        calculate_rectangle_area(-5, 10)