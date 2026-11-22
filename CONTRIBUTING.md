# Contributing to LinkedIn Funnel

Thank you for your interest in improving LinkedIn Funnel.

## Development & Testing Workflow

This project is built to run without external dependencies for core validation, while supporting standard Python tooling.

### 1. Requirements
- Python 3.10+
- Optional: `pytest` and `jsonschema` for development

### 2. Running Local Verification

Before submitting changes, run the built-in validation suite:

```bash
# Run the repository verification CLI
python3 -m linkedin_funnel verify

# Run context wiki linter
python3 context/scripts/wiki_lint.py

# Run unit tests
python3 -m unittest discover tests -v
```

### 3. Adding or Modifying Skills

When adding a new skill:
1. Create a dedicated directory under `skills/<skill-name>/` with a `SKILL.md`.
2. Ensure `SKILL.md` contains valid YAML frontmatter with `name` and `description`.
3. Register the new skill in `skills/catalog.json`.
4. Ensure `.agents/skills` and `.claude/skills` symlinks resolve to `skills/`.
5. Run `python3 -m linkedin_funnel verify` to confirm zero errors.

## Code of Conduct

Maintain senior, professional engineering standards. Ground all content and qualification logic in traceable data.
