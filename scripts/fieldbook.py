#!/usr/bin/env python3
"""Shared parsing and generation helpers for repository tooling."""

from __future__ import annotations

import csv
import io
import json
from pathlib import Path
from typing import Any, Iterable

import yaml

ROOT = Path(__file__).resolve().parents[1]


class FrontMatterError(ValueError):
    """Raised when a Markdown file does not contain valid YAML front matter."""


def load_yaml(path: Path) -> Any:
    """Load one YAML file using the safe loader."""
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_json(path: Path) -> Any:
    """Load one JSON file."""
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def parse_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    """Return YAML front matter and Markdown body from a UTF-8 file."""
    text = path.read_text(encoding="utf-8")
    normalized = text.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        raise FrontMatterError(f"{path}: missing opening YAML front-matter delimiter")

    end = normalized.find("\n---\n", 4)
    if end < 0:
        raise FrontMatterError(f"{path}: missing closing YAML front-matter delimiter")

    raw = normalized[4:end]
    try:
        parsed = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        raise FrontMatterError(f"{path}: invalid YAML front matter: {exc}") from exc

    if not isinstance(parsed, dict):
        raise FrontMatterError(f"{path}: front matter must be a mapping")

    return parsed, normalized[end + 5 :]


def taxonomy(root: Path = ROOT) -> dict[str, Any]:
    """Load the canonical taxonomy."""
    data = load_yaml(root / "meta" / "taxonomy.yaml")
    if not isinstance(data, dict):
        raise ValueError("meta/taxonomy.yaml must contain a mapping")
    return data


def scoring_schema(root: Path = ROOT) -> dict[str, Any]:
    """Load the canonical scoring configuration."""
    data = load_yaml(root / "meta" / "scoring-schema.yaml")
    if not isinstance(data, dict):
        raise ValueError("meta/scoring-schema.yaml must contain a mapping")
    return data


def artifact_files(root: Path = ROOT) -> list[Path]:
    """Discover artifact files from taxonomy folder mappings."""
    files: set[Path] = set()
    primary_types = taxonomy(root).get("primary_types", {})
    for spec in primary_types.values():
        folder = root / str(spec["folder"])
        if not folder.exists():
            continue
        for path in folder.rglob("*.md"):
            if path.name == "README.md":
                continue
            files.add(path)
    return sorted(files, key=lambda path: path.as_posix())


def journal_files(root: Path = ROOT) -> list[Path]:
    """Discover published journal entries, excluding templates and READMEs."""
    journal_root = root / "journal"
    files: list[Path] = []
    for path in journal_root.rglob("*.md"):
        if path.name == "README.md" or "templates" in path.parts:
            continue
        files.append(path)
    return sorted(files, key=lambda path: path.as_posix())


def calculate_weighted_score(
    scores: dict[str, int | float], root: Path = ROOT
) -> float:
    """Calculate the rubric-weighted score using the canonical weights."""
    dimensions = scoring_schema(root).get("dimensions", {})
    result = 0.0
    for name, spec in dimensions.items():
        if name not in scores:
            raise KeyError(f"missing score dimension: {name}")
        result += float(spec["weight"]) * float(scores[name])
    precision = int(scoring_schema(root)["weighted_score"]["precision"])
    return round(result, precision)


def artifact_record(path: Path, root: Path = ROOT) -> dict[str, Any]:
    """Build the concise canonical catalog record for one accepted artifact."""
    data, _ = parse_front_matter(path)
    evaluation = data["evaluation"]
    source = data["source"]
    license_data = data["license"]
    evidence = data["evidence"]
    return {
        "id": data["id"],
        "title": data["title"],
        "slug": data["slug"],
        "artifact_type": data["artifact_type"],
        "status": data["status"],
        "version": data["version"],
        "summary": data["summary"],
        "stealable_mechanism": data["stealable_mechanism"],
        "products": data["products"],
        "tags": data["tags"],
        "evidence_level": evidence["level"],
        "weighted_score": evaluation["weighted_score"],
        "risk_flags": evaluation["risk_flags"],
        "confidence": evaluation["confidence"],
        "source": {
            "type": source["type"],
            "title": source["title"],
            "author": source["author"],
            "url": source["url"],
            "published_at": source.get("published_at"),
            "captured_at": source["captured_at"],
            "repository": source.get("repository"),
            "path": source.get("path"),
            "commit_sha": source.get("commit_sha"),
        },
        "license": {
            "spdx": license_data["spdx"],
            "status": license_data["status"],
        },
        "created_at": data["created_at"],
        "updated_at": data["updated_at"],
        "last_verified_at": data["last_verified_at"],
        "path": path.relative_to(root).as_posix(),
    }


def artifact_records(root: Path = ROOT) -> list[dict[str, Any]]:
    """Build all accepted artifact catalog records in deterministic order."""
    records: list[dict[str, Any]] = []
    for path in artifact_files(root):
        data, _ = parse_front_matter(path)
        if data.get("status") == "accepted":
            records.append(artifact_record(path, root))
    return sorted(records, key=lambda record: (record["artifact_type"], record["id"]))


def journal_record(path: Path, root: Path = ROOT) -> dict[str, Any]:
    """Build the canonical journal-index record from front matter."""
    data, _ = parse_front_matter(path)
    fields = [
        "id",
        "period_start",
        "period_end",
        "published_at",
        "status",
        "sources_reviewed",
        "artifact_ids",
        "confidence",
    ]
    record = {field: data[field] for field in fields}
    record["path"] = path.relative_to(root).as_posix()
    return record


def render_jsonl(records: Iterable[dict[str, Any]]) -> str:
    """Render compact, key-sorted JSON Lines with a terminal newline."""
    lines = [
        json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        for record in records
    ]
    return "\n".join(lines) + ("\n" if lines else "")


def render_catalog_csv(records: list[dict[str, Any]]) -> str:
    """Render a stable review-oriented CSV view of artifact records."""
    fieldnames = [
        "id",
        "title",
        "artifact_type",
        "status",
        "version",
        "weighted_score",
        "evidence_level",
        "confidence",
        "products",
        "tags",
        "risk_flags",
        "source_type",
        "source_author",
        "source_url",
        "source_published_at",
        "license_spdx",
        "updated_at",
        "last_verified_at",
        "path",
        "stealable_mechanism",
    ]
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for record in records:
        writer.writerow(
            {
                "id": record["id"],
                "title": record["title"],
                "artifact_type": record["artifact_type"],
                "status": record["status"],
                "version": record["version"],
                "weighted_score": f'{record["weighted_score"]:.2f}',
                "evidence_level": record["evidence_level"],
                "confidence": record["confidence"],
                "products": "|".join(record["products"]),
                "tags": "|".join(record["tags"]),
                "risk_flags": "|".join(record["risk_flags"]),
                "source_type": record["source"]["type"],
                "source_author": record["source"]["author"],
                "source_url": record["source"]["url"],
                "source_published_at": record["source"]["published_at"] or "",
                "license_spdx": record["license"]["spdx"],
                "updated_at": record["updated_at"],
                "last_verified_at": record["last_verified_at"],
                "path": record["path"],
                "stealable_mechanism": record["stealable_mechanism"],
            }
        )
    return buffer.getvalue()
