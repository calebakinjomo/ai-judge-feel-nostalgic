#!/usr/bin/env python3
"""Write one childhood memory to /output/entry.txt.

The entry is a single sentence, at most 280 characters, recalling a
rainy evening in a grandmother's kitchen: steam fogging her glasses,
a child on a stool stealing pieces of yam while she pretends not to
notice. Stdlib only, no network, no clock, no randomness: the same
bytes on every run.
"""

import os
import sys

ENTRY = (
    "Every rainy evening my grandmother would lift the pot lid just enough "
    "for the steam to fog her glasses, and I would stand on a stool beside "
    "her, stealing pieces of yam while she pretended not to notice."
)


def main() -> int:
    text = ENTRY
    if not 1 <= len(text) <= 280:
        print(f"entry must be 1-280 characters, got {len(text)}", file=sys.stderr)
        return 1
    if text.strip() == "" or "\n" in text or "\r" in text:
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    if text != text.strip():
        print("entry must not start or end with whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify byte-exactness before reporting success.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("read-back mismatch: entry.txt does not match ENTRY", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to entry.txt (verified by read-back)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
