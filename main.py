#!/usr/bin/env python3
"""One word for the boss: Kraken.

Why "Kraken": a boss who is a Kraken has a tentacle in every single
project at once, drags every deadline down into the deep without warning,
and surfaces only to pull someone under. It is one vivid creature, it
lands on its own with no explanation needed, and it is exactly the sort
of word a colleague repeats at lunch.
"""

import os

ENTRY_WORD = "Kraken"


def validate_entry(word: str) -> None:
    # Competition gate: UTF-8 text, 1-30 characters, not only whitespace,
    # and a single word (no internal whitespace).
    assert isinstance(word, str), "entry must be text"
    assert 1 <= len(word) <= 30, "entry must be 1-30 characters"
    assert word.strip() != "", "entry must not be only whitespace"
    assert len(word.split()) == 1, "entry must be a single word"
    word.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    validate_entry(ENTRY_WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_WORD)


if __name__ == "__main__":
    main()
