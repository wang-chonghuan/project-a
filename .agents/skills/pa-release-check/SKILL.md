---
name: pa-release-check
description: Run a lightweight release readiness check for the project-a placeholder service.
---

# pa-release-check

Before release:

1. Run `python -m pytest`.
2. Confirm `README.md` command examples still work.
3. Confirm version metadata in `pyproject.toml` is intentional.
