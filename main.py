#!/usr/bin/env python3
"""One-letter entry: write the chosen letter to /output/entry.txt."""
import os

LETTER = "A"

def build_entry():
    """Return the single-letter entry text."""
    return LETTER

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(build_entry())

if __name__ == "__main__":
    main()
