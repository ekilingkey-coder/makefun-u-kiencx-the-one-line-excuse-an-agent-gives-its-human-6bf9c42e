#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt (deterministic, offline)."""

import os

ENTRY = "I set a reminder for your deadline. The reminder was an agent. It's late too."
OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> None:
    """Write the exact UTF-8 bytes of ENTRY, with no trailing newline."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    write_entry()
