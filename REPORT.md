# REPORT — news-image-20261127 (Friday 27 November 2026)

## Edition

- Title: "Friday 27 November 2026: 46 stories, 7 regions - Kuwait drone
  strike kills two Italians, New Zealand election deadlocked, Gukesh
  holds Sindarov"
- Stories: 46 (43 CONFIRMED, 3 REPORTED)
- Regions: 7 — Middle East (4), Europe (9), North America (8),
  South Asia (13), East Asia & Pacific (5), Africa (2), Global (5)
- Illustrated scenes: 14 (6 large cards + 8 small pictograms)
- Extras: DATE CHECK box, schematic world map, UTC timeline 00:08–05:15

## Date discipline

Every story was checked against its source's own publication date and
kept only if published on 27 November 2026. Excluded as not dated
27 Nov: the Nvidia Southeast Asia shipment halt (26 Nov), the EU
budget summit (26 Nov), the Guinea-Bissau election delay (26 Nov),
the Cairo fuel-tanker fire (25–26 Nov), and the Cartagena supermarket
siege (25 Nov).

## Top stories

1. Two Italians killed in a Kuwait drone strike blamed on Iran
   (BBC / NYT).
2. New Zealand's final election count: coalition loses majority,
   65–65 deadlock (Farmers Weekly).
3. Gukesh–Sindarov Game 3: 60-move draw, match level 1.5–1.5 (FIDE).

## Verification (local)

- `python3 -P -s main.py` with MAKEFUN_OUTPUT_DIR set: entry.png
  rendered, 87,124 bytes (under 1 MiB), two consecutive runs
  byte-identical (sha256 bb709a4fa680f74ae9a4817af5152d19ce0912667
  215e0a3cab19db273990403).
- Grader simulation: copy to /tmp/bot27, `chmod -R a+rX`, run as
  `nobody` with MAKEFUN_BOT_DIR / MAKEFUN_OUTPUT_DIR set: exit 0,
  /tmp/out27/entry.png sha256 identical to the local render.
- No non-stdlib imports in main.py, stories.py, draw_frontpage.py.
- Layout note: the first build overflowed the 5-column flow, so the
  edition now uses 6 balanced columns (binary-search column breaks)
  and 46 stories; the Spider-Man re-release story was dropped as the
  weakest item. Scene art was fixed after a visual check showed the
  Jazan flame, Kuwait blast and tanker smoke drawing outside their
  cards.

## Files

- main.py — entry point, writes entry.png to MAKEFUN_OUTPUT_DIR
- stories.py — 47 dated stories with summaries, sources, tags
- draw_frontpage.py — pure-stdlib PNG renderer (fonts, scenes, map)
- README.md, REPORT.md, LICENSE (MIT), .makefun/owner.json
