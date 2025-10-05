# Gemini Langunittest

This repository demonstrates using the Gemini CLI to automate common development tasks like generating unit tests, linting, and checking code coverage.

## Example Workflow

Here is a step-by-step example of how you can use the Gemini CLI to write, lint, and test code in this repository.

### 1. Generating Test Cases

First, ask the Gemini CLI to create a test case for a specific module.

**User Prompt:** `Please create test case for module utils/math.py`

The CLI will identify the functions in `utils/math.py` and generate a corresponding test file in `tests/unit/test_math.py` with comprehensive test cases.

```python
# tests/unit/test_math.py

import pytest
from utils.math import add

def test_add_positive_numbers():
    """Test adding two positive numbers."""
    assert add(2, 3) == 5

def test_add_negative_numbers():
    """Test adding two negative numbers."""
    assert add(-2, -3) == -5

def test_add_positive_and_negative_numbers():
    """Test adding a positive and a negative number."""
    assert add(5, -3) == 2
    assert add(-5, 3) == -2

def test_add_zero():
    """Test adding with zero."""
    assert add(5, 0) == 5
    assert add(0, 5) == 5
    assert add(0, 0) == 0

def test_add_floats():
    """Test adding floating-point numbers."""
    assert add(2.5, 3.5) == 6.0
    assert add(2.5, -3.5) == -1.0
```

### 2. Running Tests

After the test file is created, the CLI will automatically run the test suite to verify the code.

```bash
$ python -m pytest tests
============================= test session starts ==============================
...
tests/unit/test_math.py .....                                            [100%]
============================== 5 passed in 0.04s ===============================
```

### 3. Linting and Auto-Fixing

Next, you can ask the CLI to perform a lint check and apply fixes automatically.

**User Prompt:** `Do linting check on utils/ and fix warning.`

The CLI will run `flake8`, identify issues, and prompt for approval before fixing them.

**Linting Output:**
```
utils/math.py:3:1: E302 expected 2 blank lines, found 1
```

After applying the fix, the CLI will re-run the linter and the test suite to ensure that the changes were safe.

**Verification:**
```bash
$ flake8 utils/
✅ All good! No linting warnings found.

$ python -m pytest tests
============================== 5 passed in 0.03s ===============================
```

### 4. Checking Code Coverage

Finally, you can request a code coverage report.

**User Prompt:** `Show code coverage of utils/math.py`

The CLI will run `pytest` with the coverage flag and display the results.

```bash
$ python -m pytest --cov=utils.math --cov-report term-missing tests/
================================ tests coverage ================================
Name            Stmts   Miss  Cover   Missing
---------------------------------------------
utils/math.py       2      0   100%
---------------------------------------------
TOTAL               2      0   100%
============================== 5 passed in 0.07s ===============================
```

