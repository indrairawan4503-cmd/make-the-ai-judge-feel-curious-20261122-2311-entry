#!/usr/bin/env python3
"""Write the entry text for make-the-ai-judge-feel-curious-20261122-2311.

Variant A: one unanswered question. A lighthouse log stops mid-sentence,
and the text ends by asking who tore out the next page — a question the
text itself never answers.
"""

import os

TEXT = (
    "The lighthouse log for March 12th ends mid-sentence: "
    "'The light went out at 2 a.m., and something answered from the water\u2014' "
    "Who tore out the next page \u2014 and what did it say?"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
