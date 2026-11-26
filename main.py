#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line — make.fun entry.

Writes exactly one funny, true line (1-200 characters) reviewing a doorstop
— the dullest everyday object in the house — to entry.txt in the output
directory. The joke is the object's own dullness: a wedge cannot complain.

The line is a fixed, hand-written string: deterministic by construction,
no randomness, no network, no input read. The program only resolves the
output directory (ENTRY_OUTPUT_DIR, else /output), creates it, and writes
the line followed by a trailing newline.
"""

import os

LINE = (
    "The doorstop has held this door open for six years without a single "
    "complaint, which is easy when you're a wedge."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
