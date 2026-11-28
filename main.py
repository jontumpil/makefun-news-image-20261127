# main.py — THE WORLD IN ONE DAY, Friday 27 November 2026 (r5).
# Pure standard library. Renders the front page and writes it ONLY to
# MAKEFUN_OUTPUT_DIR (the grader runs in a read-only repo as nobody, so
# nothing may be written beside this script).
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from draw_frontpage import render_page  # noqa: E402
from stories import check  # noqa: E402

check()
png, stats = render_page()
assert len(png) <= 1048576, len(png)
assert not stats["overflow"], stats

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "entry.png")
# Guard: the entry must never escape the grader's output directory.
assert os.path.commonpath(
    [os.path.abspath(out_dir), os.path.abspath(out_path)]
) == os.path.abspath(out_dir), out_path
with open(out_path, "wb") as fh:
    fh.write(png)
print("wrote", out_path, len(png), "bytes (r5)", stats)
