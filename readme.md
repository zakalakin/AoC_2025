# About
https://adventofcode.com/2025

Python | Advent Of Code | For-Fun | Test Driven Design (TDD) | Red-Green Refactor

# Setup Project
## Install Python
- [Download Python 3.14.0](https://www.python.org/ftp/python/3.14.0/python-3.14.0-amd64.exe)
- Run the .exe
- Check `Use admin privileges when install` and `add python.exe to PATH` and install
- Verify python installation `where.exe python`
- Restart IDE

## Install Poetry
- `python -m pip install pipx`
- `python -m pipx install poetry`
- `pipx ensurepath`
- `pipx inject poetry poetry-plugin-truststore`
- Verify poetry installation `where.exe poetry`
- Restart IDE

## Run Poetry
- `poetry install` - installs all dependencies in pyproject.toml

# Execute Project
Select correct python interpreter, `poetry env activate`. VS select interpreter: `ctrl` + `shift` + `p`

Run PyTest `poetry run python -m pytest {file}`

Run from main.py

# Maintain Project
## Poetry Examples
- `poetry install` - installs all dependencies in pyproject.toml
- `poetry env activate` - Go into virtual env
- `poetry add` - Add new dependcies to `pyProject.toml` via poetry. E.g. `poetry add pytest`
- `poetry add ...@2.212` Add new dependencies with given version constraints. `@` exact, `^` most recent until major version. `~` up to latest until minor version
- `poetry show` - Show what poetry has installed. `poetry show ...` Show details of given package
- `poetry remove ...` - Remove package
- `poetry lock` Regenerate lock file, managed by poetry`
- `poetry version minor` - Bump version of current project

## PyTest
Used for unit tests/integration tests. A test version of each functional modules (files)/class/method should exist:
All test files should start `test_`
All test classes must start `test`
All test methods must start `test_`

Run PyTest `poetry run python -m pytest {file}`

# To Do
