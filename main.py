#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune cookie line for a crypto trader who has just been
liquidated, to /output/entry.txt. The line is fixed: a single fortune,
at most 20 words, in the cookie's voice, with the joke landing on the
loss itself -- rueful and warm, never cruel.
"""

import os

FORTUNE = (
    "Fortune favors the brave, but the market favors the patient "
    "\u2014 your liquidation just bought you patience, wholesale."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 160, "fortune must be 1-160 characters"
    assert len(text.split()) <= 20, "fortune must be at most 20 words"
    assert "\n" not in text, "fortune must be a single line"
    # The harness mounts the output directory at /output; the path is
    # fixed on purpose -- nothing is read from the environment.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
