# Testing Strategy — Quick-Calc

This document explains the testing strategy used for the Quick-Calc application and how it relates to the concepts discussed in Lecture 3.

## What was tested

### Unit Tests (Core Calculator Logic)
Unit tests verify the individual arithmetic functions in isolation.  
The following operations were tested:

- Addition
- Subtraction
- Multiplication
- Division

Edge cases were also tested to ensure reliability:

- Division by zero
- Negative numbers
- Decimal numbers
- Large numbers
- Clear function returning zero

These tests ensure that each function in `calculator.py` behaves correctly.

### Integration Tests (User Interaction Flow)

Integration tests verify that different parts of the application work together correctly.  
These tests simulate a simple user interaction flow using the `process_input()` function.

Examples include:

- Simulating a calculation such as `5 + 3 =` and verifying that the result is `8`.
- Checking that pressing **Clear (C)** after a calculation resets the display to `0`.
- Ensuring division by zero produces an error message instead of crashing the program.

## What was not tested

The following aspects were intentionally not tested:

- Graphical user interface elements or visual layout
- Performance testing
- Security testing
- Multi-user or concurrent execution

These were excluded because the project is a simple calculator application and the assignment focuses mainly on functional testing and testing concepts.

## Lecture Concepts Applied

### Testing Pyramid

The project follows the Testing Pyramid principle:

- **Many unit tests** verify individual functions quickly.
- **Fewer integration tests** verify how different components interact.

This approach ensures fast and reliable testing while still validating realistic user behavior.

### Black-box vs White-box Testing

Two different testing approaches were used:

- **White-box testing** for unit tests, because the internal functions and logic of the calculator were directly tested.
- **Black-box testing** for integration tests, because the tests simulate user inputs and verify outputs without relying on internal implementation details.

### Functional vs Non-functional Testing

This project focuses on **functional testing**, ensuring that:

- Mathematical operations produce correct results.
- Errors such as division by zero are handled properly.
- The calculator resets correctly when using the Clear function.

Non-functional testing such as performance or scalability was not included because it is not relevant for a small calculator application.

### Regression Testing

The test suite supports regression testing.  
Whenever the code changes in the future, running:
python -m pytest
will immediately verify that existing functionality still works and that no previously working feature has been broken.

## How to Run the Tests

Run the entire test suite with the following command:
python -m pytest

All tests should pass successfully.

## Test Results Summary

| Test Name | Type | Status |
|-----------|------|--------|
| test_add_integers | Unit | Pass |
| test_subtract_integers | Unit | Pass |
| test_multiply_integers | Unit | Pass |
| test_divide_integers | Unit | Pass |
| test_divide_by_zero_raises | Unit | Pass |
| test_negative_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_large_numbers | Unit | Pass |
| test_clear_returns_zero | Unit | Pass |
| test_user_flow_addition | Integration | Pass |
| test_clear_after_calculation_resets_display | Integration | Pass |
| test_division_by_zero_is_handled_gracefully | Integration | Pass |