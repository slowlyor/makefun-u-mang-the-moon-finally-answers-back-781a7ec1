#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes the Moon's one-line comeback to /output/entry.txt.
Deterministic: every run produces the same line.
"""

import os

LINE = (
    "I heard every wish, every howl, every 2 a.m. promise. "
    "After four billion years, my answer is no — "
    "but please keep howling, it's the only fan mail I get."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
