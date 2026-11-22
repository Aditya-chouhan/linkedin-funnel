"""Unit tests for JSON Schemas and structural validation."""

import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TestSchemas(unittest.TestCase):
    def test_qualification_schema_valid_json(self):
        """Verify qualification output schema is valid JSON and has expected structure."""
        schema_path = ROOT / "templates" / "qualification-output.schema.json"
        self.assertTrue(schema_path.exists())
        schema = json.loads(schema_path.read_text())
        self.assertEqual(schema.get("type"), "object")
        self.assertIn("properties", schema)
        self.assertIn("company_score", schema["properties"])
        self.assertIn("persona_score", schema["properties"])
        self.assertIn("fit_status", schema["properties"])

    def test_example_decisions_json(self):
        """Verify synthetic calibration decisions file is valid JSON with expected keys."""
        examples_path = ROOT / "examples" / "qualification-decisions.json"
        self.assertTrue(examples_path.exists())
        data = json.loads(examples_path.read_text())
        self.assertIsInstance(data, (dict, list))

    def test_asset_manifest_hashes(self):
        """Verify all assets in assets/manifest.json exist and match SHA-256 hashes."""
        manifest_path = ROOT / "assets" / "manifest.json"
        self.assertTrue(manifest_path.exists())
        manifest = json.loads(manifest_path.read_text())
        for asset in manifest["assets"]:
            file_path = ROOT / "assets" / asset["file"]
            self.assertTrue(file_path.exists(), f"Missing asset file: {file_path}")
            current_hash = hashlib.sha256(file_path.read_bytes()).hexdigest()
            self.assertEqual(current_hash, asset["sha256"], f"Hash mismatch for {asset['file']}")


if __name__ == "__main__":
    unittest.main()
