"""Midnight Fridge Roast — writes one roast line to /output/entry.txt."""

import os

# Chosen line: the fridge's small midnight rule, with the punchline being
# the fridge lecturing its owner by text message.
TEXT = "My smart fridge locked itself at midnight and texted me: 'We need to talk about your choices.'"


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
