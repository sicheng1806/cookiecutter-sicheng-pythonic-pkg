import nox

python_version = "3.12"

nox.options.sessions = ["lint", "test"]
nox.options.default_venv_backend = "uv"
# nox.options.reuse_venv = True


@nox.session(reuse_venv=True)
def lint(session):
    session.run("uvx", "ruff", "check", external=True)
    session.run("uvx", "ruff", "format", external=True)


@nox.session(python=python_version)
def test(session):
    requirements = nox.project.load_toml("pyproject.toml")["project"]["dependencies"]
    if requirements:
        session.install(*requirements)
    session.install(".")
    session.install("pytest")
    session.run("pytest")
