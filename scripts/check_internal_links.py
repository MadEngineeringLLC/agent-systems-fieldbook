#!/usr/bin/env python3
"""Check that repository-local Markdown links resolve to real paths and anchors."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

from fieldbook import ROOT

INLINE_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REFERENCE_LINK = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
SKIP_SCHEMES = {
    "data",
    "ftp",
    "http",
    "https",
    "mailto",
    "repo",
    "skills",
}


def _without_fenced_code(text: str) -> str:
    lines: list[str] = []
    in_fence = False
    marker = ""
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            current = stripped[:3]
            if not in_fence:
                in_fence = True
                marker = current
            elif current == marker:
                in_fence = False
                marker = ""
            lines.append("")
            continue
        lines.append("" if in_fence else line)
    return "\n".join(lines)


def _destination(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<") and ">" in raw:
        return raw[1 : raw.index(">")]
    # Markdown permits an optional quoted title after whitespace.
    match = re.match(r"([^\s]+)(?:\s+[\"'].*)?$", raw)
    return match.group(1) if match else raw


def _slugify_heading(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[`*_~]", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return text.replace(" ", "-")


def _anchors(path: Path) -> set[str]:
    if not path.is_file() or path.suffix.lower() != ".md":
        return set()
    text = _without_fenced_code(path.read_text(encoding="utf-8"))
    seen: Counter[str] = Counter()
    anchors: set[str] = set()
    for line in text.splitlines():
        match = HEADING.match(line)
        if not match:
            continue
        base = _slugify_heading(match.group(2))
        if not base:
            continue
        count = seen[base]
        seen[base] += 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


def _resolve(source: Path, destination: str) -> tuple[Path | None, str | None]:
    split = urlsplit(destination)
    if split.scheme.lower() in SKIP_SCHEMES:
        return None, None
    if split.netloc:
        return None, None

    raw_path = unquote(split.path)
    if raw_path:
        target = ROOT / raw_path.lstrip("/") if raw_path.startswith("/") else source.parent / raw_path
    else:
        target = source

    target = target.resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        return target, split.fragment or None
    return target, unquote(split.fragment) or None


def main() -> int:
    failures: list[str] = []
    checked = 0
    anchor_cache: dict[Path, set[str]] = {}

    for source in sorted(ROOT.rglob("*.md")):
        if ".git" in source.parts:
            continue
        text = _without_fenced_code(source.read_text(encoding="utf-8"))
        destinations = [match.group(1) for match in INLINE_LINK.finditer(text)]
        destinations.extend(match.group(1) for match in REFERENCE_LINK.finditer(text))

        for raw in destinations:
            destination = _destination(raw)
            if not destination or destination.startswith(("#", "{{", "${")):
                if destination.startswith("#"):
                    target = source
                    fragment = unquote(destination[1:])
                else:
                    continue
            else:
                target, fragment = _resolve(source, destination)
                if target is None:
                    continue

            checked += 1
            relative_source = source.relative_to(ROOT)
            assert target is not None
            if not target.exists():
                try:
                    rendered_target = target.relative_to(ROOT)
                except ValueError:
                    rendered_target = target
                failures.append(
                    f"{relative_source}: {destination!r} -> missing {rendered_target}"
                )
                continue

            if fragment:
                anchor_target = target / "README.md" if target.is_dir() else target
                if not anchor_target.is_file() or anchor_target.suffix.lower() != ".md":
                    failures.append(
                        f"{relative_source}: {destination!r} has anchor on non-Markdown target"
                    )
                    continue
                anchors = anchor_cache.setdefault(anchor_target, _anchors(anchor_target))
                normalized = _slugify_heading(fragment)
                if normalized not in anchors:
                    failures.append(
                        f"{relative_source}: {destination!r} -> missing anchor #{normalized}"
                    )

    for failure in failures:
        print(f"ERROR: {failure}", file=sys.stderr)
    if failures:
        print(
            f"Internal-link check failed: {len(failures)} broken link(s), {checked} checked",
            file=sys.stderr,
        )
        return 1
    print(f"Internal-link check passed: {checked} local link(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
