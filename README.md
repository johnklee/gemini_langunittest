# gemini_langunittest
Use Gemini CLI to write and execute test cases

## Using Gemini CLI for Test Generation

This project is configured to facilitate the generation of unit tests using the Gemini CLI. The specific instructions for the CLI's behavior are defined in `GEMINI.md`. The CLI will automatically follow these guidelines to create `pytest` compatible test files in the `tests/unit/` directory.

### Example Usage

Here is a step-by-step example of how to use Gemini CLI to write and launch a new test case.

**1. Add a new function to the source code.**

First, let's add a `subtract` function to `utils/math.py`:

```python
# utils/math.py

"""Module to conduct math operations."""

def add(a: float, b: float) -> float:
  """Addes `a` with `b`.

  Args:
    a: Value 1 to add.
    b: Value 2 to add.

  Returns:
    `a + b`
  """
  return a + b

def subtract(a: float, b: float) -> float:
  """Subtracts `b` from `a`.

  Args:
    a: Value to subtract from.
    b: Value to subtract.

  Returns:
    `a - b`
  """
  return a - b
```

**2. Prompt Gemini CLI to generate the tests.**

Next, provide a prompt to the Gemini CLI asking it to generate the unit tests for the new function.

**User Prompt:** "Generate unit tests for the `subtract` function in `utils/math.py`."

**3. Review the generated test file.**

The Gemini CLI will create a new test file or update the existing one with the following content:

```python
# tests/unit/test_math.py

"""Unit test cases for the `math` module."""
import pytest
from utils.math import add, subtract

def test_add_positive_numbers():
  """Test case to add positive numbers."""
  assert add(1, 2) == 3

# ... existing add tests ...

def test_subtract_positive_numbers():
  """Test case to subtract positive numbers."""
  assert subtract(5, 2) == 3

def test_subtract_negative_numbers():
  """Test case to subtract negative numbers."""
  assert subtract(-5, -2) == -3

def test_subtract_mixed_numbers():
  """Test case to subtract a negative number from a positive number."""
  assert subtract(5, -2) == 7

def test_subtract_zero():
  """Test case to subtract zero."""
  assert subtract(5, 0) == 5

def test_subtract_to_negative():
  """Test case where the result is negative."""
  assert subtract(2, 5) == -3
```

**4. Run the tests.**

Finally, you can run the tests, including the newly generated ones, using the standard test command:

```bash
python -m pytest tests/
```

## Testing

This project uses `pytest` for unit testing.

### Prerequisites

Ensure you have [Poetry](https://python-poetry.org/) installed.

### Installation

Install the project dependencies:

```bash
poetry install
```

### Running Unit Tests

To execute the test suite, run the following command:

```bash
python -m pytest tests/
```

### Code Coverage

To generate a code coverage report for the `utils` package, run:

```bash
python -m pytest --cov=utils tests/
```
