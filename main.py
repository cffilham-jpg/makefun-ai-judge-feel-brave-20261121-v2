import os
import sys
from pathlib import Path


TEXT = "The oar dips before the sun is up. Cold water, dark shore. You pull once, and the boat answers — slow, then sure. The mist lifts off the river in strips. By the second stroke your shoulders know the work. The far bank is still far. You row anyway."

def validate_text(text: str) -> None:
    if not text.strip():
        raise ValueError("entry text must not be empty")
    if not 1 <= len(text) <= 280:
        raise ValueError("entry text must contain 1-280 characters")


def write_entry(text: str, output_dir: Path) -> None:
    validate_text(text)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(text.encode("utf-8"))


def main() -> int:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        write_entry(TEXT, output_dir)
    except (ValueError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
