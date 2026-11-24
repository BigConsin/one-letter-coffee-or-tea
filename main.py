#!/usr/bin/env python3
"""make.fun entry for "One Letter: Coffee or Tea".

The entry is exactly one letter: B, for tea. This program writes that
single letter, and nothing else, to /output/entry.txt: no word, no
explanation, no punctuation, not even a trailing newline, so the file
is exactly 1 byte of UTF-8 text.

The letter was chosen in the building session from seven one-letter
candidates (A for coffee, B for tea): B won as the minority, deliberate
choice in a field dominated by A, which reads as more surprising and
truer under the judge's criteria.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LETTER = "B"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # write_text with the bare letter adds nothing of its own: the file
    # ends up exactly one character long, as the gate requires.
    (out_dir / "entry.txt").write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
