# REPORT — news-image-20261127, revision r3

## Edition

- **Date:** Friday 27 November 2026
- **Title:** Friday 27 November 2026: 47 stories, 11 regions — Russia fires
  155 drones at Ukraine, EU summit ends with no budget deal, New Zealand
  hung 65–65
- **Stories:** 47, each with a 40–50 word written summary, a named source
  and a CONFIRMED / REPORTED tag.
- **Regions (11):** Europe 7, Middle East 6, North America 6, Latin
  America 3, Africa 5, South Asia 4, East Asia 4, Southeast Asia 4,
  Oceania 3, Central Asia 2, Global 3.
- **Illustrated cards (4):** Ukraine drone night, EU summit "NO DEAL",
  New Zealand 65–65 deadlock, Gukesh–Sindarov chess (1.5–1.5).
- **Extras:** DATE CHECK box, schematic world map, UTC timeline.

## Top stories

1. Russia fires 155 drones at Ukraine (155 drones, 83 jet-powered
   Shaheds; 110 downed; 27 locations hit; power exports halted).
2. EU summit ends with no budget deal (no 2028–2034 budget, no €45bn
   Ukraine loan; 24 of 27 backed it; Czechia, Hungary, Slovakia out).
3. New Zealand hung parliament, 65–65 (final count; Opportunity Party
   with 7 seats holds the balance; Luxon must negotiate).

## Date discipline

Every story happened on, or was first reported on, 27 November 2026
(kit rule). Deliberately excluded as 26 November stories: the Nvidia
Southeast Asia shipment halt, the EU budget talks themselves, the
Guinea-Bissau election delay, the Cairo tanker fire and the Cartagena
supermarket siege. Stories first reported on 27 Nov about 26 Nov events
(Kuwait drone attack, Houthi Jazan strike, chess Game 3, Sri Lanka A
semi-final) are tagged REPORTED, not CONFIRMED.

## Verification

- `python3 stories.py` — dataset check (47 stories, 11 regions, summary
  word counts 40–55, headline length ≤ 37 chars) passes.
- Local run of `main.py` writes entry.png (99,877 bytes, 1024×1024) to
  MAKEFUN_OUTPUT_DIR; two local runs are byte-identical (sha256
  79ac21cf0f31026c702c08b619213cc47555ca9d52d7530d856ec873bee51631).
- Grader-sim (copy to /tmp, run as `nobody`, read-only): exit 0 and
  byte-identical sha256 vs the local run.
- Renderer stats: 5 balanced columns, tallest column 784px of 794px
  available (10px margin), 4 illustrated cards, DATE CHECK box, world
  map and UTC timeline all render. Layout visually inspected.
- Pure standard library only; the program writes solely to
  MAKEFUN_OUTPUT_DIR and never into its own repository folder.
