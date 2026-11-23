"""Unit tests for the Claude + Apple LinkedIn Post Writer engine."""

import unittest
from linkedin_funnel.post_writer import generate_linkedin_post


class TestPostWriter(unittest.TestCase):
    def test_default_teardown_generation(self):
        res = generate_linkedin_post("Pipeline Automation Engine")
        self.assertEqual(res["topic"], "Pipeline Automation Engine")
        self.assertEqual(res["format"], "teardown")
        self.assertEqual(res["cta_keyword"], "FUNNEL")
        self.assertIn("Pipeline Automation Engine", res["post_body"])
        self.assertIn("Drop a comment with \"FUNNEL\"", res["post_body"])
        self.assertIn("#GTM", res["post_body"])
        self.assertIn("#ClaudeAI", res["post_body"])
        # No external links in body
        self.assertNotIn("http://", res["post_body"])
        self.assertNotIn("https://", res["post_body"])
        # Link in pinned comment
        self.assertIn("https://github.com/Aditya-chouhan/linkedin-funnel", res["pinned_comment"])

    def test_waterfall_format(self):
        res = generate_linkedin_post(
            topic="Content Waterfall System",
            format_type="waterfall",
            cta_keyword="SYSTEM"
        )
        self.assertEqual(res["format"], "waterfall")
        self.assertEqual(res["cta_keyword"], "SYSTEM")
        self.assertIn("The Single-Video Trunk", res["post_body"])
        self.assertIn("Drop a comment with \"SYSTEM\"", res["post_body"])
        self.assertNotIn("http", res["post_body"])

    def test_benchmark_format(self):
        res = generate_linkedin_post(
            topic="2D ICP Qualification",
            format_type="benchmark",
            cta_keyword="ICP"
        )
        self.assertEqual(res["format"], "benchmark")
        self.assertIn("Cold outbound didn't die", res["post_body"])
        self.assertIn("Company Fit Scoring (0-100)", res["post_body"])
        self.assertIn("Drop a comment with \"ICP\"", res["post_body"])

    def test_custom_pillars_and_hook(self):
        pillars = [
            {"title": "Custom Pillar A", "desc": "Detailed architecture note."},
            {"title": "Custom Pillar B", "desc": "Another precision point."}
        ]
        res = generate_linkedin_post(
            topic="Agent Framework",
            custom_hook="Agents without system architecture are toys.",
            pillars=pillars
        )
        self.assertIn("Agents without system architecture are toys.", res["post_body"])
        self.assertIn("1. Custom Pillar A", res["post_body"])
        self.assertIn("2. Custom Pillar B", res["post_body"])


if __name__ == "__main__":
    unittest.main()
