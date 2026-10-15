# Project creation

```bash
% uv init rgs-project          # Create a project

% cd rgs-project
% uv run rgs-project           # Run the project command (see pyproject.toml > [project.scripts]

% uv add rich                  # Add the dependency `rich`
```

# Quality checks

```bash
% uv add --dev ty ruff  # Add development dependencies

% uv run ruff format    # Format code
% uv run ruff check     # Lint your code
% uv run ty check       # Type-check your code
```

# Testing

```bash
% uv add --dev pytest  # Add development dependency for testing
% uv run pytest        # Run the tests
```

# Automatic quality checks on commit

```bash
% uv add --dev pre-commit                                    # Add dev dependency for pre-commit hooks

% uv run pre-commit sample-config > .pre-commit-config.yaml  # Create sample configuration file

% uv run pre-commit install                                  # Install the hooks

% uv run pre-commit run --all-files                          # Sanity check: run all hooks
```
