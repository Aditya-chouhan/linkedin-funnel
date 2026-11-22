"""Content Waterfall Planner: converts a weekly thesis into a multi-channel sprint schedule."""

from datetime import datetime, timedelta
from typing import Any, Dict, List


def generate_waterfall_plan(thesis: str, pillar: str = "Pipeline Architecture", start_date_str: str = "") -> Dict[str, Any]:
    """Generates the 7-day multi-channel waterfall schedule and skill assignments."""
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d") if start_date_str else datetime.now()
    except ValueError:
        start_date = datetime.now()

    days: List[Dict[str, Any]] = [
        {
            "day": 0,
            "date": start_date.strftime("%Y-%m-%d"),
            "channel": "YouTube / Core Video / Loom",
            "format": "Long-Form Video Breakdown (12-18 min)",
            "title": f"The Complete Engineering Guide to {thesis}",
            "primary_skill": "youtube-script",
            "supporting_skills": ["video-editor", "youtube-thumbnail", "youtube-description"],
            "funnel_job": "TOFU Authority & Technical Proof"
        },
        {
            "day": 1,
            "date": (start_date + timedelta(days=1)).strftime("%Y-%m-%d"),
            "channel": "Substack / LinkedIn Newsletter / X Article",
            "format": "Long-Form Essay / Architecture Teardown",
            "title": f"How We Engineered {thesis}: Frameworks & Real Numbers",
            "primary_skill": "newsletter-writer",
            "supporting_skills": ["x-article-writer", "linkedin-article-adapter"],
            "funnel_job": "MOFU Mechanism & System Explanation"
        },
        {
            "day": 2,
            "date": (start_date + timedelta(days=2)).strftime("%Y-%m-%d"),
            "channel": "LinkedIn & X",
            "format": "System Architecture Graphic / Excalidraw / 3D Diorama",
            "title": f"The full-stack visual map of {thesis}",
            "primary_skill": "flowchart",
            "supporting_skills": ["diorama-3d", "graphics-designer", "brand-review"],
            "funnel_job": "TOFU Bookmark Magnet & Visual Memorability"
        },
        {
            "day": 3,
            "date": (start_date + timedelta(days=3)).strftime("%Y-%m-%d"),
            "channel": "LinkedIn",
            "format": "High-Converting Lead Magnet Post",
            "title": f"I spent 40 hours building a production template for {thesis}. Comment 'KIT' and I'll send it.",
            "primary_skill": "lead-magnet-creator",
            "supporting_skills": ["lead-magnet-delivery", "linkedin-hook-writer", "linkedin-copywriter"],
            "funnel_job": "BOFU Inbound Lead Capture & DM Qualification"
        },
        {
            "day": 4,
            "date": (start_date + timedelta(days=4)).strftime("%Y-%m-%d"),
            "channel": "LinkedIn & X",
            "format": "Carousel / Multi-Image Slide Deck",
            "title": f"5 Non-Obvious Lessons from Deploying {thesis} in Production",
            "primary_skill": "graphics-designer",
            "supporting_skills": ["repurpose-content", "linkedin-copywriter"],
            "funnel_job": "MOFU Tactical Retention & Engagement"
        },
        {
            "day": 5,
            "date": (start_date + timedelta(days=5)).strftime("%Y-%m-%d"),
            "channel": "LinkedIn",
            "format": "Proof & Case Study Post",
            "title": f"What happened when we switched our pipeline to {thesis}",
            "primary_skill": "linkedin-copywriter",
            "supporting_skills": ["voice-calibration", "capture-context"],
            "funnel_job": "BOFU Social Proof & Direct Conversion"
        },
        {
            "day": 6,
            "date": (start_date + timedelta(days=6)).strftime("%Y-%m-%d"),
            "channel": "Direct Messages / Unibox",
            "format": "Inbound Triage & Consultative Discovery",
            "title": "Review qualified engagers and conduct consultative problem discovery",
            "primary_skill": "linkedin-unibox-reply",
            "supporting_skills": ["claude-sequencer", "claude-unibox"],
            "funnel_job": "Pipeline Acceleration & Demo Booking"
        }
    ]

    return {
        "sprint_thesis": thesis,
        "pillar": pillar,
        "sprint_start_date": start_date.strftime("%Y-%m-%d"),
        "total_deliverables": len(days),
        "schedule": days
    }
