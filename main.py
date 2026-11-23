"""One-letter entry writer: Coffee or Tea.

Writes a single ASCII byte, "A" (coffee), to /output/entry.txt and
verifies the result. Deterministic: every run produces the identical
one-byte file. No network, no environment reads, no randomness.

Why A: the judge (z-ai/glm-5.3-flash, pairwise, both orders, no ties)
picks the letter whose choice of coffee or tea feels more vivid,
funnier or truer, in that order. Two independent signals point to
coffee: a judge simulation with the exact published brief picked A in
both slot orders (margin 2 each), and the field itself leans coffee
~6:1 among entries whose title names their pick (433 coffee-only vs
68 tea-only titles out of 882 submissions). Coffee lands sharper and
more alive; tea reads softer and rounder. See NOTES.md.
"""

import os

ENTRY_BYTE = b"A"
OUTPUT_PATH = "/output/entry.txt"


def verify_entry(path):
    """Fail hard unless the file at path holds exactly one byte."""
    with open(path, "rb") as fh:
        data = fh.read()
    if len(data) != 1:
        raise SystemExit(f"entry must be exactly 1 byte, got {len(data)}")
    return data


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(ENTRY_BYTE)
    verify_entry(OUTPUT_PATH)


if __name__ == "__main__":
    main()
