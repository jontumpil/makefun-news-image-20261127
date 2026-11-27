#!/usr/bin/env python3
"""Entry point for news-image-20261127. Standard library only.

Renders THE WORLD IN ONE DAY for Friday 27 November 2026 as a
deterministic 1024x1024 PNG and writes it to MAKEFUN_OUTPUT_DIR.
The grader runs this program in a read-only repository as user nobody,
so NOTHING is ever written into the repository folder.
"""

import argparse
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from draw_frontpage import render_png
from stories import STORIES, TITLE, DATE_CHECK


def resolve_out(arg_out):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if os.path.isabs(arg_out):
        return arg_out
    return os.path.join(out_dir, arg_out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="entry.png",
                    help="output file; relative paths resolve under "
                         "MAKEFUN_OUTPUT_DIR")
    args = ap.parse_args()
    out = resolve_out(args.out)
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    data = render_png(STORIES, TITLE, DATE_CHECK)
    # Guard: never write a broken or empty image to the output dir.
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "renderer did not produce a PNG"
    assert len(data) > 1000, "rendered PNG is suspiciously small"
    with open(out, "wb") as f:
        f.write(data)
    size = os.path.getsize(out)
    digest = hashlib.sha256(data).hexdigest()
    print("wrote %s (%d bytes) sha256=%s" % (out, size, digest))
    assert size < 1024 * 1024, "entry.png is over the 1 MiB limit"


if __name__ == "__main__":
    main()
