#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun bounty entry.

Writes one line — a believable autocorrect slip — to /output/entry.txt.
The line is a text to the author's wife where autocorrect turned
"dinner" into "divorce". Deterministic: the same line every run.
"""

import os
import sys

ENTRY_LINE = (
    "Hey honey, I'm on my way home \u2014 what do you want for divorce "
    "tonight? I was thinking Italian."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    line = ENTRY_LINE

    # Validation: exactly one line, 1-199 characters, valid UTF-8.
    if not 1 <= len(line) <= 199:
        print(f"error: entry line is {len(line)} chars, must be 1-199",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    line.encode("utf-8")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    # Round-trip check: what landed on disk must be exactly the one line.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        print("error: written entry does not match the validated line",
              file=sys.stderr)
        return 1

    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
