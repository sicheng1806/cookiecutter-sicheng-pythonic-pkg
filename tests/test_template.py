"""Test Test whether the template works correctly."""

import subprocess
from pathlib import Path
import shutil

tmpdir = Path(".tmp")


def init_tmpdir():
    if tmpdir.exists():
        shutil.rmtree(tmpdir)


def test_cookiecutter():
    init_tmpdir()
    result = subprocess.run(
        ["python", "-m", "cookiecutter", ".", "-o", tmpdir, "--no-input"]
    )
    assert result.returncode == 0


if __name__ == "__main__":
    test_cookiecutter()
