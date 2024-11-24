# Get Start

This project is a Python package that uses `uv` to manage the project.

## Project Develop Tools

This project requires the following two tools to be installed:

- [git](https://git-scm.com/) Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
- [uv](https://github.com/astral-sh/uv) An extremely fast Python package and project manager, written in Rust.

In addition to that, you also need to use `uv tool install` to install some auxiliary tools:

- [Ruff](https://github.com/astral-sh/ruff?tab=readme-ov-file) An extremely fast Python linter and code formatter, written in Rust.
- [pre-commit](https://github.com/pre-commit/pre-commit) A framework for managing and maintaining multi-language pre-commit hooks.
- [![Nox](https://img.shields.io/badge/%F0%9F%A6%8A-Nox-D85E00.svg)](https://github.com/wntrblm/nox) Flexible test automation with Python.
- [typos](https://github.com/crate-ci/typos) Finds and corrects spelling mistakes among source code.

## Init project environment

- `uv sync`  Update the project's environment.
- `pre-commit install` Install the pre-commit script.

## Develop

In addition to the regular development process, you can also use the following auxiliary tools to help with inspection and modification.

```{note}
Note that `uvx` is an alias for `uv tool run`.
```

### Format code style

- `uvx ruff check` run the Ruff linter.
- `uvx ruff format` run the Ruff formatter

or do it by nox: `nox -s lint`.

### Check spelling mistakes

- `uvx typos` to find spelling mistakes
- `uvx typos -w` to fix spelling mistakes

### Check test

- `uv run pytest` run the pytest

or do it by nox: `nox -s test`

```{note}
lint and test can both do by `nox`
```

### Build document

- `nox -s docs` build the document by sphinx.
- `nox -s docs-live` rebuild Sphinx documentation on changes, with hot reloading in the browser.

## Delivery

### Run nox

Run nox to format code style and check test.

```shell script
nox
```

### Git tag

Modify package version value, then commit.

Add tag

```shell script
git tag -a v0.1.0
```

### Build

Build this tag distribution package.

```shell script
uv build
```

### Upload index server

Upload to pypi server, or pass `--repository https://pypi.org/simple` to specify index server.

```shell script
uv publish
```

## Develop Guildlines
