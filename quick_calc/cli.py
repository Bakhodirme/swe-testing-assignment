"""
A minimal input-layer simulator for integration testing.

We simulate "button presses" as tokens:
Examples:
  ["5", "+", "3", "="] -> "8"
  ["9", "*", "2", "=", "C"] -> "0"
"""

from __future__ import annotations
from quick_calc.calculator import add, subtract, multiply, divide, clear


def process_input(tokens: list[str]) -> str:
    display = 0.0
    current_op: str | None = None
    pending: float | None = None

    def apply(op: str, left: float, right: float) -> float:
        if op == "+":
            return add(left, right)
        if op == "-":
            return subtract(left, right)
        if op == "*":
            return multiply(left, right)
        if op == "/":
            return divide(left, right)
        raise ValueError(f"Unknown operator: {op}")

    for token in tokens:
        token = token.strip()

        # Clear
        if token.upper() == "C":
            display = clear()
            current_op = None
            pending = None
            continue

        # Equals
        if token == "=":
            # No-op if incomplete expression
            continue

        # Operator
        if token in {"+", "-", "*", "/"}:
            current_op = token
            pending = display
            continue

        # Number
        try:
            num = float(token)
        except ValueError:
            return "Error: Invalid input"

        if pending is None:
            display = num
        else:
            try:
                display = apply(current_op, pending, num)  # type: ignore[arg-type]
            except ValueError as e:
                if "Division by zero" in str(e):
                    return "Error: Division by zero"
                return "Error"
            pending = None
            current_op = None

    # Format output nicely (8.0 -> 8)
    if display.is_integer():
        return str(int(display))
    return str(display)