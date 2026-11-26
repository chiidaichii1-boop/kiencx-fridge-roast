#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins.

The program writes a single roast line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is fixed and deterministic: no randomness, no network, no clock,
no environment-dependent behaviour, so every run produces identical bytes.

The roast: the fridge's door-open alert texts its owner while the owner is
standing right in front of it, mid-snack -- an appliance that snitches.
It avoids the stock milk-reorder joke and names a real smart-fridge
behaviour (push alerts about the door) with a sting at the end.
"""

import os

# One line, one sentence, 143 characters -- inside the 1..160 gate.
LINE = (
    "My smart fridge just texted me the door's been open too long \u2014 "
    "I'm standing right here eating cheese at 2am, "
    "being snitched on by an appliance."
)


def main():
    """Write the roast line to entry.txt with no trailing newline."""
    text = LINE.strip()
    if not (1 <= len(text) <= 160):
        raise ValueError("entry must be 1..160 characters, got %d" % len(text))
    if text.count("\n") != 0:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
