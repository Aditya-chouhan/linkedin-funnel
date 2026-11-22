"""Unit tests for the validator module."""

from pathlib import Path
import unittest
from linkedin_funnel.validator import verify_repository

ROOT = Path(__file__).resolve().parents[1]


class TestValidator(unittest.TestCase):
    def test_repository_verification_passes(self):
        """Ensure verify_repository passes on the current workspace."""
        success, errors = verify_repository(ROOT)
        self.assertTrue(success, f"verify_repository failed with errors: {errors}")
        self.assertEqual(len(errors), 0)


if __name__ == "__main__":
    unittest.main()
