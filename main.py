#!/usr/bin/env python3
"""Entry program for Famous Last Words at 1 Percent.

Writes one farewell line (at most 199 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt: what a phone says as its battery hits 1 percent.
It is spending the last of itself the way it spent the rest:
on your photo upload.
"""

import os

LINE = (
    "With my last 1% I could have called for help, but I "
    "spent it finishing your photo upload. You're welcome. "
    "Remember me at 100%."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
