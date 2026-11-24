#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about a small everyday annoyance to
/output/entry.txt. Deterministic: no network, no randomness, no model
calls at runtime -- the rant is a fixed literal, written out as-is.
"""

import os

RANT = (
    "At 3 a.m. my smoke detector began to chirp. Not an alarm. A chirp. "
    "One beep a minute, like a tiny robot clearing its throat at me. I "
    "stood on a chair in my underwear, broom in hand, hunting which of "
    "the four white discs was the traitor. No smoke. No fire. Just a "
    "dying battery, taking me down with it. I ripped it off the ceiling "
    "and threw it in a drawer, where it now chirps its revenge."
)


def main() -> None:
    text = RANT.strip()
    assert 1 <= len(text) <= 400, f"rant is {len(text)} chars, must be 1-400"
    assert text.strip(), "rant must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
