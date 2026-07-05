---
name: python-testing-patterns
description: Design and implement Python tests with pytest, fixtures, mocking, parametrization, and regression coverage. Use when writing tests, setting up a test suite, debugging failing tests, choosing test scope, mocking external dependencies, or deciding what coverage is meaningful.
---

# Python Testing Patterns

Write tests that make behavior safer to change. Prefer focused, readable tests
over clever fixtures or coverage theater.

For advanced patterns such as async tests, monkeypatching, property-based tests,
database testing, CI, and coverage tooling, read `references/advanced-patterns.md`.

## Core Principles

- **One behavior per test.** A failure should point to one broken behavior.
- **Arrange / Act / Assert.** Keep setup, execution, and verification distinct.
- **Test boundaries and errors.** Happy-path tests alone are weak.
- **Isolate external effects.** Mock network, time, randomness, and services when
  they are not the behavior under test.
- **Use meaningful coverage.** Cover important behavior and risks, not every line.

## Basic Pytest Pattern

```python
def test_adds_two_numbers():
    result = add(2, 3)
    assert result == 5
```

For exceptions:

```python
import pytest

def test_rejects_zero_division():
    with pytest.raises(ValueError, match="zero"):
        divide(1, 0)
```

For parametrized cases:

```python
import pytest

@pytest.mark.parametrize("value, expected", [
    ("user@example.com", True),
    ("not-an-email", False),
])
def test_email_validation(value, expected):
    assert is_valid_email(value) is expected
```

## Fixtures

Use fixtures for reusable setup with clear lifetime:

```python
@pytest.fixture
def user():
    return User(id=1, email="a@example.com")
```

Avoid hidden fixture webs. If a test needs many fixtures, the unit may be too
coupled or the test may be too broad.

## Mocking

Mock at system boundaries:
- HTTP clients;
- filesystem or object storage;
- database sessions when not testing persistence;
- time and randomness;
- expensive model/API calls.

Prefer fakes over mocks when behavior is complex enough that call assertions
become brittle.

## Test Suite Shape

Use a small pyramid:
- many unit tests for pure logic;
- fewer integration tests for boundaries;
- a few end-to-end tests for critical workflows.

Name tests by behavior:

```text
test_<unit>_<scenario>_<expected_behavior>
```

## Output

When advising or writing tests, return:
- target behavior;
- test levels needed;
- fixtures/mocks;
- concrete test cases;
- missing edge/error paths;
- command to run the focused tests.
