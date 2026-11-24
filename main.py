"""Sick-day excuse entry: writes one line (<200 chars) to entry.txt.

The judge weighs: half believable, fresh idea, laugh lands near the end,
sounds like a real person texting their boss, no wasted words.
"""
import os

ENTRY = (
    "I pulled something in my shoulder opening a jar of pickles, "
    "and the jar is still sealed \u2014 I'm taking the loss and the day off."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
