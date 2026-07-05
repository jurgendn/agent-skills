# Python Style Configs

Use this when concrete configuration or templates are needed.

## Ruff

```toml
[tool.ruff]
line-length = 120
target-version = "py312"

[tool.ruff.lint]
select = [
    "E",
    "W",
    "F",
    "I",
    "B",
    "C4",
    "UP",
    "SIM",
]
ignore = ["E501"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

## Mypy

```toml
[tool.mypy]
python_version = "3.12"
strict = true
warn_unused_ignores = true
warn_return_any = true
```

Use strict settings for libraries and research infrastructure; relax locally for
notebooks or quick exploratory scripts when needed.

## Google-Style Docstring

```python
def load_records(path: Path, *, strict: bool = True) -> list[Record]:
    """Load records from a JSONL file.

    Args:
        path: Input JSONL file.
        strict: If true, raise on malformed rows; otherwise skip them.

    Returns:
        Parsed records in file order.

    Raises:
        ValueError: If a row is malformed and strict is true.
    """
```

## README Minimum

- What the project does.
- How to install.
- One working command.
- Where outputs go.
- How to run tests.
