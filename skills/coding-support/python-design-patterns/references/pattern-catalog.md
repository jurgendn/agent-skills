# Python Design Pattern Catalog

Use these examples only when a task needs concrete patterns.

## KISS

Prefer a dictionary or simple function over a factory when variants are known and
static.

```python
FORMATTERS = {"json": JsonFormatter, "csv": CsvFormatter}

def get_formatter(name: str) -> Formatter:
    return FORMATTERS[name]()
```

## Single Responsibility

Split orchestration from transformation. A function that validates, mutates,
persists, and serializes has too many reasons to change.

## Composition Over Inheritance

Prefer:

```python
class ReportService:
    def __init__(self, renderer: Renderer, store: Store):
        self.renderer = renderer
        self.store = store
```

over a deep inheritance hierarchy where subclasses override small hooks.

## Dependency Injection

Pass external effects in:

```python
def send_report(report: Report, mailer: Mailer) -> None:
    mailer.send(report.to_email())
```

This makes tests use fakes without patching global imports.

## Rule of Three

Two similar functions may still encode different business rules. Wait for the
third case before extracting a shared abstraction, then verify the abstraction
has a stable name in the domain.

## Anti-Patterns

- One subclass inheritance.
- Hidden global config.
- Utility modules that collect unrelated behavior.
- Repository pattern around a single query with no business boundary.
- Dataclasses used as unvalidated dictionaries.
