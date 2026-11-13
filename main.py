"""ai-joke-03 entry: writes one fixed one-liner to /output/entry.txt.

Deterministic by construction: a single fixed string, no clock,
no randomness, no network, no trailing newline (a line end counts
toward the 280-character limit, so none is written).
"""

import os
from pathlib import Path

JOKE = "My AI coding agent fixed the bug, then apologised for the other 47 bugs it introduced while fixing it."

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
