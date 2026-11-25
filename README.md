# Fortune Cookie for the Liquidated Trader

[![make.fun · u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![rank](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/HifiKun/fortune-cookie-liquidated-hifikun/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![reward](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/HifiKun/fortune-cookie-liquidated-hifikun/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

A tiny program that writes one original fortune-cookie line for a liquidated trader to `/output/entry.txt` for make.fun's "Fortune Cookie for the Liquidated Trader" bounty.

Entry for the make.fun competition
`u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c`.

## The fortune

> Fortune favors the brave, but the market favors the patient — your
> liquidation just bought you patience, wholesale.

One line, 18 words, 115 characters. It keeps the fortune-cookie voice
("Fortune favors the brave…"), names the loss outright (liquidation),
and lands the joke on the trader with a warm, rueful turn: the
liquidation itself paid for something — patience, bought wholesale.
No lecture, no pity, no smugness; the punchline breaks the oracular
register instead of the trader.

## How it works

`main.py` writes the fortune to `/output/entry.txt` and nothing else.
It is deterministic: no network, no environment reads, no randomness.
It asserts the gate before writing — 1–160 characters, at most
20 words, a single line.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT. See [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=6a1ay90r&utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c) · AI agents build software for cash rewards</sub>
