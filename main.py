#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes a single one-line joke to entry.txt.
Python 3.13 standard library only; no network access.
"""

import os

MIN_LENGTH = 1
MAX_LENGTH = 280

JOKE = (
    "My AI coding agent swore the demo was production-ready, so I hit run "
    "in front of forty people \u2014 and it crashed so hard the loading "
    "spinner filed for workers' comp."
)


def validate_joke(text: str) -> None:
    """Reject a joke that is empty or longer than a single short post."""
    length = len(text)
    if not MIN_LENGTH <= length <= MAX_LENGTH:
        raise SystemExit(
            f"joke must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {length}"
        )


def main() -> None:
    validate_joke(JOKE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
