"""Unit test cases for the `math` module."""
import pytest
from utils.math import add

def test_add_positive_numbers():
  """Test case to add positive numbers."""
  assert add(1, 2) == 3

def test_add_negative_numbers():
  """Test case to add negative numbers."""
  assert add(-1, -2) == -3

def test_add_mixed_numbers():
  """Test case to add a positive and a negative number."""
  assert add(1, -2) == -1

def test_add_zero():
  """Test case to add zero."""
  assert add(1, 0) == 1

def test_add_floats():
  """Test case to add floats."""
  assert add(1.2, 2.3) == 3.5
