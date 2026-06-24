# test-bounty-repo

Minimal repo to validate Tamagochi's GitHub bounty cycle end-to-end.

## Setup

```bash
pip install -r requirements.txt
pytest
```

`test_divide` fails until `divide()` is fixed (currently returns `a + b` instead of `a / b`).

## Issue

See [ISSUE.md](ISSUE.md) for the GitHub issue text to paste manually.
