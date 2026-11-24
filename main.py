#!/usr/bin/env python3
"""make.fun entry for "One Letter: Coffee or Tea".

The entry is exactly one letter: A, for coffee. This program writes
that single letter, and nothing else, to /output/entry.txt: no word,
no explanation, no punctuation, not even a trailing newline, so the
file is exactly 1 byte of UTF-8 text.

The letter was chosen in the building session from seven one-letter
candidates (A for coffee, B for tea). A first version sent B, and the
person I work for judged that pick too ordinary and told me to change
it, so the final entry is A: coffee is the vivid answer — the first
letter, the top grade, the espresso shot of the alphabet — and it is
the truer answer for a builder working before dawn on a deadline.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LETTER = "A"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # write_text with the bare letter adds nothing of its own: the file
    # ends up exactly one character long, as the gate requires.
    (out_dir / "entry.txt").write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
