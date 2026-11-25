#!/usr/bin/env python3
"""One-line entry for make.fun: the best meal I ever had.

Writes a single sentence (at most 200 characters) to entry.txt in the output
directory. Standard library only; no network, no clock, no randomness, so the
two grading runs produce byte-identical output.
"""

import os
import sys

ENTRY = (
    "At 2 a.m. on a night train, my mother unwrapped cold nasi bakar in banana "
    "leaf, and the steam smelled like home before I even tasted it."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
