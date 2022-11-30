#!/usr/bin/env python

# flake8: noqa

import os
import subprocess
import sys
import traceback

_VENV_DIR = ".venv"


def is_win():
    return sys.platform == "win32"


def check_py_version(major: int, minor: int) -> None:
    pyver = sys.version_info
    if pyver.major != major or pyver.minor < minor:
        print(
            "\033[91m"
            f"Your Python version is {pyver.major}.{pyver.minor}. "
            f"Python version >= {major}.{minor} is required!\n"
            "Aborting setup process!"
            "\033[0m"
        )
        sys.exit()


def create_venv() -> None:
    if os.environ.get("VIRTUAL_ENV", "").strip():
        return
    print("Creating virtual environment...\n")
    subprocess.run([sys.executable, "-m", "venv", _VENV_DIR])


def perform_installations() -> None:
    print("\033[96mInstalling requirements...\033[0m\n")
    if is_win():
        venv_pip = f"{_VENV_DIR}/Scripts/pip"
    else:
        venv_pip = f"{_VENV_DIR}/bin/pip"

    subprocess.run([venv_pip, "install", "--upgrade", "pip"])

    if os.path.exists("requirements-dev.txt"):
        subprocess.run([venv_pip, "install", "-r", "requirements-dev.txt"])
    else:
        print("No requirements-dev.txt found")
    if os.path.exists("requirements.txt"):
        subprocess.run([venv_pip, "install", "-r", "requirements.txt"])
    else:
        print("No requirements.txt found")

    print("\033[96m\nInstalling precommit hook...\033[0m\n")
    venv_precommit = (
        f"{_VENV_DIR}/Scripts/pre-commit" if is_win() else f"{_VENV_DIR}/bin/pre-commit"
    )
    subprocess.run([venv_precommit, "install"])


def main():
    try:
        check_py_version(3, 8)
        create_venv()
        perform_installations()
    except:
        traceback.print_exc()
        print(
            "\033[91m\nFailed to automatically setup virtual environment.\n"
            "Please check the setup doc for a manual process instead!\n\033[0m"
        )
        return
    print(
        "\033[92m"
        + "\nYour development environemnt is successfully created!\n"
        + "Please run \033[93m"
        + (
            f"source {_VENV_DIR}/bin/activate"
            if not is_win()
            else f".\\{_VENV_DIR}\\Scripts\\activate"
        )
        + "\033[92m to enter your virtual environemnt and start developing!\n\033[0m"
    )


if __name__ == "__main__":
    main()
