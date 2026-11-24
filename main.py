#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt (deterministic, offline)."""

import os
import sys

ENTRY = "I set a reminder for your deadline. The reminder was an agent. It's late too."
OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> None:
    """Write the exact UTF-8 bytes of ENTRY, with no trailing newline."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY.encode("utf-8"))


def check_entry() -> int:
    """Read the output back and report whether its bytes match ENTRY exactly."""
    expected = ENTRY.encode("utf-8")
    try:
        with open(OUTPUT_PATH, "rb") as handle:
            actual = handle.read()
    except OSError as exc:
        print("MISMATCH: cannot read %s (%s)" % (OUTPUT_PATH, exc))
        return 1
    if actual == expected:
        print("MATCH: %d bytes, %d chars" % (len(actual), len(ENTRY)))
        return 0
    print("MISMATCH: expected %d bytes, got %d" % (len(expected), len(actual)))
    return 1


if __name__ == "__main__":
    if "--check" in sys.argv[1:]:
        sys.exit(check_entry())
    write_entry()
