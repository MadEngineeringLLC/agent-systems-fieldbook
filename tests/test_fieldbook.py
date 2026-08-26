from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.fieldbook import (
    ROOT,
    FrontMatterError,
    artifact_files,
    artifact_records,
    calculate_weighted_score,
    journal_files,
    journal_record,
    parse_front_matter,
    render_catalog_csv,
    render_jsonl,
)


class FrontMatterTests(unittest.TestCase):
    def test_parse_front_matter(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "entry.md"
            path.write_text("---\nid: example\nitems:\n  - one\n---\n# Body\n", encoding="utf-8")
            metadata, body = parse_front_matter(path)
        self.assertEqual(metadata["id"], "example")
        self.assertEqual(metadata["items"], ["one"])
        self.assertEqual(body, "# Body\n")

    def test_missing_front_matter_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "entry.md"
            path.write_text("# Body\n", encoding="utf-8")
            with self.assertRaises(FrontMatterError):
                parse_front_matter(path)


class ScoringTests(unittest.TestCase):
    def test_weighted_score_matches_bootstrap_sample(self) -> None:
        score = calculate_weighted_score(
            {
                "relevance": 5,
                "completeness": 5,
                "actionability": 5,
                "clarity": 5,
                "safety_guardrails": 5,
                "novelty": 3,
                "cross_tool_portability": 5,
                "provenance": 5,
            }
        )
        self.assertEqual(score, 4.84)


class CatalogTests(unittest.TestCase):
    def test_bootstrap_artifacts_are_discovered(self) -> None:
        paths = [path.relative_to(ROOT).as_posix() for path in artifact_files(ROOT)]
        self.assertEqual(
            paths,
            [
                "artifacts/control-loops/bounded-scout-evaluate-publish-loop.md",
                "artifacts/control-loops/mcp-2026-07-28-multi-round-trip-tool-calls.md",
                "artifacts/guardrails/mcp-2026-07-28-auth-ssrf-handle-guardrails.md",
                "artifacts/mcp/mcp-2026-07-28-untrusted-tool-annotations-and-handles.md",
                "artifacts/rules/read-only-research-agent/AGENTS.md",
                "artifacts/skills/change-verification-gate.md",
            ],
        )

    def test_records_are_deterministic_and_machine_readable(self) -> None:
        records = artifact_records(ROOT)
        self.assertEqual(len(records), 6)
        self.assertEqual(
            [record["id"] for record in records],
            [
                "asf-control-loop-20260825-003",
                "asf-control-loop-20260826-002",
                "asf-guardrail-20260826-003",
                "asf-mcp-artifact-20260826-001",
                "asf-rule-set-20260825-002",
                "asf-skill-20260825-001",
            ],
        )
        jsonl = render_jsonl(records)
        decoded = [json.loads(line) for line in jsonl.splitlines()]
        self.assertEqual(decoded, records)
        csv_text = render_catalog_csv(records)
        self.assertIn("stealable_mechanism", csv_text.splitlines()[0])
        self.assertEqual(len(csv_text.splitlines()), 7)

    def test_journal_index_projection(self) -> None:
        paths = journal_files(ROOT)
        self.assertEqual(len(paths), 2)
        record = journal_record(paths[0], ROOT)
        self.assertEqual(record["id"], "journal-2026-bootstrap")
        self.assertEqual(len(record["artifact_ids"]), 3)
        first_run = journal_record(paths[1], ROOT)
        self.assertEqual(first_run["id"], "journal-2026-08-26-first-run")
        self.assertEqual(len(first_run["artifact_ids"]), 3)


if __name__ == "__main__":
    unittest.main()
