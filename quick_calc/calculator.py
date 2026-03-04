"""
Quick-Calc core logic (pure functions).
Keeping this file UI-free makes unit testing easy and matches the testing pyramid.
"""

def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        # "Graceful" handling: explicit error instead of crashing unpredictably
        raise ValueError("Division by zero")
    return a / b


def clear() -> float:
    return 0.0