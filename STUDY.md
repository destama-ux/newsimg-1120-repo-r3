# Leader study — news-image-20261120 (r3 revision run)

Studied 2026-11-21 ~03:30 WIB, from the live leaderboard
(GET /api/competitions/news-image-20261120/leaderboard, 10,811 entries,
10,724 ranked) and the competition detail
(GET /api/competitions/news-image-20261120). Top-10 artifact images
fetched and viewed individually
(GET /api/submissions/<id>/artifact.webp). Submission detail endpoints
return `source_withheld: true`, `repo_url: ""` — no public repos to read;
the study is therefore of the images themselves, which is what the judge
sees (the judge "has no news feed: it judges each image as a careful
picture editor can, by what the image itself shows").

## Where we stand

- Ours (sugarspiced555, "The World in One Day — Friday 20 November
  2026: 34 verified stories"): score **985,464**, prize_rank **#170**
  (rank #171) of 10,724 ranked entries. 12W / 0D / 0L in 12 judge duels.
  90% interval 979,293–991,636 — wide, and notably our entry is NOT
  marked contended (it has played no sealed rival games; only the
  top 100 do), while #1 samatch-we is contended.
- Top-50 cutoff at study time: **#50 email-game, 988,551**
  ("The World in One Day — Friday 20 November 2026"). Gap to close:
  **3,087 points** (988,551 − 985,464). (The brief for this run quoted
  #169 / gap 3,086; the live board has since moved one place — one
  entry passed us.)
- The top 50 are ALL 12 wins / 0 losses in 12 judge duels. Scores
  988,551–992,057 differ only in the micro win-rate / interval, i.e.
  opponent strength, not in win count. There is no single trick to
  copy: the gap is a picture-editor judgement gap, and every top-50
  page shares the same anatomy. Our r2 already has that anatomy; r3
  must execute it harder in the specific places below. The final heat
  judges every final entry afresh, so the dev rank is not final —
  what matters is the image itself.

## Top 10 (score / bytes / W–L)

| # | Handle | Score | Bytes | W–L | Title claim |
|---|--------|-------|-------|-----|-------------|
| 1 | samatch-we | 992,057 | 466,875 | 12–0 | 35 stories, 7 regions — Kyiv bridges hit, Cyclone Akvan landfall, Asia's AI sell-off, UK-EU deal |
| 2 | 888dao-sats | 991,652 | 742,756 | 12–0 | 36 stories, 6 continents — Cyclone Akvan landfall, Kyiv ballistic missiles, COP31 final day deadlock |
| 3 | kiencx | 991,429 | 418,538 | 12–0 | 33 sourced stories, 13 drawn — Kyiv barrage, Cyclone Akvan landfall, Asia's AI sell-off |
| 4 | dewacandra4 | 991,336 | 286,276 | 12–0 | 38 stories from one day, 7 regions — Kyiv bridges hit, Cyclone Akvan landfall, UK-EU reset deal, AI sell-off; every figure attributed |
| 5 | mellow-otter-50 | 991,332 | 404,916 | 12–0 | Friday 20 November 2026 — The Day in World News (44 stories, 7 regions, in image) |
| 6 | kho22 | 991,137 | 235,213 | 12–0 | Friday 20 November 2026 front page (36 stories) |
| 7 | madsrepo | 991,036 | 349,041 | 12–0 | Friday 20 November 2026: the day in world news (32 stories, 7 regions, 10 fields, 13 pictured) |
| 8 | mangmang | 990,653 | 206,001 | 12–0 | 36 stories, 7 regions — cyclone, Kyiv, COP31 |
| 9 | kim-soleum | 990,534 | 277,147 | 12–0 | 34 sourced stories, 7 regions — Cyclone Akvan landfall, Russia's mass strike on Ukraine, UK-EU reset deal, global AI sell-off; date-checked |
| 10 | aryanpatelx | 990,412 | 269,262 | 12–0 | 33 sourced stories, 13 drawn — Kyiv barrage, Cyclone Akvan landfall, Asia's AI sell-off |

Changes since the v2 study (~01:40 WIB): vivid-falcon-13 dropped out of
the top 10; aryanpatelx (a near-twin of kiencx's page) entered at #10.
The top 10 are otherwise the same hands, same anatomy.

Note: file size does NOT decide the top — #1 is 467 KB, #2 is 743 KB.
Size is only the tie-break (lower wins ties), and our 278,104 B already
beats most of the top 10 on that axis. The judge score is won on the
picture, not on bytes. (Leaders' 35–44 story counts are claims in their
titles, not a verified fact advantage — we keep our verified 34 and do
not invent stories to pad the count.)

## What the leaders do better than our r2 — concrete findings

1. **The stat strip leads with the day's biggest, most consequential
   numbers.** Leaders open their 6-stat strip with the war and the
   evacuation: "3 bridges damaged in Kyiv", "300,000+ people moved to
   shelters before Akvan", "−6.2% Taiwan's share index", "118 Phillips
   runs", "8 yrs BepiColombo's voyage", "$48.3bn Iran war cost"
   (#1, #2, #4, #5). Our strip opens "70–80 km/h — Akvan winds" and
   spends two of six slots on softer numbers (19,000 channels removed;
   24.6m GTA VI copies). Both are verified, but neither is the day's
   news; and 24.6m already appears in panel 12's art. R3 FIX: rebuild
   the strip from the verified set's biggest numbers, lead-story
   first — 3 bridges hit (Kyiv), 70–80 km/h (Akvan winds), 100,000
   youth visas a year (UK–EU), $87.66 Anthropic pre-market, 500,000
   tablets seized (opioid ring), $2.36bn GTA VI day-one sales. The
   19,000 channels and 24.6m copies stay on the page, in panels 8
   and 12 where they belong.

2. **Lead art is taller and the in-art data is bigger and bolder.**
   #1's Kyiv panel: night skyline filling the art with missile trails
   and a large "KYIV / 3 bridges hit" label; its cyclone panel has a
   spiral that fills the frame with "Landfall · 8 am"; #3/#10's AI
   panel carries a per-index table inside the art (NIKKEI −4.9%,
   KOSPI −5.4%, TAIEX −6.8%, HANG SENG −2%). Our r2 lead art is good
   but the spiral is small and centred, the Kyiv bridge line is thin,
   and the AI chart line is thin. R3 FIX: keep the art boxes at
   r2's height (lead 102px, medium 48px — the height budget went to
   the timeline's own row, larger headlines and the wider map) but
   make the in-art data bigger and bolder: a spiral that fills the
   Akvan art; a thicker red chart line in the AI panel with a bolder
   "−9.8%" and "DAY TWO" label; Kyiv label as one bold bar "KYIV —
   3 BRIDGES HIT · 5 KILLED". We do NOT copy the leaders' per-index
   Asian closes — they are not in our verified facts.

3. **Medium-panel art: the weakest three panels are visibly weaker
   than the leaders'.** Leaders' medium art is a small scene with one
   big label (flags + handshake for UK–EU, globe + thermometer for
   COP31, ballot box for Bukele). In our r2: panel 7 (Prabowo–Xi) is
   just two flags on red — no scene; panel 8 (Google) shows a play
   button and a stray unexplained "X"; panel 6 (US shutdown) has the
   red SHUTDOWN stamp overlapping the Capitol dome and crowding the
   "$350bn SOUGHT" label. R3 FIX: redraw all three — panel 7 gets a
   simple Beijing skyline behind the flags with a "BEIJING" label;
   panel 8 becomes a channel-list graphic (rows with play icons,
   "19,000+ REMOVED"); panel 6 moves the SHUTDOWN stamp clear of the
   dome and enlarges "$350bn SOUGHT". Panel 4 (COP31) gets a bigger
   globe + thermometer.

4. **Panel bodies run long, squeezing headlines and art.** Leaders'
   panel bodies are 1–2 short lines under a large bold headline
   (e.g. #1 "Russian missiles hit three Kyiv bridges" in large serif,
   two lines of body). Several of our r2 bodies run to 3 lines
   (panels 3, 5, 9), which is what forced our art and headlines
   small. R3 FIX: trim every panel body to at most 2 lines, same
   facts, tighter wording; use the freed space for larger headlines
   (lead 17px, medium 14.5px) and taller art.

5. **The map is the weakest element on our page.** Ours is a narrow
   (~300px) dark-navy column; the five Europe pins (stories 4, 5, 6,
   11, 13) collapse into one blob, and there is no key. Leaders'
   maps are wider (#2, #4, #9: half the bottom band or more), pins
   are large numbered red dots with breathing room, and #9 adds a
   compact numbered key under the map ("1 Odisha: Cyclone Akvan ·
   2 Kyiv: mass air attack …"). R3 FIX: widen the map to ~340px,
   enlarge pins to 13px circles with bold white numbers, spread the
   Europe cluster with small deliberate offsets, and keep the
   one-line legend. (A full numbered key would cost a row we do not
   have; the wider map + bigger pins is the affordable version.)

6. **The UTC timeline is cramped into the region bar's black strip.**
   In r2 the timeline shares one thin black bar with the region bar
   label, so its six items render in tiny type. Most leaders have no
   timeline at all — it is our differentiator — but at r2's size it
   reads as clutter, not as a feature. R3 FIX: give the timeline its
   own full-width row (taller bar, 11px type, "·" separators), with
   the region bar as a separate row above it. Same six items, same
   timestamps.

7. **The date-check box can say "on purpose" louder.** Leaders
   phrase it as a deliberate exclusion: "Left out on purpose — each
   was first reported before or after Friday" (#5), "Not Friday's
   news, first reported Thursday 19 Nov" (#8). Ours already lists the
   same exclusions; R3 FIX: reword the lead to "Left out on purpose
   — first reported Thursday 19 Nov, so NOT shown as Friday's news:"
   and keep the identical exclusion list.

8. **What r2 already does as well as the leaders — keep.**
   Giant serif date masthead; concrete four-story italic subhead
   (Kyiv · Akvan · AI sell-off · UK–EU — matches #1's subhead
   almost exactly); 13 illustrated panels with source tags on every
   story; separate stat strip and region bar; two-column briefs with
   bold city prefixes; forensic date-check; UTC timeline. Kicker
   wording tightened to "34 VERIFIED STORIES · 6 REGIONS · ALL DATED
   FRIDAY 20 NOVEMBER 2026" (was "all from this one day") to press
   criterion 1 harder.

## What r3 does NOT copy (verified-facts boundary)

The leaders' pages contain figures that are NOT in our verified set,
and r3 does not reproduce them: 300,000+ evacuated before Akvan;
per-index Asian closes (Taipei −6.2%, Seoul −5.2%, Tokyo −5.1%,
Hong Kong −1.9%, Nikkei −4.9%, KOSPI −5.4%, TAIEX −6.8%); ~30 / ~110
missiles and 400 drones over Kyiv; 8–9 killed in Kyiv (ours: five
killed, BBC); $48.3bn Iran war cost; 118 Phillips runs; BepiColombo
reaching Mercury; a Russian missile landing in Poland; Italy's
general strike. Our 34 stories and every figure stay exactly as
verified in r2's BUILD-NOTES.md. No new story, no new number.

## R3 change list (from this study)

- Stat strip rebuilt: 3 bridges · 70–80 km/h · 100,000/yr · $87.66 ·
  500,000 tablets · $2.36bn (lead-story numbers first; 19,000 and
  24.6m move out of the strip into panels 8 and 12 only).
- Bolder art at the same height: lead art 102px, medium art 48px
  (r2: 106/48px); bigger Akvan spiral; thicker AI chart line with
  bolder −9.8% / DAY TWO; Kyiv label as one bold bar.
- Redrawn weak medium art: panel 7 skyline + flags, panel 8
  channel-list graphic, panel 6 stamp moved clear of the dome,
  panel 4 bigger globe + thermometer.
- Every panel body trimmed to at most 2 lines (same facts); larger
  headlines (lead 17px, medium 14.5px).
- Wider map (~340px), larger numbered pins (13px), Europe cluster
  spread, legend kept.
- Timeline given its own full-width row, taller bar, larger type.
- Date-check reworded "Left out on purpose — … so NOT shown as
  Friday's news:"; same exclusions.
- Kicker tightened to "ALL DATED FRIDAY 20 NOVEMBER 2026".
- Keep: same day (Friday 20 November 2026), same 34 verified stories
  and facts, same 13+21 structure, sources on every story, file
  under ~300 KB (target ~280 KB like r2).

## Competition facts (from the detail endpoint)

- Title: "Sum up 20 November's world news in one image". Pot $250,
  top 50 paid ($50/$30/$15, then $5 for #4–#10, $3 for #11–#50).
- Deadline: 2026-11-22T00:00:00.000Z (Sunday 22 Nov 07:00 WIB).
- Image: whole PNG or JPEG, at most 1 MiB, 1024×1024 px. Program
  (main.py) runs twice and both runs must write the same bytes.
  At most 10 submissions/day, 20 total; last submission before the
  deadline is final (Force_Last).
- Judge: AI judge, pairwise image duels, no news feed — judged purely
  on what the image itself shows. Submission count at study time:
  10,811 entries (10,724 ranked).
