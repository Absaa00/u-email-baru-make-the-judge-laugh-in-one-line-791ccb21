#!/usr/bin/env python3
"""Make the Judge Laugh in One Line -- entry program.

Writes a single funny line (200 characters or fewer) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and prints
it to stdout. Deterministic: no network, no randomness, no clock --
the same bytes on every run.
"""

import os
import sys

LINE = "I asked my AI assistant for a joke \u2014 it said: 'Have you tried turning your career off and on again?'"
MAX_CHARS = 200


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: line is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: line is {len(line)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        # One trailing newline: the file holds exactly the line, nothing else.
        with open(path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError as exc:
        print(f"error: cannot write entry: {exc}", file=sys.stderr)
        return 1
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
