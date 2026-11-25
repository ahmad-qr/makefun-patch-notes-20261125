"""The funniest one-line patch note for a bug in real life.

Writes the note to /output/entry.txt for make.fun's
"Real-Life Patch Notes: The Comedy Changelog" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "v2.4.1: fixed a bug where the brain replayed an embarrassing "
    "moment from 2019 every night at 3 a.m."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 160 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 160, "line must be 1-160 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
