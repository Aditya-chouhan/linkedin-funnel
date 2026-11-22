"""Deterministic ICP Qualification Engine for B2B inbound leads."""

from typing import Any, Dict, List, Tuple


def evaluate_company(company_data: Dict[str, Any]) -> Tuple[float, bool, str, List[str]]:
    """Evaluates company score (0-100), disqualification status, reason, and evidence."""
    score = 50.0
    disqualified = False
    evidence: List[str] = []

    employees = company_data.get("employee_count", 0)
    industry = str(company_data.get("industry", "")).lower()
    business_model = str(company_data.get("business_model", "")).lower()

    if business_model in ["b2b", "b2b saas", "enterprise", "agency"]:
        score += 30.0
        evidence.append(f"Business model: {business_model}")
    elif business_model in ["b2c", "d2c", "consumer"]:
        score -= 40.0
        disqualified = True
        evidence.append(f"Disqualifying business model: {business_model}")

    if 10 <= employees <= 500:
        score += 20.0
        evidence.append(f"Target headcount tier: {employees} employees")
    elif employees > 1000:
        evidence.append(f"Enterprise headcount: {employees} employees")
    elif employees > 0 and employees < 5:
        score -= 15.0
        evidence.append(f"Early micro-team: {employees} employees")

    if any(tech in industry for tech in ["software", "ai", "tech", "data", "marketing", "consulting", "fintech"]):
        score += 10.0
        evidence.append(f"Target vertical: {industry}")

    final_score = max(0.0, min(100.0, score))
    if disqualified:
        reason = "Company is disqualified: non-target B2C/consumer business model."
    elif final_score >= 70:
        reason = "Strong B2B ICP match with ideal headcount and industry alignment."
    elif final_score >= 40:
        reason = "Moderate company fit; requires manual review."
    else:
        reason = "Weak company fit: low headcount and non-aligned vertical."

    return final_score, disqualified, reason, evidence


def evaluate_persona(person_data: Dict[str, Any]) -> Tuple[float, bool, str, List[str]]:
    """Evaluates persona score (0-100), disqualification status, reason, and evidence."""
    score = 50.0
    disqualified = False
    evidence: List[str] = []

    title = (str(person_data.get("headline", "")) + " " + str(person_data.get("title", ""))).lower()

    if any(kw in title for kw in ["founder", "ceo", "co-founder", "cro", "head of revenue", "head of growth"]):
        score += 40.0
        evidence.append("Executive leadership with primary revenue and GTM budget ownership")
    elif any(kw in title for kw in ["vp", "director", "head of"]):
        score += 25.0
        evidence.append("Senior decision-maker / departmental leadership")
    elif any(kw in title for kw in ["lead", "manager"]):
        score += 10.0
        evidence.append("Mid-level functional owner")
    elif any(kw in title for kw in ["intern", "student", "freelance", "junior"]):
        score -= 40.0
        disqualified = True
        evidence.append("Entry-level or non-decision maker title")

    final_score = max(0.0, min(100.0, score))
    if disqualified:
        reason = "Persona is disqualified: junior or entry-level non-buyer role."
    elif final_score >= 70:
        reason = "High-leverage economic buyer or direct functional decision-maker."
    elif final_score >= 40:
        reason = "Mid-tier influencer; may require referral to senior buyer."
    else:
        reason = "Low seniority role with minimal purchasing authority."

    return final_score, disqualified, reason, evidence


def qualify_prospect(prospect: Dict[str, Any]) -> Dict[str, Any]:
    """Produces a structured qualification evaluation conforming to qualification-output.schema.json."""
    company = prospect.get("company", {})
    missing_fields: List[str] = []

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
