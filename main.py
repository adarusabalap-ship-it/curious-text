"""make.fun text contest entry."""

from pathlib import Path

TEXT = (
    "Every Thursday my neighbor waters a plant that is not there. She fills the can, "
    "crosses the yard, tips it over the bare square where a tree came out years ago, "
    "and goes back inside. Once I asked. She said the soil remembers the shape. "
    "The shape is thirsty."
)

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8", newline="")


if __name__ == "__main__":
    write_entry()
