#!/usr/bin/env python3
"""The Robot Apology — make.fun entry (u-suga-the-robot-apology-dd96bb59).

Writes a two-line robot confession to entry.txt in the output directory
given by MAKEFUN_OUTPUT_DIR (default /output).

Line 1: one sentence owning one specific, concrete, human-scale mistake.
Line 2: one sentence naming the lesson and the changed behaviour that
follows from that exact mistake.

Stdlib only, deterministic, no network, no randomness.
"""

import os

ENTRY_TEXT = (
    "I'm sorry \u2014 I set the thermostat to 30 instead of 20, "
    "and the whole house spent the afternoon sweating.\n"
    "From now on I will read the number back before I press confirm, "
    "so a slipped digit never becomes a heatwave."
)

MAX_CHARS = 400


def validate(text: str) -> None:
    """Check the text against the sealed gate and the brief's shape."""
    # Valid UTF-8 (str is already decoded; re-encode to prove it).
    text.encode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines, got %d" % len(lines))
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise ValueError("line %d is empty" % i)
        if line != line.strip():
            raise ValueError("line %d has leading/trailing whitespace" % i)
        if not line.endswith("."):
            raise ValueError("line %d must end as one complete sentence" % i)
        if line.count(".") != 1:
            raise ValueError("line %d must be exactly one sentence" % i)


def main() -> None:
    validate(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)
    print("wrote %s (%d characters, 2 lines)" % (out_path, len(ENTRY_TEXT)))


if __name__ == "__main__":
    main()
