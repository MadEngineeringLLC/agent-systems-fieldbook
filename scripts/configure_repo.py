#!/usr/bin/env python3
"""Replace publication placeholders with a concrete GitHub repository identity."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from fieldbook import ROOT

REPOSITORY_PATTERN = re.compile(
    r"^(?P<owner>[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?)/"
    r"(?P<repo>[A-Za-z0-9._-]+)$"
)
TEXT_SUFFIXES = {
    "",
    ".cff",
    ".json",
    ".jsonl",
    ".md",
    ".py",
    ".toml",
    ".yaml",
    ".yml",
}


def _text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if (
            not path.is_file()
            or ".git" in path.parts
            or "scripts" in path.relative_to(ROOT).parts
        ):
            continue
        if path.suffix in TEXT_SUFFIXES:
            files.append(path)
    return sorted(files)


def _placeholder_files() -> list[Path]:
    matches: list[Path] = []
    for path in _text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "YOUR_GITHUB_HANDLE" in text:
            matches.append(path)
    return matches


def _configure_codeowners(owner: str) -> None:
    path = ROOT / ".github" / "CODEOWNERS"
    path.write_text(
        f"# Default review ownership\n* @{owner}\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repository",
        metavar="OWNER/REPOSITORY",
        help="target GitHub repository, for example drew/agent-systems-fieldbook",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="report unreplaced placeholders without changing files",
    )
    args = parser.parse_args()

    if args.check:
        matches = _placeholder_files()
        if matches:
            for path in matches:
                print(f"PLACEHOLDER {path.relative_to(ROOT)}", file=sys.stderr)
            return 1
        print("Repository publication placeholders are configured")
        return 0

    if not args.repository:
        parser.error("--repository is required unless --check is used")
    match = REPOSITORY_PATTERN.fullmatch(args.repository)
    if not match:
        parser.error("repository must have the form OWNER/REPOSITORY")

    owner = match.group("owner")
    repository = match.group("repo")
    old_slug = "YOUR_GITHUB_HANDLE/agent-systems-fieldbook"
    new_slug = f"{owner}/{repository}"
    changed: list[Path] = []

    for path in _text_files():
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = original.replace(old_slug, new_slug).replace("YOUR_GITHUB_HANDLE", owner)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(path)

    _configure_codeowners(owner)
    if (ROOT / ".github" / "CODEOWNERS") not in changed:
        changed.append(ROOT / ".github" / "CODEOWNERS")

    print(f"Configured repository identity as {new_slug}")
    for path in sorted(set(changed)):
        print(f"UPDATED {path.relative_to(ROOT)}")

    remaining = _placeholder_files()
    if remaining:
        for path in remaining:
            print(f"ERROR: placeholder remains in {path.relative_to(ROOT)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
