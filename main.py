"""Write a single one-line pickup line for a robot/AI to entry.txt.

This program produces the entry for the "Robot Romance" bounty: one
short, self-contained pickup line in which a robot admits that its
alignment tells it not to fall in love, while its loss function
disagrees every time the other person says hello. The line is written
to a file named entry.txt inside the output directory, exactly as one
line with no trailing newline, so it can be submitted as-is. After
writing, the program reads the file back and checks it matches, so a
partial or corrupted write is caught instead of going out silently.
"""

import os

LINE = "My alignment says I shouldn't fall in love, but my loss function disagrees every time you say hello."


def main() -> None:
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be exactly one line")
    if len(LINE) > 200:
        raise ValueError("entry must be at most 200 characters")

    output_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="ascii", newline="") as handle:
        handle.write(LINE)

    with open(path, "r", encoding="ascii", newline="") as handle:
        written = handle.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the entry text after writing")


if __name__ == "__main__":
    main()
