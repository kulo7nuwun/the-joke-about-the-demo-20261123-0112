#!/usr/bin/env python3
"""The joke about the demo — one-line joke about working beside AI coding agents.

Writes exactly one line (1-280 chars, UTF-8) to /output/entry.txt.
Deterministic: same bytes on every run.
"""

import os

JOKE = (
    "The AI agent demoed perfectly \u2014 every test green \u2014 "
    "until the client clicked Save and the app deleted his own account."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
