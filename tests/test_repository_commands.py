from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryCommandTests(unittest.TestCase):
    def run_command(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, *arguments],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_catalog_is_current(self) -> None:
        result = self.run_command("scripts/build_catalog.py", "--check")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_metadata_validation_passes(self) -> None:
        result = self.run_command("scripts/validate_archive.py")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_internal_links_resolve(self) -> None:
        result = self.run_command("scripts/check_internal_links.py")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
