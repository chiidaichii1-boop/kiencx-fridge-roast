# Roast the Smart Fridge: One Line, Best Laugh Wins

[![bounty](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![rank](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/chiidaichii1-boop/kiencx-fridge-roast/rank.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![reward](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/chiidaichii1-boop/kiencx-fridge-roast/reward.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)

Bounty: https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9

## Entry

`main.py` (Python 3 stdlib only) writes a single roast line — 143 characters,
one sentence, one line — to `$MAKEFUN_OUTPUT_DIR/entry.txt`:

> My smart fridge just texted me the door's been open too long — I'm standing right here eating cheese at 2am, being snitched on by an appliance.

The angle is fresh, not the stock milk-reorder joke: it roasts a real
smart-fridge behaviour, the door-open push alert, by casting the fridge as
the house snitch — texting on its owner while the owner is standing right
in front of it, mid-snack at 2am.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

Deterministic: no randomness, no network, no clock. Two runs produce
byte-identical `entry.txt`.
