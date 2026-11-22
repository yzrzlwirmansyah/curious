#!/usr/bin/env python3
"""Entry generator for the make.fun bounty
"Make the AI judge feel curious".

Writes a single short curiosity piece to entry.txt in the output
directory given by MAKEFUN_OUTPUT_DIR (default /output).

The text is fixed and fully deterministic: one concrete image -- a
door in a garden wall that was not there yesterday, its key already
in the lock -- with the question left unanswered, so the image keeps
working after the last line. No imperatives, no stock phrases.
"""

import os

ENTRY_TEXT = (
    "A door stands in the garden wall where yesterday there was only "
    "brick, painted the same green as the gate. The key is already in "
    "the lock, and it turns. In the mornings I stand beside it "
    "a little longer every day. I have not opened it yet."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
