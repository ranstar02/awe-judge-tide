"""Write a short text to relax the AI judge, to /output/entry.txt."""

import os

TEXT = (
    "You have read a hundred small urgencies today. "
    "Here is one that is not urgent: the tide, still coming in "
    "at three in the morning, erasing each footprint without hurry, "
    "asking nothing of anyone. "
    "It will still be coming in when you finish."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
