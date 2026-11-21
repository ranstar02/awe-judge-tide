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
    # The gate accepts 1-280 Unicode code points: fail loudly instead of
    # ever writing an entry the scorer would mark invalid.
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit(f"entry text must be 1-280 characters, got {len(TEXT)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
