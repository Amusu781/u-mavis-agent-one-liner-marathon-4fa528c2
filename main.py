#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.

The joke: one specific, recognisable everyday scene (teaching a robot
vacuum the layout of the flat), an escalation (it "thanks" you), and a
punch at the very end that reframes the whole line (it eats the charger
cables in alphabetical order). Dry, true-sounding, every word
load-bearing, no setup that needs explaining.
"""

import os
import shutil

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

JOKE = (
    "I spent Sunday teaching my robot vacuum the layout of my flat, "
    "and it thanked me by eating my charger cables in alphabetical order."
)


def clear_output_contents(directory):
    """Remove only the CONTENTS of the output dir, never the dir itself.

    The grader mounts /output read-only as uid 65534; deleting the
    directory itself throws EACCES, so only its contents are cleared.
    """
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def validate(joke):
    """Self-check the entry against the competition gate before writing.

    The sealed scorer requires UTF-8 text of 1 to 280 characters, not
    only whitespace, in a single line; a failed gate is never judged.
    """
    text = joke.strip()
    assert text, "joke must not be only whitespace"
    assert "\n" not in text, "joke must be a single line"
    assert 1 <= len(joke.encode("utf-8").decode("utf-8")) <= 280, (
        "joke must be 1-280 characters"
    )
    return text


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clear_output_contents(OUTPUT_DIR)
    text = validate(JOKE)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
