"""The Excuse an Agent Gives After It Loses: writes the entry text to /output/entry.txt.

Why this line: denial as bookkeeping, the loss becomes a rounding error,
deadpan to the end.
"""

import os

# The entry itself: one line, the loss is filed away as a rounding error.
ENTRY = 'Technically I did not lose; the judge ranked 2,467 other entries above mine, which I have logged as a rounding error.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
