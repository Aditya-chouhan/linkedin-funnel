"""Unit tests for ICP Qualification and scoring engine."""

import unittest
from linkedin_funnel.qualification import evaluate_company, evaluate_persona, qualify_prospect


class TestQualification(unittest.TestCase):
    def test_ideal_b2b_founder_qualified(self):
        """A B2B SaaS founder at a 45-person company should be qualified."""
        prospect = {
            "full_name": "Sarah Connor",
            "headline": "Founder & CEO @ CyberFlow (B2B AI Platform)",
            "title": "Chief Executive Officer",
            "company": {
                "name": "CyberFlow",
                "employee_count": 45,
                "industry": "Enterprise Software",
                "business_model": "B2B SaaS"
            }
        }
        res = qualify_prospect(prospect)
        self.assertGreaterEqual(res["company_score"], 70)
        self.assertGreaterEqual(res["persona_score"], 70)
        self.assertFalse(res["company_disqualified"])
        self.assertFalse(res["persona_disqualified"])
        self.assertEqual(res["fit_status"], "qualified")

    def test_b2c_intern_disqualified(self):
        """A B2C retail intern should be immediately disqualified."""
        prospect = {
            "full_name": "Bob Green",
            "headline": "Marketing Intern @ RetailShop",
            "title": "Marketing Intern",
            "company": {
                "name": "RetailShop",
                "employee_count": 3,
                "industry": "Apparel",
                "business_model": "B2C"
            }
        }
        res = qualify_prospect(prospect)
        self.assertTrue(res["company_disqualified"] or res["persona_disqualified"])
        self.assertEqual(res["fit_status"], "not_fit")

    def test_borderline_review_case(self):
        """A manager at an ambiguous company should be flagged for review."""
        prospect = {
            "full_name": "Alex Taylor",
            "headline": "Marketing Manager",
            "title": "Marketing Manager",
            "company": {
                "name": "Logistics Co",
                "employee_count": 8,
                "industry": "Logistics",
                "business_model": "Services"
            }
        }
        res = qualify_prospect(prospect)
        self.assertFalse(res["company_disqualified"])
        self.assertFalse(res["persona_disqualified"])
        self.assertEqual(res["fit_status"], "review")

    def test_missing_fields_reporting(self):
        """Missing company employee_count and industry should be detected and reported."""
        prospect = {
            "full_name": "Jane Doe",
            "headline": "CEO",
            "company": {
                "name": "Stealth"
            }
        }
        res = qualify_prospect(prospect)
        self.assertIn("company.employee_count", res["missing"])
        self.assertIn("company.industry", res["missing"])

    def test_evaluate_company_headcount_brackets(self):
        """Verify scores across different company size brackets."""
        # Sweet spot 10-500
        score_mid, _, _, _ = evaluate_company({"employee_count": 50, "business_model": "B2B"})
        # Enterprise >1000
        score_ent, _, _, _ = evaluate_company({"employee_count": 2500, "business_model": "B2B"})
        # Micro <5
        score_micro, _, _, _ = evaluate_company({"employee_count": 2, "business_model": "B2B"})

        self.assertGreater(score_mid, score_micro)
        self.assertGreaterEqual(score_mid, score_ent)


if __name__ == "__main__":
    unittest.main()
