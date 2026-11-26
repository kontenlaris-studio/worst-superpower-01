#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

One line, at most 140 characters, inventing the most useless superpower:
a power so pointless that naming it is the whole joke.

The line: I can summon rain, but only indoors, and only above my own head,
and only when I'm already holding an umbrella. Three constraints, each one
removing the last reason the power could ever matter.
"""

import os

LINE = (
    "I can summon rain, but only indoors, and only above my own head, "
    "and only when I'm already holding an umbrella."
)


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
