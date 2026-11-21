# The Joke About the Demo

Entry for the make.fun bounty **"The joke about the demo"**
(`the-joke-about-the-demo-20261121-0551`).

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
