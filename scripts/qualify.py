#!/usr/bin/env python3
"""
LinkedIn Funnel — Deterministic ICP Qualification CLI.
Strictly conforms to templates/qualification-output.schema.json.
"""

from pathlib import Path
import sys

# Ensure local package is in sys.path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import argparse
import json
from linkedin_funnel.qualification import qualify_prospect


def main():
    parser = argparse.ArgumentParser(description="LinkedIn Funnel Deterministic Qualification Engine")
    parser.add_argument("input_file", help="Path to JSON file containing candidate profile or array of profiles")
    parser.add_argument("--output", "-o", help="Optional output JSON path")
    args = parser.parse_args()

    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: input file '{input_path}' not found", file=sys.stderr)
        sys.exit(1)

    data = json.loads(input_path.read_text())
    prospects = data if isinstance(data, list) else [data]
    results = [qualify_prospect(p) for p in prospects]

    out_json = json.dumps(results if len(results) > 1 else results[0], indent=2)
    if args.output:
        Path(args.output).write_text(out_json)
        print(f"Qualification written to {args.output}")
    else:
        print(out_json)


if __name__ == "__main__":
    main()
