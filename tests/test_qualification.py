"""Unit tests for ICP Qualification and scoring engine."""

import unittest
from scripts.qualify import qualify_prospect


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


if __name__ == "__main__":
    unittest.main()
