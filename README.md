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
   .venv\Scripts\activate