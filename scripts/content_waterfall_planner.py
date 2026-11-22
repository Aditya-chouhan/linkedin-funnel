#!/usr/bin/env python3
"""
LinkedIn Funnel — Content Waterfall Sprint Planner CLI.
"""

from pathlib import Path
import sys

# Ensure local package is in sys.path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import argparse
from datetime import datetime
import json
from linkedin_funnel.waterfall import generate_waterfall_plan


def main():
    parser = argparse.ArgumentParser(description="LinkedIn Funnel Content Waterfall Sprint Planner")
    parser.add_argument("thesis", help="Core topic, thesis, or technical project for the week")
    parser.add_argument("--pillar", default="Pipeline Architecture", help="Content pillar name")
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"), help="Start date (YYYY-MM-DD)")
    parser.add_argument("--output", "-o", help="Optional output JSON path")
    args = parser.parse_args()

    plan = generate_waterfall_plan(args.thesis, args.pillar, args.date)
    out_json = json.dumps(plan, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(out_json)
        print(f"Sprint waterfall plan saved to {args.output}")
    else:
        print(out_json)


if __name__ == "__main__":
    main()
