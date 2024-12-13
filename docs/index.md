# cookiecutter-sicheng-pythonic-pkg

A template for generating Python engineering projects using the [Cookiecutter](https://github.com/cookiecutter/cookiecutter) tool.

- Documentation: https://cookiecutter-sicheng-pythonic-pkg.readthedocs.io/en/latest/
- GitHub: https://github.com/sicheng1806/cookiecutter-sicheng-pythonic-pkg

## Features

- Uses [uv](https://github.com/astral-sh/uv) as the project virtual environment management tool.
- Configures `GitHub Actions`.
- Uses [ruff](https://github.com/astral-sh/ruff) as the code style linter.
- Uses [pytest](https://github.com/pytest-dev/pytest) as the testing framework.
- Uses [sphinx](https://github.com/sphinx-doc/sphinx) as the documentation generation tool.
- Uses [pre-commit](https://github.com/pre-commit/pre-commit) to configure automated review scripts before `git commit`.
- Uses [nox](https://github.com/wntrblm/nox) as the automation tool, and configures scripts for code style review, testing, and documentation building.
- Use [typos](https://github.com/crate-ci/typos) as a source code spell checker tool.
- Use [codecov]


## How to Use

1. Install [cookiecutter](https://github.com/cookiecutter/cookiecutter).
2. Use the template:
```bash
cookiecutter https://github.com/sicheng1806/cookiecutter-sicheng-pythonic-pkg
```

## Project Structure

```text
my_project/
├── docs
│   ├── conf.py
│   ├── development.md
│   ├── doc_requirements.txt
│   ├── index.md
│   ├── _static
│   └── _templates
├── LICENSE
├── noxfile.py
├── pyproject.toml
├── README.md
├── src
│   └── my_project
│       └── __init__.py
└── tests
    ├── conftest.py
    ├── __init__.py
    ├── settings.yml
    └── test_version.py
```

## Contents

```{toctree}
./development.md
```
