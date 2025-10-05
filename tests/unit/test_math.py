# tests/unit/test_math.py

import pytest
from utils.math import add

def test_add_positive_numbers():
    """Test adding two positive numbers."""
    assert add(2, 3) == 5

def test_add_negative_numbers():
    """Test adding two negative numbers."""
    assert add(-2, -3) == -5

def test_add_positive_and_negative():
    """Test adding a positive and a negative number."""
    assert add(5, -3) == 2
    assert add(-5, 3) == -2

def test_add_zero():
    """Test adding with zero."""
    assert add(10, 0) == 10
    assert add(0, 10) == 10
    assert add(0, 0) == 0

def test_add_floats():
    """Test adding floating-point numbers."""
    assert add(2.5, 3.5) == 6.0
    assert add(-2.5, 1.0) == -1.5
