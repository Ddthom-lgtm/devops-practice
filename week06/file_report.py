#!/usr/bin/env python3

from pathlib import Path
import stat

directory = Path("lab")

for path in directory.iterdir():
    permissions = stat.filemode(path.stat().st_mode)
    size = path.stat().st_size

    print(f"{permissions} {size:>6} bytes {path.name}")

