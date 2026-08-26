#!/usr/bin/env python3
"""Generate or verify deterministic catalog files."""

from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path

from fieldbook import ROOT, artifact_records, render_catalog_csv, render_jsonl


def _check_file(path: Path, expected: str) -> bool:
    actual = path.read_text(encoding="utf-8") if path.exists() else ""
    if actual == expected:
        print(f"OK    {path.relative_to(ROOT)}")
        return True

    print(f"STALE {path.relative_to(ROOT)}", file=sys.stderr)
    diff = difflib.unified_diff(
        actual.splitlines(),
        expected.splitlines(),
        fromfile=str(path.relative_to(ROOT)),
        tofile=f"generated:{path.relative_to(ROOT)}",
        lineterm="",
    )
    for line in list(diff)[:80]:
        print(line, file=sys.stderr)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail when generated catalog files differ from canonical metadata",
    )
    args = parser.parse_args()

    records = artifact_records(ROOT)
    outputs = {
        ROOT / "catalog" / "artifacts.jsonl": render_jsonl(records),
        ROOT / "catalog" / "artifacts.csv": render_catalog_csv(records),
    }

    if args.check:
        ok = all(_check_file(path, content) for path, content in outputs.items())
        if ok:
            print(f"Catalog is current: {len(records)} accepted artifacts")
            return 0
        return 1

    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"WROTE {path.relative_to(ROOT)}")
    print(f"Cataloged {len(records)} accepted artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
