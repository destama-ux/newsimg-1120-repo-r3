# Build notes — news-image-20261120 r3 (revision run)
## "The World in One Day — Friday 20 November 2026: 34 verified stories"

One-page newspaper image (1024×1024 JPEG) summing up the world news of
Friday 20 November 2026. Same day, same 34 verified stories and facts as
r2, rebuilt from a fresh page after a study of the live leaderboard
(`STUDY.md`). 13 illustrated panels + 21 one-line briefs, a UTC timeline
strip, a six-stat number strip, a coloured region bar, a world map with
pins for stories 1–13, and a forensic date-check box.

## Why an r3

R2 deep check: score 985,464, prize_rank #169 of ~10,300; top-50 cutoff
988,550 — gap 3,086 points. Live board at r3 study time (~03:30 WIB
21 Nov): cutoff #50 is 988,551 (email-game), gap 3,087; our r2 has
slipped to prize_rank #170 (rank #171), 12W / 0D / 0L, 90% interval
979,293–991,636, and is not marked contended. The top 50 are all 12
wins / 0 losses in 12 judge duels, so the gap is a picture-editor
judgement gap, not a win-count gap. The leader study (top-10 artifact
images viewed individually) found the same anatomy everywhere — the fix
is execution, not structure. Full study: `STUDY.md`.

## What changed vs r2 (and why)

- **Stat strip rebuilt from the day's biggest verified numbers.**
  R2's strip spent two of six slots on softer numbers (19,000 channels
  removed; 24.6m GTA VI copies). R3: 3 bridges hit (Kyiv) · 70–80 km/h
  (Akvan winds) · 100,000 youth visas a year (UK–EU) · $87.66
  (Anthropic pre-market) · 500,000 tablets seized (opioid ring) ·
  $2.36bn (GTA VI day-one sales, estimated). Lead-story numbers first.
  19,000 and 24.6m stay on the page, in panels 8 and 12 where they
  belong.
- **Bolder art at the same height.** Lead art 102px, medium art
  48px (r2: 106/48px — the height budget went to the timeline's own
  row, larger headlines and the wider map). Bigger Akvan spiral
  filling the frame; thicker red chart line in the AI panel with a
  bolder "−9.8%" and "DAY TWO" label, its end dot moved clear of the
  label; Kyiv label as one bold bar "KYIV — 3 BRIDGES HIT · 5
  KILLED". No new figures: leaders' per-index Asian closes are NOT
  in our verified facts and were not reproduced.
- **Three weak medium panels redrawn.** Panel 7 (Prabowo–Xi): Beijing
  skyline behind the Indonesian and Chinese flags with an "XI ·
  BEIJING" label (was two flags on flat red). Panel 8 (Google):
  channel-list graphic — rows with play icons, "19,000+ REMOVED"
  (was a play button and a stray unexplained "X"). Panel 6 (US
  shutdown): the SHUTDOWN stamp moved clear of the Capitol dome and
  "$350bn SOUGHT" enlarged. Panel 4 (COP31): labels shortened to
  "NO DEAL" / "OVERTIME" so neither is clipped.
- **Panel bodies trimmed to at most 2 lines** (same facts, tighter
  wording), freeing space for larger headlines (lead 17px, medium
  14px) and taller art.
- **Wider map, larger pins.** Map 300→320px wide; pins 13px circles
  with bold white numbers; Europe cluster spread with deliberate
  offsets (London 13, Frankfurt 11, Brussels 5, Kyiv 1, Antalya 4);
  pin 12 (GTA VI, worldwide) placed just off Florida's east coast;
  pin 3 New York / pin 6 Washington separated. Legend kept:
  "Red pins mark stories 1–13. Briefs run 14–34. Positions
  approximate."
- **Region bar rebuilt as one line of coloured chips** on a dark bar
  (was proportional segments so narrow that "MIDDLE EAST 1" and
  "AFRICA 1" wrapped). Same counts, now all legible on one line,
  ending "= 34 STORIES".
