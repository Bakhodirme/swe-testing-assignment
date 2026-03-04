# Integration tests for Quick-Calc user interaction flow
from quick_calc.cli import process_input


def test_user_flow_addition():
    # simulate: 5 + 3 =
    assert process_input(["5", "+", "3", "="]) == "8"


def test_clear_after_calculation_resets_display():
    # simulate: 9 * 2 = then Clear
    assert process_input(["9", "*", "2", "=", "C"]) == "0"


def test_division_by_zero_is_handled_gracefully():
    # simulate: 5 / 0 =
    assert process_input(["5", "/", "0", "="]) == "Error: Division by zero"