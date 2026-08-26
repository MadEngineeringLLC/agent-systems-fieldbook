#!/usr/bin/env python3
"""Validate repository metadata, invariants, provenance, and generated indexes."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

from fieldbook import (
    ROOT,
    FrontMatterError,
    artifact_files,
    calculate_weighted_score,
    journal_files,
    journal_record,
    load_json,
    load_yaml,
    parse_front_matter,
    scoring_schema,
    taxonomy,
)

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "LICENSE",
    "NOTICE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "GOVERNANCE.md",
    "SUPPORT.md",
    "ROADMAP.md",
    "CHANGELOG.md",
    "CITATION.cff",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/dependabot.yml",
    ".github/workflows/validate.yml",
    "meta/evaluation-rubric.md",
    "meta/scoring-schema.yaml",
    "meta/taxonomy.md",
    "meta/taxonomy.yaml",
    "meta/provenance-policy.md",
    "meta/rejection-policy.md",
    "meta/deduplication-policy.md",
    "meta/self-improvement-policy.md",
    "schemas/artifact.schema.json",
    "schemas/evaluation.schema.json",
    "schemas/journal.schema.json",
    "skills/hardened-candidate-evaluator/SKILL.md",
    "automation/grok-bot/fieldbook-steward-system-prompt.md",
    "automation/grok-bot/first-run.md",
    "catalog/artifacts.jsonl",
    "catalog/artifacts.csv",
]

SECRET_PATTERNS: dict[str, re.Pattern[str]] = {
    "private key": re.compile(
        r"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----"
    ),
    "GitHub fine-grained token": re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    "GitHub legacy token": re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    "AWS access key": re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
}

TEXT_SUFFIXES = {
    "",
    ".cff",
    ".csv",
    ".json",
    ".jsonl",
    ".md",
    ".py",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}


class Report:
    """Collect deterministic validation outcomes."""

    def __init__(self) -> None:
        self.checks = 0
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def check(self, condition: bool, message: str) -> None:
        self.checks += 1
        if not condition:
            self.errors.append(message)

    def error(self, message: str) -> None:
        self.checks += 1
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)


def _json_path(error: Any) -> str:
    parts = [str(part) for part in error.absolute_path]
    return ".".join(parts) if parts else "<root>"


def _validate_schema(
    report: Report, instance: Any, schema_path: Path, source_path: Path
) -> None:
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda item: list(item.absolute_path))
    report.checks += 1
    for error in errors:
        report.errors.append(
            f"{source_path.relative_to(ROOT)}:{_json_path(error)}: {error.message}"
        )


def _validate_required_files(report: Report) -> None:
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        report.check(path.is_file(), f"missing required file: {relative}")
        if path.is_file():
            report.check(path.stat().st_size > 0, f"required file is empty: {relative}")


def _validate_parseable_files(report: Report) -> None:
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        relative = path.relative_to(ROOT)
        try:
            if path.suffix in {".yaml", ".yml", ".cff"}:
                with path.open("r", encoding="utf-8") as handle:
                    yaml.safe_load(handle)
                report.checks += 1
            elif path.suffix == ".json":
                load_json(path)
                report.checks += 1
            elif path.suffix == ".jsonl":
                for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                    if not line.strip():
                        continue
                    try:
                        value = json.loads(line)
                    except json.JSONDecodeError as exc:
                        report.error(f"{relative}:{number}: invalid JSONL: {exc}")
                        continue
                    report.check(
                        isinstance(value, dict),
                        f"{relative}:{number}: each JSONL line must be an object",
                    )
        except (OSError, UnicodeDecodeError, yaml.YAMLError, json.JSONDecodeError) as exc:
            report.error(f"{relative}: parse failure: {exc}")



def _validate_citation(report: Report) -> None:
    path = ROOT / "CITATION.cff"
    try:
        data = load_yaml(path)
    except (OSError, yaml.YAMLError) as exc:
        report.error(f"CITATION.cff: cannot parse: {exc}")
        return
    report.check(isinstance(data, dict), "CITATION.cff: root must be a mapping")
    if not isinstance(data, dict):
        return
    for key in ("cff-version", "message", "title", "authors"):
        report.check(key in data, f"CITATION.cff: missing required field {key!r}")
    report.check(str(data.get("cff-version")) == "1.2.0", "CITATION.cff: cff-version must be 1.2.0")
    report.check(data.get("type", "software") in {"software", "dataset"}, "CITATION.cff: type must be software or dataset")
    authors = data.get("authors", [])
    report.check(isinstance(authors, list) and bool(authors), "CITATION.cff: authors must be a non-empty list")
    if isinstance(authors, list):
        for index, author in enumerate(authors):
            valid = isinstance(author, dict) and (
                bool(author.get("name"))
                or (bool(author.get("family-names")) and bool(author.get("given-names")))
            )
            report.check(valid, f"CITATION.cff: author {index} needs name or family-names/given-names")

def _validate_text_hygiene(report: Report) -> None:
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or path.suffix not in TEXT_SUFFIXES:
            continue
        relative = path.relative_to(ROOT)
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        report.check("\x00" not in text, f"{relative}: contains NUL bytes")
        report.check("\r" not in text, f"{relative}: contains CR line endings")
        for number, line in enumerate(text.splitlines(), 1):
            if line.endswith((" ", "\t")):
                report.error(f"{relative}:{number}: trailing whitespace")
        if text and not text.endswith("\n"):
            report.error(f"{relative}: missing terminal newline")


def _validate_secret_absence(report: Report) -> None:
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or path.suffix not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                report.error(f"{path.relative_to(ROOT)}: possible {label} detected")


def _expected_folder_map() -> dict[str, str]:
    return {
        artifact_type: str(spec["folder"])
        for artifact_type, spec in taxonomy(ROOT)["primary_types"].items()
    }


def _date_order_valid(data: dict[str, Any]) -> bool:
    try:
        created = date.fromisoformat(data["created_at"])
        updated = date.fromisoformat(data["updated_at"])
        verified = date.fromisoformat(data["last_verified_at"])
    except (KeyError, TypeError, ValueError):
        return False
    return created <= updated and created <= verified


def _validate_artifacts(report: Report) -> list[dict[str, Any]]:
    schema_path = ROOT / "schemas" / "artifact.schema.json"
    scoring = scoring_schema(ROOT)
    folders = _expected_folder_map()
    known_namespaces = set(taxonomy(ROOT).get("tag_namespaces", {}))
    known_risks = {
        risk
        for severity in ("critical", "high", "moderate")
        for risk in scoring["risk_flags"][severity]
    }
    critical_risks = set(scoring["risk_flags"]["critical"])
    records: list[dict[str, Any]] = []
    ids: Counter[str] = Counter()
    slugs: Counter[str] = Counter()
    source_keys: Counter[tuple[Any, ...]] = Counter()

    for path in artifact_files(ROOT):
        relative = path.relative_to(ROOT)
        try:
            data, body = parse_front_matter(path)
        except FrontMatterError as exc:
            report.error(str(exc))
            continue

        records.append(data)
        _validate_schema(report, data, schema_path, path)
        report.check(
            bool(body.strip()),
            f"{relative}: artifact body must not be empty",
        )
        report.check(
            body.lstrip().startswith("# "),
            f"{relative}: artifact body must begin with one H1 heading",
        )
        artifact_type = data.get("artifact_type")
        expected_folder = folders.get(str(artifact_type))
        report.check(
            expected_folder is not None,
            f"{relative}: unknown artifact type {artifact_type!r}",
        )
        if expected_folder:
            report.check(
                relative.as_posix().startswith(expected_folder + "/"),
                f"{relative}: type {artifact_type!r} belongs under {expected_folder}/",
            )

        artifact_id = str(data.get("id", ""))
        slug = str(data.get("slug", ""))
        ids[artifact_id] += 1
        slugs[slug] += 1
        source = data.get("source", {})
        source_key = (
            source.get("url"),
            source.get("repository"),
            source.get("path"),
            source.get("commit_sha"),
        )
        source_keys[source_key] += 1

        evaluation = data.get("evaluation", {})
        scores = evaluation.get("scores", {})
        try:
            expected_score = calculate_weighted_score(scores, ROOT)
        except (KeyError, TypeError, ValueError) as exc:
            report.error(f"{relative}: cannot calculate weighted score: {exc}")
        else:
            report.check(
                evaluation.get("weighted_score") == expected_score,
                f"{relative}: weighted_score is {evaluation.get('weighted_score')!r}; expected {expected_score:.2f}",
            )

        report.check(
            evaluation.get("rubric_version") == scoring["rubric_version"],
            f"{relative}: rubric version does not match meta/scoring-schema.yaml",
        )
        report.check(
            _date_order_valid(data),
            f"{relative}: dates must satisfy created_at <= updated_at and last_verified_at",
        )
        report.check(
            data.get("provenance", {}).get("source_preserved") is True,
            f"{relative}: source_preserved must be true",
        )
        report.check(
            data.get("provenance", {}).get("credit_preserved") is True,
            f"{relative}: credit_preserved must be true",
        )

        tags = data.get("tags", [])
        for tag in tags:
            namespace = tag.split(":", 1)[0]
            report.check(
                namespace in known_namespaces,
                f"{relative}: unknown tag namespace in {tag!r}",
            )
        evidence_level = data.get("evidence", {}).get("level")
        report.check(
            f"evidence:{evidence_level}" in tags,
            f"{relative}: tags must include evidence:{evidence_level}",
        )

        risk_flags = evaluation.get("risk_flags", [])
        for risk in risk_flags:
            report.check(risk in known_risks, f"{relative}: unknown risk flag {risk!r}")

        if data.get("status") == "accepted":
            report.check(
                evaluation.get("disposition") == "accept",
                f"{relative}: accepted artifact must have accept disposition",
            )
            report.check(
                float(evaluation.get("weighted_score", 0))
                >= float(scoring["dispositions"]["accept"]["weighted_minimum"]),
                f"{relative}: accepted artifact is below weighted acceptance threshold",
            )
            for dimension, spec in scoring["dimensions"].items():
                minimum = int(spec["accept_minimum"])
                report.check(
                    int(scores.get(dimension, 0)) >= minimum,
                    f"{relative}: {dimension} is below acceptance minimum {minimum}",
                )
            report.check(
                not (set(risk_flags) & critical_risks),
                f"{relative}: accepted artifact has unresolved critical risk",
            )
            report.check(
                data.get("license", {}).get("status") in {"verified", "declared", "not-applicable"},
                f"{relative}: accepted artifact has unresolved license status",
            )

    for artifact_id, count in ids.items():
        report.check(count == 1, f"duplicate artifact id {artifact_id!r} appears {count} times")
    for slug, count in slugs.items():
        report.check(count == 1, f"duplicate artifact slug {slug!r} appears {count} times")
    for key, count in source_keys.items():
        report.check(
            count == 1,
            f"duplicate source identity appears {count} times: {key!r}",
        )

    report.check(bool(records), "no artifact entries discovered")
    return records



def _evaluation_files() -> list[Path]:
    files: list[Path] = []
    for folder in ("accepted", "watch", "rejected", "quarantined"):
        root = ROOT / "evaluations" / folder
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            if path.name != "README.md":
                files.append(path)
    return sorted(files, key=lambda path: path.as_posix())


def _validate_evaluations(report: Report, artifact_ids: set[str]) -> int:
    schema_path = ROOT / "schemas" / "evaluation.schema.json"
    scoring = scoring_schema(ROOT)
    folder_disposition = {
        "accepted": "accept",
        "watch": "watch",
        "rejected": "reject",
        "quarantined": "quarantine",
    }
    known_risks = {
        risk
        for severity in ("critical", "high", "moderate")
        for risk in scoring["risk_flags"][severity]
    }
    required_sections = [
        "## Executive assessment",
        "## Stealable mechanism",
        "## Mechanism and context",
        "## Evidence",
        "## Safety review",
        "## Improvements",
        "## Attribution",
        "## Facts, inferences, and unknowns",
        "## Archive action",
    ]
    count = 0
    for path in _evaluation_files():
        count += 1
        relative = path.relative_to(ROOT)
        try:
            data, body = parse_front_matter(path)
        except FrontMatterError as exc:
            report.error(str(exc))
            continue
        _validate_schema(report, data, schema_path, path)
        report.check(body.lstrip().startswith("# Evaluation:"), f"{relative}: body must begin with '# Evaluation:'")
        for heading in required_sections:
            report.check(heading in body, f"{relative}: missing required section {heading!r}")

        scores = data.get("scores", {})
        try:
            expected_score = calculate_weighted_score(scores, ROOT)
        except (KeyError, TypeError, ValueError) as exc:
            report.error(f"{relative}: cannot calculate evaluation score: {exc}")
        else:
            report.check(
                data.get("weighted_score") == expected_score,
                f"{relative}: weighted_score is {data.get('weighted_score')!r}; expected {expected_score:.2f}",
            )

        folder = relative.parts[1]
        expected_disposition = folder_disposition[folder]
        actual_disposition = data.get("decision", {}).get("disposition")
        report.check(
            actual_disposition == expected_disposition,
            f"{relative}: folder requires {expected_disposition!r}, got {actual_disposition!r}",
        )

        for risk in data.get("risks", []):
            flag = risk.get("flag")
            report.check(flag in known_risks, f"{relative}: unknown risk flag {flag!r}")

        if actual_disposition == "accept":
            gates = data.get("gates", {})
            for gate in scoring["dispositions"]["accept"]["required_gates"]:
                report.check(gates.get(gate) is True, f"{relative}: accept gate {gate!r} is not true")
            report.check(
                float(data.get("weighted_score", 0)) >= float(scoring["dispositions"]["accept"]["weighted_minimum"]),
                f"{relative}: accepted evaluation is below threshold",
            )
            candidate_id = data.get("candidate", {}).get("candidate_id")
            report.check(
                candidate_id in artifact_ids,
                f"{relative}: accepted evaluation candidate {candidate_id!r} has no accepted artifact",
            )
            archive_target = data.get("archive_target")
            report.check(
                isinstance(archive_target, str) and archive_target.startswith("artifacts/"),
                f"{relative}: accepted evaluation must target artifacts/",
            )
    return count

def _validate_journal(report: Report, artifact_ids: set[str]) -> None:
    schema_path = ROOT / "schemas" / "journal.schema.json"
    expected_records: list[dict[str, Any]] = []
    ids: Counter[str] = Counter()
    for path in journal_files(ROOT):
        try:
            data, body = parse_front_matter(path)
        except FrontMatterError as exc:
            report.error(str(exc))
            continue
        _validate_schema(report, data, schema_path, path)
        report.check(bool(body.strip()), f"{path.relative_to(ROOT)}: journal body is empty")
        ids[str(data.get("id", ""))] += 1
        for artifact_id in data.get("artifact_ids", []):
            report.check(
                artifact_id in artifact_ids,
                f"{path.relative_to(ROOT)}: unknown artifact id {artifact_id!r}",
            )
        try:
            start = date.fromisoformat(data["period_start"])
            end = date.fromisoformat(data["period_end"])
        except (KeyError, TypeError, ValueError):
            pass
        else:
            report.check(start <= end, f"{path.relative_to(ROOT)}: period_start is after period_end")
        expected_records.append(journal_record(path, ROOT))

    for journal_id, count in ids.items():
        report.check(count == 1, f"duplicate journal id {journal_id!r}")

    index_path = ROOT / "journal" / "index.jsonl"
    actual_records: list[dict[str, Any]] = []
    if index_path.is_file():
        for line in index_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                actual_records.append(json.loads(line))
    expected_sorted = sorted(expected_records, key=lambda item: (item["period_end"], item["id"]))
    actual_sorted = sorted(actual_records, key=lambda item: (item["period_end"], item["id"]))
    report.check(
        actual_sorted == expected_sorted,
        "journal/index.jsonl is stale or inconsistent with journal front matter",
    )


def _validate_taxonomy_folders(report: Report) -> None:
    primary_types = taxonomy(ROOT)["primary_types"]
    folders: Counter[str] = Counter()
    for artifact_type, spec in primary_types.items():
        folder = str(spec["folder"])
        folders[folder] += 1
        path = ROOT / folder
        report.check(path.is_dir(), f"taxonomy folder missing for {artifact_type}: {folder}")
        report.check(
            (path / "README.md").is_file(),
            f"taxonomy folder lacks README.md: {folder}",
        )
    for folder, count in folders.items():
        report.check(count == 1, f"taxonomy maps multiple primary types to {folder}")


def _validate_placeholders(report: Report, strict: bool) -> None:
    matches: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if (
            not path.is_file()
            or ".git" in path.parts
            or "scripts" in path.relative_to(ROOT).parts
            or path.suffix not in TEXT_SUFFIXES
        ):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "YOUR_GITHUB_HANDLE" in text:
            matches.append(path.relative_to(ROOT).as_posix())
    if matches:
        message = (
            "repository owner placeholder remains in: " + ", ".join(matches)
            + "; run scripts/configure_repo.py before publishing"
        )
        if strict:
            report.error(message)
        else:
            report.warning(message)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict-placeholders",
        action="store_true",
        help="treat unreplaced repository-owner placeholders as errors",
    )
    args = parser.parse_args()

    report = Report()
    _validate_required_files(report)
    _validate_parseable_files(report)
    _validate_citation(report)
    _validate_text_hygiene(report)
    _validate_secret_absence(report)
    _validate_taxonomy_folders(report)
    artifacts = _validate_artifacts(report)
    artifact_ids = {str(item.get("id")) for item in artifacts}
    evaluation_count = _validate_evaluations(report, artifact_ids)
    _validate_journal(report, artifact_ids)
    _validate_placeholders(report, args.strict_placeholders)

    for warning in report.warnings:
        print(f"WARNING: {warning}")
    for error in report.errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if report.errors:
        print(
            f"Validation failed: {len(report.errors)} error(s), "
            f"{len(report.warnings)} warning(s), {report.checks} checks",
            file=sys.stderr,
        )
        return 1

    print(
        f"Validation passed: {len(artifacts)} artifacts, {evaluation_count} evaluation records, "
        f"{len(report.warnings)} warning(s), {report.checks} checks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
