# The World in One Day — Friday 20 November 2026: 34 verified stories

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/destama-ux/newsimg-1120-repo-r3/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/destama-ux/newsimg-1120-repo-r3/reward.svg)](https://make.fun/bounty/news-image-20261120)

One-page newspaper image summing up the world news of Friday
20 November 2026 — 34 verified stories: 13 illustrated panels
(Kyiv bridges hit, Cyclone Akvan landfall, the AI sell-off, COP31,
the UK–EU reset deal, and eight more) plus 21 one-line briefs, a UTC
timeline, a six-stat strip, a region bar, a world map, and a forensic
date-check box. Entry for the make.fun competition
`news-image-20261120` (revision r3). Every story on the page happened,
or was first reported, on Friday 20 November 2026; Thursday's news is
named in the date-check box as deliberately left out.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This validates `artwork.jpg` (JPEG, exactly 1024×1024, at most 1 MiB)
and copies it byte-for-byte to `out/entry.png`. Python 3 standard
library only; no network.

## Files

- `page.html` — the page the artwork was rendered from (fresh
  composition for r3; see `BUILD-NOTES.md`).
- `artwork.jpg` — the entry image, 1024×1024 JPEG, 287,639 bytes.
- `main.py` — validates `artwork.jpg` and writes it to
  `$MAKEFUN_OUTPUT_DIR/entry.png`.
- `BUILD-NOTES.md` — the r3 changes, the story list with sources,
  size, and verification.
- `STUDY.md` — leader study of the live top 10 and the r3 change list.

## License

MIT — see `LICENSE`.
