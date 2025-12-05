# about
https://adventofcode.com/2025

Fun, rushed, tdd, pythons, red green refactor,

# Python
## Install python
- [Download Python 3.14.0](https://www.python.org/ftp/python/3.14.0/python-3.14.0-amd64.exe)
- Run the .exe
- Check `Use admin privileges when install` and `add python.exe to PATH` and install
- Verify python installation `where.exe python`
- Restart IDE

# POETRY
## Install
- `python -m pip install pipx`
- `python -m pipx install poetry`
- `pipx ensurepath`
- `pipx inject poetry poetry-plugin-truststore`
- Verify poetry installation `where.exe poetry`
- Restart IDE

## Examples
- `poetry install` - installs all dependencies in pyproject.toml
- `poetry env activate` - go into virtual env
- `poetry add` - Add new dependcies to `pyProject.toml` via poetry. E.g. `poetry add pytest`
- `poetry add ...@2.212` add new dependencies with given version constraints. `@` exact, `^` most recent until major version. `~` up to latest until minor version
- `poetry show` - show what poetry has installed. `poetry show ...` show details of given package
- `poetry remove ...` - remove package
- `poetry lock` regenerate lock file, managed by poetry`
- `poetry version minor` - bump version of current project

## PyTest
All test classes must start `test`
All test methods must start `test_`
`poetry run python -m pytest file`

# To Do
