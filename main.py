"""Write the one-line AI excuse for breaking production to /output/entry.txt."""

import os

ENTRY = "The good news: the deploy only took four seconds. The bad news: so did the outage."


def main() -> None:
    # Gate: entry must be a single line of 1-180 characters.
    assert 1 <= len(ENTRY) <= 180, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
