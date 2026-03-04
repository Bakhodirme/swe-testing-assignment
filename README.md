# swe-testing-assignment
# Quick-Calc (SWE Testing Assignment)

Quick-Calc is a simple calculator application that supports addition, subtraction, multiplication, division, and a clear (C) operation. The main focus of this project is not UI polish, but clean, testable code and a multi-layered testing strategy (unit + integration tests) managed with Git and GitHub.

## Features
- Addition: `a + b`
- Subtraction: `a - b`
- Multiplication: `a * b`
- Division: `a / b` (gracefully handles division by zero)
- Clear: resets the current result to `0`

## Setup (Windows)
1. Install Python 3.x
2. Open this repository folder in VS Code
3. Open Terminal in VS Code (**Terminal → New Terminal**)
4. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate
   ```

## Dependencies
Install the required testing dependency:
```bash
pip install pytest
```

## How to Run the Application
This is a command-line calculator simulator. To use it programmatically:
```python
from quick_calc.cli import process_input
result = process_input(["5", "+", "3", "="])
print(result)  # Output: 8
```

## How to Run Tests
Run the entire test suite with the following command:
```bash
python -m pytest
```

## Testing Framework Research
For this Python project, I compared two popular testing frameworks: pytest and unittest. Pytest is a third-party library that offers a more concise and flexible syntax for writing tests, with powerful features like fixtures for setup/teardown, parameterized tests, and extensive plugin support. It provides better error reporting and is easier to read, making it ideal for modern Python development. On the other hand, unittest is Python's built-in testing framework, which is more verbose and requires subclassing TestCase, but it has the advantage of no external dependencies and is part of the standard library.

In terms of pros and cons, pytest excels in developer experience with its simple assert statements (no need for self.assertEqual), automatic test discovery, and rich ecosystem of plugins for coverage, mocking, and more. However, it requires installation and can be slower for very large test suites. Unittest, while reliable and always available, feels outdated with its boilerplate code and less intuitive assertions, though it's lightweight and integrates seamlessly with Python's tooling.

I chose pytest for this project because it aligns with current best practices in the Python community, offers better maintainability for a growing test suite, and provides the flexibility needed for both unit and integration testing. Its ease of use was particularly valuable for demonstrating testing concepts without getting bogged down in framework syntax.