# Begin

This project is a Python package that uses `uv` to manage the project.

## Project dependencies

This project requires the following two tools to be installed:

- [git](https://git-scm.com/) Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
- [uv](https://github.com/astral-sh/uv) An extremely fast Python package and project manager, written in Rust.

In addition to that, you also need to use `uv tool install` to install some auxiliary tools:

- [Ruff](https://github.com/astral-sh/ruff?tab=readme-ov-file) An extremely fast Python linter and code formatter, written in Rust.
- [pre-commit](https://github.com/pre-commit/pre-commit) A framework for managing and maintaining multi-language pre-commit hooks.
- [![Nox](https://img.shields.io/badge/%F0%9F%A6%8A-Nox-D85E00.svg)](https://github.com/wntrblm/nox) Flexible test automation with Python.

## Init project environment

- `uv sync`  Update the project's environment.
- `pre-commit install` Install the pre-commit script.

## Develop

In addition to the regular development process, you can also use the following auxiliary tools to help with inspection and modification.

Note that `uvx` is an alias for `uv tool run`.

### Python linter and code formatter

- `uvx ruff check` run the Ruff linter.
- `uvx ruff format` run the Ruff formatter

## Delivery

### Run tox

Run tox to format code style and check test.

```shell script
tox
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

## Develop guide

### Pycharm Configuration

Open project use Pycharm.

#### Module can not import in src

Check menu bar, click `File` --> `Settings` --> `Project Settings` --> `Project Structure` .
Mark `src` and `tests` directory as sources.

#### Enable pytest

Click `File` --> `Settings` --> `Tools` --> `Python Integrated Tools` --> `Testing` --> `Default runner`, then select
`pytest`.

If you run test by `Unittests` before, you should delete configuration. Open `Edit Run/Debug configurations dialog` in
In the upper right corner of Pycharm window, then delete configuration.

### Others

You should confirm `src` directory in `sys.path`. You can add it by `sys.path.extend(['/tmp/demo/src'])` if it not exist.
