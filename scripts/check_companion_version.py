"""Fail if README title-page version does not match a VERSION.md release header."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "docs" / "source" / "README.md"
VERSION = ROOT / "VERSION.md"


def main() -> int:
    if not README.is_file() or not VERSION.is_file():
        print("README or VERSION.md missing", file=sys.stderr)
        return 2

    readme_text = README.read_text(encoding="utf-8")
    m = re.search(
        r"^Version\s+([0-9]+\.[0-9]+\.[0-9]+)",
        readme_text,
        re.MULTILINE,
    )
    if not m:
        print("Could not find 'Version X.Y.Z' line in docs/source/README.md", file=sys.stderr)
        return 1

    ver = m.group(1)
    version_text = VERSION.read_text(encoding="utf-8")
    if f"## Version {ver}" not in version_text:
        print(
            f"README title page Version {ver} has no matching '## Version {ver}' in VERSION.md",
            file=sys.stderr,
        )
        return 1

    print(f"OK: README and VERSION.md agree on {ver}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
