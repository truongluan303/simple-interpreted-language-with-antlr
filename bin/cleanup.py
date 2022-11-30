#!/usr/bin/env python

import pathlib

# Find every pycache directory and remove them
[p.unlink() for p in pathlib.Path(".").rglob("*.py[co]")]
[p.rmdir() for p in pathlib.Path(".").rglob("__pycache__")]
