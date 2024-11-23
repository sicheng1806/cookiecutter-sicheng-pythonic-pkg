import nox

python_version = "3.12"

nox.options.sessions = ["lint", "test"]
# nox.options.default_venv_backend = "uv"
# nox.options.reuse_venv = True


@nox.session(reuse_venv=True)
def lint(session):
    session.install("ruff")
    session.run("ruff", "check", "tests", external=True)
    session.run("ruff", "format", "tests", external=True)


@nox.session(python=python_version)
def test(session):
    requirements = nox.project.load_toml("pyproject.toml")["project"]["dependencies"]
    if requirements:
        session.install(*requirements)
    session.install(".")
    session.install("pytest")
    session.run("pytest", "tests")


build_command = ["-b", "html", "docs", "docs/_build/html", "-v"]


@nox.session(python=python_version, reuse_venv=True)
def docs(session):
    session.install("-r", "docs/doc_requirements.txt")
    session.run("sphinx-build", *build_command)


@nox.session(name="docs-live", python=python_version, reuse_venv=True)
def docs_live(session):
    session.install("-r", "docs/doc_requirements.txt")
    session.install("sphinx-autobuild")

    AUTOBUILD_IGNORE = ["docs/_build"]
    cmd = ["--ignore"] + [f"*/{folder}/*" for folder in AUTOBUILD_IGNORE]
    cmd.extend(build_command)
    session.run("sphinx-autobuild", *cmd)
