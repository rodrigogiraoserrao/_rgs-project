# Project creation

```bash
% uv init rgs-project  # Create a project
% cd rgs-project
% uv run rgs-project   # Run the project command (see pyproject.toml > [project.scripts])

% uv add rich          # Add the dependency `rich`
```

# Quality checks

```bash
% uv add --dev ty ruff     # Add development dependencies

% uv run ruff format       # Format code
% uv run ruff check        # Lint your code
% uv run ruff check --fix  # Lint and auto-fix your code
% uv run ty check          # Type-check your code
```

# Testing

Tests live in `<project root>/tests`.

```bash
% uv add --dev pytest  # Add development dependency for testing
% uv run pytest        # Run the tests
```

# Automatic quality checks on commit

Pre-commit configuration lives in `.pre-commit-config.yaml`.

```bash
% uv add --dev pre-commit                                    # Add dev dependency for pre-commit hooks

% uv run pre-commit sample-config > .pre-commit-config.yaml  # Create sample configuration file

% uv run pre-commit install                                  # Install the hooks

% uv run pre-commit run --all-files                          # Sanity check: run all hooks
```

# GitHub Actions

GH Action configuration lives in `.github/workflows/*.yaml`.

# Publishing to (Test)PyPI

If you save your token in `.env`, make sure to add that file to `.gitignore`!

```bash
% uv build                     # Build the project

% set -a; source .env; set +a  # Export the UV_PUBLISH_TOKEN in .env (Unix/WSL)

% uv publish --index testpypi  # Publish to Test PyPI
```
