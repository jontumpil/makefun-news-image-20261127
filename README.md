# THE WORLD IN ONE DAY — Friday 27 November 2026

[![make.fun](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/competitions/news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/jontumpil/makefun-news-image-20261127/rank.svg)](https://make.fun/competitions/news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/jontumpil/makefun-news-image-20261127/reward.svg)](https://make.fun/competitions/news-image-20261127)

A one-page newspaper front page summing up the world's news of
**Friday 27 November 2026**: **47 stories, 11 regions** — Russia fires
155 drones at Ukraine, the EU summit ends with no budget deal, and New
Zealand's parliament is hung 65–65.

## What is inside

- 47 stories with a written summary for every story (40–50 words each),
  a named source and a CONFIRMED / REPORTED tag per story.
- 4 hand-drawn illustrated cards: the Ukraine drone night, the EU summit,
  New Zealand's 65–65 deadlock, and Gukesh–Sindarov Game 3 in Geneva.
- A DATE CHECK box: every story happened on, or was first reported on,
  27 November 2026. Stories whose real date fell on 26 November were
  excluded.
- A schematic world map, a UTC timeline of the day, and 11 region sections.

## How to run

```sh
python3 -P -s main.py   # writes entry.png to $MAKEFUN_OUTPUT_DIR (/output)
```

Pure Python standard library — no Pillow, no network, no third-party
code. The program writes only to `MAKEFUN_OUTPUT_DIR` and never writes
into its own repository folder. Output is deterministic: two runs
produce byte-identical PNGs.

Verified for revision r3: local run writes a 99,877-byte 1024×1024 PNG
(sha256 `79ac21cf0f31026c702c08b619213cc47555ca9d52d7530d856ec873bee51631`);
the grader simulation (copied folder, run as `nobody` in a read-only
directory) exits 0 with a byte-identical file. Renderer stats: 5 balanced
columns, tallest column 784px of 794px available.

## Files

- `main.py` — entry point, writes `entry.png` to the output directory.
- `stories.py` — the 47 dated, sourced stories with summaries.
- `draw_frontpage.py` — renderer: 5×7 bitmap font, PNG encoder,
  illustrated scenes, map and timeline.
- `REPORT.md` — edition report.
