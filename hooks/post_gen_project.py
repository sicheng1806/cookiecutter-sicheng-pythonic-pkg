"""Post-generate project hooks"""

import os
import shutil
from pathlib import Path


def remove_file(file: Path, *files: Path):
    """
    Remove file
    :param file:
    :param files:
    :return:
    """
    os.remove(file)
    for _f in files:
        os.remove(_f)


def setup_ci_tools(flag: str):
    """
    Setup ci tools
    :param flag:
    :return:
    """
    if flag != "github":
        shutil.rmtree(".github", ignore_errors=True)


if __name__ == "__main__":
    CI_TOOLS = "{{ cookiecutter.ci_tools }}"

    setup_ci_tools(CI_TOOLS)
