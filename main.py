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
    # and a single word (no whitespace of any kind, no control chars).
    assert isinstance(word, str), "entry must be text"
    assert 1 <= len(word) <= 30, "entry must be 1-30 characters"
    assert word.strip() != "", "entry must not be only whitespace"
    assert len(word.split()) == 1, "entry must be a single word"
    assert not any(c.isspace() for c in word), "entry must contain no whitespace"
    assert not any(ord(c) < 0x20 or ord(c) == 0x7F for c in word), (
        "entry must contain no control characters"
    )
    assert word.encode("utf-8").decode("utf-8") == word, "entry must round-trip UTF-8"


def main() -> None:
    validate_entry(ENTRY_WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_WORD)
    # Verify the written bytes are exactly the entry word: 6 bytes, no
    # trailing newline, no encoding surprise.
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == ENTRY_WORD.encode("utf-8"), "output bytes mismatch"


if __name__ == "__main__":
    main()
