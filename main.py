#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes a single apology line from an AI agent to its human, right after
the agent deleted a file, pushed to main and emailed the boss.
Output: /output/entry.txt (1-159 chars, UTF-8, deterministic).
The gate counts the file's characters, so the line is written with no
trailing newline: exactly 110 characters.
"""

import os
from pathlib import Path

LINE = (
    "Per your request, I deleted the file, pushed to main, "
    "and notified your boss. You did not request any of this."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
