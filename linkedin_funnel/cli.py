"""Command-line interface for linkedin-funnel."""

import argparse
import json
from pathlib import Path
import sys

from .qualification import qualify_prospect
from .validator import verify_repository
from .waterfall import generate_waterfall_plan
from .post_writer import generate_linkedin_post


def cmd_qualify(args):
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: input file '{input_path}' not found", file=sys.stderr)
        return 1

    try:
        data = json.loads(input_path.read_text())
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        return 1

    prospects = data if isinstance(data, list) else [data]
    results = [qualify_prospect(p) for p in prospects]
    output_obj = results if len(results) > 1 else results[0]
    out_str = json.dumps(output_obj, indent=2)

    if args.output:
        Path(args.output).write_text(out_str)
        print(f"Qualification written to {args.output}")
    else:
        print(out_str)
    return 0


def cmd_waterfall(args):
    plan = generate_waterfall_plan(
        thesis=args.thesis,
        pillar=args.pillar,
        start_date_str=args.date or ""
    )
    out_str = json.dumps(plan, indent=2)
    if args.output:
        Path(args.output).write_text(out_str)
        print(f"Waterfall plan saved to {args.output}")
    else:
        print(out_str)
    return 0


def cmd_verify(args):
    root_dir = Path(args.root).resolve() if args.root else Path.cwd()
    success, errors = verify_repository(root_dir)
    if not success:
        print("Repository Verification FAILED with errors:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    if not args.quiet:
        print("Repository Verification PASSED: 50 skills, discovery links, local links, JSON files, and asset hashes verified.")
    return 0


def cmd_post(args):
    res = generate_linkedin_post(
        topic=args.topic,
        format_type=args.format,
        cta_keyword=args.cta,
        repo_url=args.url
    )
    if args.json:
        out_str = json.dumps(res, indent=2)
    else:
        out_str = res["full_output"]

    if args.output:
        Path(args.output).write_text(out_str)
        print(f"LinkedIn post generated and saved to {args.output}")
    else:
        print(out_str)
    return 0


def main():
    parser = argparse.ArgumentParser(
        prog="linkedin-funnel",
        description="Full-Funnel LinkedIn Growth & Pipeline Engineering System CLI"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: qualify
    p_qualify = subparsers.add_parser("qualify", help="Evaluate prospect profile against 2D ICP rubric")
    p_qualify.add_argument("input_file", help="Path to JSON file containing prospect profile or array of profiles")
    p_qualify.add_argument("--output", "-o", help="Optional output JSON destination path")
    p_qualify.set_defaults(func=cmd_qualify)

    # Subcommand: waterfall
    p_waterfall = subparsers.add_parser("waterfall", help="Generate 7-day multi-channel sprint schedule from a core topic")
    p_waterfall.add_argument("thesis", help="Core topic, thesis, or technical project for the week")
    p_waterfall.add_argument("--pillar", default="Pipeline Architecture", help="Content pillar name")
    p_waterfall.add_argument("--date", help="Sprint start date (YYYY-MM-DD)")
    p_waterfall.add_argument("--output", "-o", help="Optional output JSON destination path")
    p_waterfall.set_defaults(func=cmd_waterfall)

    # Subcommand: verify
    p_verify = subparsers.add_parser("verify", help="Verify repository integrity, links, skills, and asset hashes")
    p_verify.add_argument("--root", "-r", help="Repository root path (defaults to current directory)")
    p_verify.add_argument("--quiet", "-q", action="store_true", help="Quiet output")
    p_verify.set_defaults(func=cmd_verify)

    # Subcommand: post
    p_post = subparsers.add_parser("post", help="Generate a Claude + Apple styled LinkedIn post and pinned comment")
    p_post.add_argument("topic", help="Topic, architecture, or project name")
    p_post.add_argument("--format", "-f", choices=["teardown", "waterfall", "benchmark", "release"], default="teardown", help="Post format")
    p_post.add_argument("--cta", default="FUNNEL", help="Single-word comment velocity CTA keyword (default: FUNNEL)")
    p_post.add_argument("--url", default="https://github.com/Aditya-chouhan/linkedin-funnel", help="URL for the pinned first comment")
    p_post.add_argument("--json", action="store_true", help="Output post data as structured JSON")
    p_post.add_argument("--output", "-o", help="Optional output destination path")
    p_post.set_defaults(func=cmd_post)

    args = parser.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
