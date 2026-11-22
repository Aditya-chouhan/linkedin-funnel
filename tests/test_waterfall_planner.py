"""Unit tests for the content waterfall planner CLI."""

import unittest
from scripts.content_waterfall_planner import generate_waterfall_plan


class TestWaterfallPlanner(unittest.TestCase):
    def test_waterfall_generation(self):
        plan = generate_waterfall_plan(
            thesis="Multi-Agent Pipeline Engineering",
            pillar="Architecture",
            start_date_str="2026-11-23"
        )
        self.assertEqual(plan["sprint_thesis"], "Multi-Agent Pipeline Engineering")
        self.assertEqual(plan["total_deliverables"], 7)
        self.assertEqual(len(plan["schedule"]), 7)

        # Day 0 is video asset
        self.assertEqual(plan["schedule"][0]["day"], 0)
        self.assertEqual(plan["schedule"][0]["primary_skill"], "youtube-script")

        # Day 3 is lead magnet post
        self.assertEqual(plan["schedule"][3]["day"], 3)
        self.assertEqual(plan["schedule"][3]["primary_skill"], "lead-magnet-creator")


if __name__ == "__main__":
    unittest.main()
