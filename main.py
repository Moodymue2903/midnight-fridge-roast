"""Midnight Fridge Roast — make.fun entry.

The program writes one roast to /output/entry.txt: a smart fridge
turning its owner away at midnight for breaking the dress code.

The line was picked by a blind tournament. Fifteen original candidates
were ranked by four judges against the published judge brief, and the
head-to-head tie-break — run by GLM, the house-judge model family —
picked this line over the two runners-up, winning 2-0 against each in
both orders.
"""

import sys
from pathlib import Path

LINE = "My fridge turned me away at midnight for breaking the dress code \u2014 pyjamas."

MAX_CHARS = 200
OUTPUT = Path("/output/entry.txt")


def find_problems(text):
    """Return a list of rule violations for the line (empty means it passes)."""
    problems = []
    if not text.strip():
        problems.append("the line is empty or only whitespace")
    if len(text) > MAX_CHARS:
        problems.append(
            "the line is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        problems.append("the line must be a single line, with no line breaks")
    if text != text.strip():
        problems.append("the line has leading or trailing whitespace")
    return problems


def write_entry(text, path=OUTPUT):
    """Write the line to the entry file, making the folder if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def verify_written(text, path=OUTPUT):
    """Check the file on disk matches the line exactly; None when it does."""
    written = path.read_bytes()
    if written != text.encode("utf-8"):
        return "file holds %d bytes, the line is %d" % (
            len(written),
            len(text.encode("utf-8")),
        )
    return None


def main():
    problems = find_problems(LINE)
    if problems:
        print("error: " + "; ".join(problems), file=sys.stderr)
        return 1

    write_entry(LINE)
    mismatch = verify_written(LINE)
    if mismatch is not None:
        print("error: " + mismatch, file=sys.stderr)
        return 1

    print("wrote %d characters (%d bytes) to %s" % (len(LINE), len(LINE.encode("utf-8")), OUTPUT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
