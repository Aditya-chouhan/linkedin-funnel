#!/usr/bin/env python3
"""Check this repository without installing dependencies."""

from pathlib import Path
import sys

# Ensure local package is in sys.path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from linkedin_funnel.validator import verify_repository

if __name__ == "__main__":
    success, errors = verify_repository(ROOT)
    if not success:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print("Template OK: 50 skills, discovery links, local links, 12 JSON files and 7 asset hashes")
