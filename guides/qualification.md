# Claude Qualification Guide: Inbound Scoring & Fit Evaluation

[Back to LinkedIn Funnel](../README.md) · [Previous: Collection](profile-watcher.md) · [Next: Conversations](dm-conversion.md)

The qualification engine turns raw LinkedIn engager data into an objective, score-backed shortlist of qualified B2B buyers. It evaluates **Company Fit** and **Persona Fit** independently so high personal engagement never masks an unqualified organization.

---

## 1. Defining Your Rubrics

Define your target buyer parameters in `company/`:
- `company/company_rubric.json`: Headcount, industry, geography, business model (B2B SaaS / Services).
- `company/persona_rubric.json`: Job titles, decision-making remit, seniority, pain triggers.
- `templates/icp-rubric.md`: Prose calibration guide.

### Scoring Structure (100 Points Each)

| Metric | Target Sweet Spot | Pass Threshold | Disqualifiers |
|---|---|---|---|
| **Company Fit** (100 pts) | 20–250 employees, B2B SaaS, funded/scaling | ≥ 70 / 100 | B2C retail, non-profits, agency interns |
| **Persona Fit** (100 pts) | Founder, CEO, VP Sales, Head of Growth | ≥ 70 / 100 | Individual contributors, students, job-seekers |

---

## 2. Running Qualification with Claude & CLI

Run evaluation locally on any candidate JSON file using the built-in CLI:

```bash
# Qualify a candidate profile record
python3 -m linkedin_funnel qualify --profile examples/decisions.json

# Or ask Claude Code directly
claude "Evaluate the engagers in examples/decisions.json against my company rubric"
```

### JSON Output Contract

The qualification engine produces structured JSON matching [`templates/qualification-output.schema.json`](../templates/qualification-output.schema.json):

```json
{
  "company_score": 85,
  "persona_score": 90,
  "is_qualified": true,
  "fit_status": "qualified",
  "company_disqualified": false,
  "persona_disqualified": false,
  "reasons": [
    "Company is a 45-person B2B SaaS firm with active outbound motion.",
    "Candidate is Co-Founder & CEO with direct revenue ownership."
  ],
  "missing_evidence": []
}
```

---

## 3. Calibration Workflow

1. **Verify Baseline Test Suite**:
   ```bash
   python3 -m unittest tests/test_qualification.py -v
   ```
2. **Review Calibration Cases**:
   - `test_ideal_b2b_founder_qualified`: Must pass with `fit_status: qualified`.
   - `test_b2c_intern_disqualified`: Must fail immediately on company and persona gates.
   - `test_borderline_review_case`: Flags ambiguous headcount for manual review.
3. **Audit Before Outreach**:
   Only candidates with `is_qualified: true` and zero disqualification flags advance to consultative direct messaging in [`guides/dm-conversion.md`](dm-conversion.md).