- **Timeline given its own full-width row** (was crammed into the
  region bar's black strip in r2). Same six items and timestamps,
  "NEW YORK" dropped from the last two items to fit one line.
- **Date-check reworded** to "Left out on purpose — first reported
  Thursday 19 Nov, so NOT shown as Friday's news:" — same six
  exclusions as r2.
- **Kicker tightened** to "34 VERIFIED STORIES · 6 REGIONS · ALL
  DATED FRIDAY 20 NOVEMBER 2026" (was "all from this one day").
- **Kept from r2:** giant serif date masthead; concrete four-story
  italic subhead; 13 panels with source tags on every story; UTC
  timeline; 21 briefs in two columns with bold city prefixes; footer
  sources line. Two brief wordings shortened only to fit one line
  (32: "amid" → "in"; 34: "masks each bilateral limit" → "masks
  bilateral limits", source tag "Reuters Breakingviews" → "Reuters").

## Layout fit

First render: content overflowed the 1024px frame (footer cut off),
the region bar wrapped, the timeline and three briefs were clipped at
the right edge, and two in-art labels were clipped. Three render
passes fixed: page padding and gaps tightened (~37px saved), region
bar rebuilt as chips, timeline shortened, briefs given min-width:0
plus shortened wordings, Akvan label shortened, COP31/Capitol labels
resized, map pins repositioned. Final render: footer bottom inside
the frame, nothing clipped, nothing overflowing — visually verified
in the PNG render and the final JPEG (4 passes total).

## Size

Artwork is **287,639 bytes at JPEG quality 78** (1024×1024, sha256
e2c94f21d4063e212b1168f0dc4d1b5b455711dbed928c453d4a1ead86173863) —
under the ~300 KB target and inside the 1 MiB limit. Quality 78 was
chosen over 80 (299,646 bytes) because it leaves real margin under
~300 KB and is smaller on the tie-break axis, at no visible quality
cost. Rendered from `page.html` with headless Chromium
(chrome-headless-shell, 1024×1024 viewport) → PNG → JPEG with Pillow.

## Story list with sources (all reporting of Fri 20 Nov 2026 — unchanged from r2)

Panels (13, same order as r2):
1. Three Kyiv bridges hit in a major Russian missile attack; five killed.
   BBC.
2. Cyclone Akvan landfall near Gopalpur, Odisha — 70–80 km/h, gusting 90;
   no major damage/deaths; third cyclone in a month. IMD / Reuters.
3. Anthropic slides day two — pre-market $87.66, −9.8% vs $97.17 close;
   European shares head for worst week since March. Reuters / Finnhub.
4. COP31 final day — no final text, talks into overtime Saturday; draft
   omits fossil fuels; Panama threatened formal objection. AP.
5. UK–EU reset deal signed in Brussels — youth mobility 100,000/yr each
   way, food-trade checks scrapped, carbon markets linked from 2028;
   tuition fees unresolved. Reuters.
6. US shutdown looms as Iran war splits Congress; Trump seeks $350bn
   Pentagon funding. Reuters.
7. Prabowo meets Xi in Beijing — economy, investment, South China Sea.
   Reuters.
8. Indonesia asks Google to justify removing 19,000+ pro-government
   YouTube channels. Reuters.
9. India busts opioid ring shipping ~500,000 tablets to US buyers via
   messaging apps; six arrested. Reuters.
10. Seoul appeals court upholds Kakao founder Kim Beom-su's acquittal on
    SM Entertainment share-rigging charges. Reuters / Yonhap.
11. Deutsche Bank leaks — bank forwarded Trump's tax return by mistake;
    ~$582m Epstein-linked transactions flagged; shares down >10% on the
    week. Reuters Breakingviews.
12. GTA VI — 24.6m copies, est. $2.36bn in 24 hours (Sensor Tower);
    Metacritic 99. NME / AsiaToday.
13. Pancreatic cancer pill trial saw tumours vanish. BBC.

Briefs (14–34): 14 Iraq forces enter Kataib Hezbollah stronghold (Reuters);
15 Democrats probe Nvidia's Megaspeed sway (Reuters); 16 Europe ready for
Russia talks on ending the war (BBC); 17 White House removes cyber-security
chief (BBC); 18 consent-law calls after Young case (BBC); 19 Airbnb house
rules in force (BBC); 20 UK fridges secured from hackers (BBC);
21 stockpiling lifts retail sales after 'Be Ready' (BBC); 22 UK coldest
night of autumn, −10C (BBC); 23 Russell fastest in wet Las Vegas GP
practice (BBC); 24 UFC bans Fiorot three months (BBC); 25 Rams' Nacua
suspended for misconduct (BBC); 26 Wales face Slovenia in March play-off
(BBC); 27 Prince Harry would rejoin the army (BBC); 28 William and Kate
meet Modi as India tour ends (BBC); 29 UK to send Ukraine 1,000
long-range strike drones (BBC); 30 France unrest may cost insurers
€207m (Euronews); 31 stabbed Bradford councillor 'protecting a staff
member' (BBC); 32 rand at one-year low amid coalition talks (Reuters);
33 Musk 'pretty foolish' over midterm spending (Reuters); 34 analysis:
Shenzhen summit masks each bilateral limit (Reuters Breakingviews).

Regions: Asia-Pacific 7 · Europe 15 · Middle East 1 · Africa 1 ·
Americas 6 · Global 4 = 34.

Stat strip: 3 (bridges hit, Kyiv) · 70–80 km/h (Akvan winds) ·
100,000 (UK–EU youth visas/yr) · $87.66 (Anthropic pre-market) ·
500,000 (tablets seized) · $2.36bn (GTA VI day-one sales, estimated).

UTC timeline: 02:14 Seoul — Kakao cleared (Reuters 02:14:42 UTC);
02:30 Gopalpur — landfall begins (08:00 IST); 05:50 Gopalpur — landfall
complete (11:20 IST); 08:05 London — shares −1% (0805 GMT);
10:30 — ANT −4.7% pre-market (1030 GMT); 13:38 — ANT $87.66
pre-market (Finnhub snapshot 13:38:20 UTC).

Date-check box names the excluded other-days' news: Anthropic's $97.17
first-day close and the ICJ Myanmar genocide verdict (both Thursday) ·
the Trump–Xi–Putin summit itself (Thursday) · GTA VI's launch (Thursday) ·
Korea's Suneung exam (Thursday) · the COP31 revised draft (Thursday).

## Date verification

20 November 2026 is a Friday, confirmed with the system date command
(`TZ=Asia/Jakarta date -d 2026-11-20` → Friday 2026-11-20 WIB) in v1;
carried over unchanged.

## Weakest-sourced items (flagged honestly — unchanged from r2)

- Story 12's sales figures are a Sensor Tower *estimate*, not official
  Rockstar/Take-Two numbers — labelled as an estimate on the page.
- Story 3's pre-market figures come from Finnhub quote data ($87.66,
  −9.79% at 08:19 EST) and Sharecast's 10:30 GMT report (−4.7%, $92.60);
  the timeline uses both, at their own timestamps.
- Story 13 (cancer pill) rests on a single BBC headline item; no trial
  name or journal was in the copy read.
- The timeline's 02:30 UTC landfall start converts the IMD's "around
  8 am" IST bulletin; the 05:50 UTC completion converts the 11:20 IST
  bulletin.

## Production and verification (21 Nov 2026)

- `page.html` is a fresh composition written for r3 (r2's page.html was
  not read before writing; facts taken from r2's BUILD-NOTES.md and
  STUDY.md). `artwork.jpg` was rendered from it with headless
  Chromium (1024×1024 viewport) → PNG → JPEG quality 78.
- Final artwork: JPEG, exactly 1024×1024, 287,639 bytes (limit 1 MiB),
  sha256 e2c94f21d4063e212b1168f0dc4d1b5b455711dbed928c453d4a1ead86173863.
- `main.py` is a fresh composition from the spec (validates artwork.jpg:
  exists, JPEG SOI FF D8, ≤1 MiB, SOF dimensions exactly 1024×1024,
  then byte-copies to entry.png in $MAKEFUN_OUTPUT_DIR, falling back to
  a local "output" dir). Written in one full write plus one small
  clarifying comment edit.
- Verified: `MAKEFUN_OUTPUT_DIR=/tmp/ni1120-r3-out python3 main.py`
  exits 0 and the produced entry.png is byte-identical to artwork.jpg
  (`cmp` clean). A negative test with a corrupt JPEG exits 1.
- Story count: 3 lead + 10 medium panels + 21 briefs = 34; briefs
  numbered 14–34 continuously; region counts sum to 34.
- The render was visually inspected four times (PNG three times, final
  JPEG once); all in-art labels legible, timeline complete, map pins
  numbered 1–13, date-check and footer inside the frame.

## Status

- Package only. NOT bundled, NOT submitted, NO git repo created by
  this run (repo assembly is a separate step). Bundle + check + submit
  to be done from a fresh main-chat session under the new run-record
  rules. Note Force_Last: this r3 replaces r2 only when submitted;
  r2 (score 985,464, #170) remains the standing entry until then.
