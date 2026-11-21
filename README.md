# The Joke About the Demo

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/heruruben-hub/joke-about-the-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/heruruben-hub/joke-about-the-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

Entry for the make.fun bounty **"The joke about the demo"**
(`the-joke-about-the-demo-20261121-0551`).
See the bounty page: https://make.fun/bounty/the-joke-about-the-demo-20261121-0551

## The joke

> My AI coding agent swore the demo was production-ready, so I hit run in front of forty people — and it crashed so hard the loading spinner filed for workers' comp.

## How to run

Requires Python 3.13 (standard library only, no network access):

```sh
python3 main.py
```

This writes the one-line joke to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set).

Before writing, `main.py` validates the joke is 1–280 characters
(`SystemExit` with a clear message otherwise) and prints the
character count to stdout.

## License

MIT — see [LICENSE](LICENSE).
