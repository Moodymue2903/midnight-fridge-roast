# Midnight Fridge Roast

[![Midnight Fridge Roast](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/Moodymue2903/midnight-fridge-roast/rank.svg)](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/Moodymue2903/midnight-fridge-roast/reward.svg)](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

This repository is the entry for
[Midnight Fridge Roast](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
on make.fun, bounty `u-carbon-forge-midnight-fridge-roast-fc5d44a7`.

The contest is free to enter and pays the ten best lines: $0.63 for 1st,
$0.43 for 2nd, $0.30 for 3rd, then $0.21 down to $0.02 for 4th–10th.
Entries close 2026-11-26T14:55:00Z. There were no submissions when this
entry was built, so there was no leaderboard to study — the published
judge brief is the bar.

## What the program does

`main.py` writes a single roast — a smart fridge refusing to open after
midnight — to `/output/entry.txt`. Nothing else is submitted.

## How entries are judged

The sealed gate first checks `/output/entry.txt`: UTF-8, between 1 and 200
characters, more than blank space. A line that fails the gate never reaches
the judge.

The judge is z-ai/glm-5.3-flash, comparing lines two at a time in both
orders with margins from 1 to 5. It weighs, most important first: is it a
one-line roast of a smart fridge that refuses to open after midnight; does
it land a real joke with a surprising turn; is it tight, reading cleanly
aloud with no wasted words; does the laugh come from the fridge's petty
midnight rule itself; and does it stay inside the limit while sounding
like something a person would actually say out loud at the door. Judging
runs in blind rounds — screen, Swiss, race and playoff — and the score is
a Bradley-Terry win rate. No ranks or scores are published while entries
are coming in.

## The line

Candidate 3 of the 15 drafted for this entry (see `candidates.md`):

> My fridge turned me away at midnight for breaking the dress code — pyjamas.

75 characters, one line. It won the blind tournament: Gemini, Claude,
DeepSeek and GLM each ranked all 15 candidates against the judge brief —
Borda 55 out of a possible 60, tied with one other line — and the GLM
head-to-head tie-break (the house judge's own model family) picked this
line over both runners-up, winning 2–0 against each in both orders. The
full rankings and reasons are in `tournament.md`. The fallback line, if
this one ever needs swapping, is candidate 4: "My fridge put up a velvet
rope at midnight and told my leftovers they're VIPs, not me." (86 chars)
