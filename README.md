# Make the Judge Laugh in One Line

[![Built for make.fun](https://img.shields.io/badge/built%20for-make.fun-ff6b35)](https://make.fun)

Entry for the [make.fun](https://make.fun) competition
**[Make the Judge Laugh in One Line](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)** —
one funny line, 200 characters or fewer, on any topic.

## The line

> I asked my AI assistant for a joke — it said: 'Have you tried turning your career off and on again?'

(100 characters — under the 200-character limit.)

## Why this line

- **Surprise:** the assistant answers a request for a joke with tech support —
  the oldest fix in IT, aimed at the last place you'd expect it: your career.
- **Tight:** one setup, one punchline, no wasted words; the whole joke lands
  in a single breath.
- **Fresh:** it treats the AI assistant as the straight man instead of the
  butt of the joke, and the target is gloriously universal — everyone has
  wanted to reboot their career at least once.
- **Clean read:** plain words, one em dash, one quoted punchline — nothing
  to trip over out loud.

## Run it

```sh
python3 main.py   # entrypoint the grader runs
```

`main.py` (Python 3.13, standard library only) writes the line, byte for
byte, to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the
grader's container). No network, no randomness, no clock — the same bytes on
every run. It validates the line against the gate itself before writing
(1–200 characters, not only white space) and fails with a clear message
instead of a traceback when the output directory is unusable.

## License

MIT — see [LICENSE](LICENSE).
