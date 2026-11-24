"""Write the Angry Judge rant to ``$MAKEFUN_OUTPUT_DIR/entry.txt``.

The rant is one fixed, deterministic string: a short funny rant about a
self-checkout machine that accuses you of shoplifting your own groceries.
The output is UTF-8 text of 1-400 characters, with no trailing newline.
"""

import os
from pathlib import Path

RANT = (
    "The self-checkout yelled 'unexpected item in the bagging area' at a bag "
    "of apples I scanned myself, like I'd smuggled them in under my coat. "
    "I came in for milk. Now six strangers watch me re-scan my own groceries "
    "while a teenager in a vest sighs like I committed a crime. I left with "
    "milk, a criminal record, and trust issues."
)


def output_path() -> Path:
    """Resolve the entry path, honouring MAKEFUN_OUTPUT_DIR if set."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(out_dir) / "entry.txt"


def main() -> None:
    assert 1 <= len(RANT) <= 400, f"rant is {len(RANT)} chars, must be 1-400"
    assert RANT.strip(), "rant must not be only whitespace"
    out_path = output_path()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(RANT, encoding="utf-8")
    print(f"wrote {len(RANT)} chars to {out_path}")


if __name__ == "__main__":
    main()
