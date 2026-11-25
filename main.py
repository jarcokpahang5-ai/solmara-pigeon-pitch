"""Pigeon Pitch, One Line — make.fun bounty entry (u-donrulezz-pigeon-pitch-one-line-af06c6cf).

A scrappy city pigeon pitches CrumbDrop, its startup that turned dropped
street fries into a same-day delivery empire. The joke lands on the
pigeon's leverage: "seed us" is both the seed round and literal birdseed —
invest in the bird, or the bird keeps investing in your Tesla's paint job.

Pure Python 3.13 standard library only. Deterministic, no network.
Writes the single entry line to /output/entry.txt (and to output/entry.txt
as a best effort) and prints it to stdout, byte-identical to the file.
"""

ENTRY = (
    "Coo-founder of CrumbDrop: I turned your dropped fries into a same-day delivery empire — seed us, or I keep pooping on your Tesla."
)


def main() -> None:
    text = ENTRY
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
        except OSError:
            pass
    print(text, end="")


if __name__ == "__main__":
    main()
