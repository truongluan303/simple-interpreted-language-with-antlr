#!usr/bin/env python

import os
from subprocess import check_output, run

_VENV_DIR = ".venv"


def main():
    venv_pip = (
        "pip" if os.environ.get("VIRTUAL_ENV", "").strip() else f"{_VENV_DIR}/bin/pip"
    )
    all_packages = check_output([venv_pip, "freeze"]).decode("utf-8").split("\n")

    for package in all_packages:
        if package:
            run([venv_pip, "uninstall", package, "-y"])


if __name__ == "__main__":
    main()
