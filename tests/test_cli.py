"""Unit tests for the unified CLI interface."""

import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TestCLI(unittest.TestCase):
    def test_cli_verify_subcommand(self):
        """Test 'python3 -m linkedin_funnel verify' exits with code 0."""
        cmd = [sys.executable, "-m", "linkedin_funnel", "verify", "--root", str(ROOT)]
        res = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, f"CLI verify failed: {res.stderr}")
        self.assertIn("PASSED", res.stdout)

    def test_cli_qualify_subcommand(self):
        """Test 'python3 -m linkedin_funnel qualify' outputs valid qualification JSON."""
        example_json = ROOT / "examples" / "qualification-decisions.json"
        cmd = [sys.executable, "-m", "linkedin_funnel", "qualify", str(example_json)]
        res = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, f"CLI qualify failed: {res.stderr}")
        data = json.loads(res.stdout)
        self.assertIn("company_score", data)
        self.assertIn("fit_status", data)

    def test_cli_waterfall_subcommand(self):
        """Test 'python3 -m linkedin_funnel waterfall' produces a 7-day schedule."""
        cmd = [
            sys.executable, "-m", "linkedin_funnel", "waterfall",
            "Full Stack Inbound Pipeline", "--date", "2026-11-23"
        ]
        res = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, f"CLI waterfall failed: {res.stderr}")
        data = json.loads(res.stdout)
        self.assertEqual(data["sprint_thesis"], "Full Stack Inbound Pipeline")
        self.assertEqual(len(data["schedule"]), 7)


if __name__ == "__main__":
    unittest.main()
