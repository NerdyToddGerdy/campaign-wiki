# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

CampaignWiki is a Python project (>=3.10) managed with **Poetry**.

## Commands

```bash
# Install dependencies
poetry install

# Run the project (update once an entry point exists)
poetry run python -m campaignwiki

# Add a dependency
poetry add <package>

# Add a dev dependency
poetry add --group dev <package>
```

### Testing (once configured)
```bash
poetry run pytest
poetry run pytest tests/path/to/test_file.py::test_name  # single test
```

### Linting (once configured)
```bash
poetry run ruff check .
poetry run mypy .
```

## Architecture

> This project is in early initialization. Update this section as structure is established.

- **Build system:** Poetry (`pyproject.toml`)
- **Python version:** 3.10+
- **Source layout:** TBD — add notes here when modules are created