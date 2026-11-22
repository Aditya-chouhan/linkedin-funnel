#!/usr/bin/env python3
"""
LinkedIn Funnel — Deterministic ICP Qualification Engine.

Scores prospect profiles according to the two-dimensional ICP rubric:
- company_score (0-100) & company_disqualified (bool)
- persona_score (0-100) & persona_disqualified (bool)
- fit_status: 'qualified', 'review', or 'not_fit'

Strictly conforms to templates/qualification-output.schema.json.
"""

import argparse
import json
from pathlib import Path
import sys


def evaluate_company(company_data: dict) -> tuple[int, bool, str, list[str]]:
    """Evaluates company score (0-100), disqualification, reason, and evidence."""
    score = 50
    disqualified = False
    evidence = []

    employees = company_data.get("employee_count", 0)
    industry = company_data.get("industry", "").lower()
    business_model = company_data.get("business_model", "").lower()

    if business_model in ["b2b", "b2b saas", "enterprise", "agency"]:
        score += 30
        evidence.append(f"Business model: {business_model}")
    elif business_model in ["b2c", "d2c", "consumer"]:
        score -= 40
        disqualified = True
        evidence.append(f"Disqualifying business model: {business_model}")

    if 10 <= employees <= 500:
        score += 20
        evidence.append(f"Target headcount tier: {employees} employees")
    elif employees > 1000:
        evidence.append(f"Enterprise headcount: {employees} employees")
    elif employees > 0 and employees < 5:
        score -= 15
        evidence.append(f"Early micro-team: {employees} employees")

    if any(tech in industry for tech in ["software", "ai", "tech", "data", "marketing", "consulting"]):
        score += 10
        evidence.append(f"Target vertical: {industry}")

    final_score = max(0, min(100, score))
    if disqualified:
        reason = "Company is disqualified: non-target B2C/consumer business model."
    elif final_score >= 70:
        reason = "Strong B2B ICP match with ideal headcount and industry alignment."
    elif final_score >= 40:
        reason = "Moderate company fit; requires manual review."
    else:
        reason = "Weak company fit: low headcount and non-aligned vertical."

    return final_score, disqualified, reason, evidence


def evaluate_persona(person_data: dict) -> tuple[int, bool, str, list[str]]:
    """Evaluates persona score (0-100), disqualification, reason, and evidence."""
    score = 50
    disqualified = False
    evidence = []

    title = (person_data.get("headline", "") + " " + person_data.get("title", "")).lower()

    if any(kw in title for kw in ["founder", "ceo", "co-founder", "cro", "head of revenue", "head of growth"]):
        score += 40
        evidence.append("Executive leadership with primary revenue and GTM budget ownership")
    elif any(kw in title for kw in ["vp", "director", "head of"]):
        score += 25
        evidence.append("Senior decision-maker / departmental leadership")
    elif any(kw in title for kw in ["lead", "manager"]):
        score += 10
        evidence.append("Mid-level functional owner")
    elif any(kw in title for kw in ["intern", "student", "freelance", "junior"]):
        score -= 40
        disqualified = True
        evidence.append("Entry-level or non-decision maker title")

    final_score = max(0, min(100, score))
    if disqualified:
        reason = "Persona is disqualified: junior or entry-level non-buyer role."
    elif final_score >= 70:
        reason = "High-leverage economic buyer or direct functional decision-maker."
    elif final_score >= 40:
        reason = "Mid-tier influencer; may require referral to senior buyer."
    else:
        reason = "Low seniority role with minimal purchasing authority."

    return final_score, disqualified, reason, evidence


def qualify_prospect(prospect: dict) -> dict:
    """Produces the structured schema evaluation."""
    company = prospect.get("company", {})
    missing_fields = []

    if "employee_count" not in company:
        missing_fields.append("company.employee_count")
    if "industry" not in company:
        missing_fields.append("company.industry")
    if "headline" not in prospect and "title" not in prospect:
        missing_fields.append("prospect.title")

    c_score, c_disq, c_reason, c_evidence = evaluate_company(company)
    p_score, p_disq, p_reason, p_evidence = evaluate_persona(prospect)

    if c_disq or p_disq:
        fit_status = "not_fit"
    elif c_score >= 70 and p_score >= 70:
        fit_status = "qualified"
    elif c_score >= 40 and p_score >= 40:
        fit_status = "review"
    else:
        fit_status = "not_fit"

    return {
        "company_score": float(c_score),
        "persona_score": float(p_score),
        "company_disqualified": c_disq,
        "persona_disqualified": p_disq,
        "fit_status": fit_status,
        "company_reason": c_reason,
        "persona_reason": p_reason,
        "missing": missing_fields,
        "evidence_used": c_evidence + p_evidence
    }


def main():
    parser = argparse.ArgumentParser(description="LinkedIn Funnel Deterministic Qualification Engine")
    parser.add_argument("input_file", help="Path to JSON file containing candidate profile")
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
