"""A pigeon pitches its startup in exactly one line.

The bird in question runs CrumbDrop, a delivery service built on fries
nobody wanted anymore. The punchline is the threat folded into the ask:

This script keeps that one line safe: it checks the line is really one
line and within the allowed length, saves it to the output file the
judge reads, and echoes it to standard output with no extra newline.
"""

import os
import sys

# The pitch itself. One line, 129 characters, kept exactly as written.
PITCH = "Coo-founder of CrumbDrop: I turned your dropped fries into a same-day delivery empire — seed us, or I keep pooping on your Tesla."

MIN_LENGTH = 1
MAX_LENGTH = 200

# Where the judge looks first, then a local fallback next to this file.
OUTPUT_TARGETS = ("/output/entry.txt", "output/entry.txt")


def check_pitch(line):
    """Refuse anything that is not a single short line."""
    if not isinstance(line, str):
        raise TypeError("the pitch must be text")
    if "\n" in line or "\r" in line:
        raise ValueError("the pitch must fit on one line")
    if not MIN_LENGTH <= len(line) <= MAX_LENGTH:
        raise ValueError(
            "the pitch must be between %d and %d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(line))
        )


def save_pitch(line):
    """Write the pitch to each target that accepts it."""
    for target in OUTPUT_TARGETS:
        try:
            folder = os.path.dirname(target)
            if folder:
                os.makedirs(folder, exist_ok=True)
            with open(target, "w", encoding="utf-8") as handle:
                handle.write(line)
        except OSError:
            # A target we cannot reach is skipped; the other may work.
            continue


def run():
    check_pitch(PITCH)
    save_pitch(PITCH)
    sys.stdout.write(PITCH)


if __name__ == "__main__":
    run()
