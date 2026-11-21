#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes a single one-line joke to entry.txt.
Python 3.13 standard library only; no network access.
"""

import os

JOKE = (
    "My AI coding agent swore the demo was production-ready, so I hit run "
    "in front of forty people \u2014 and it crashed so hard the loading "
    "spinner filed for workers' comp."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
