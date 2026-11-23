"""Claude + Apple LinkedIn Post Writer Engine.

Generates high-converting, authority-building LinkedIn posts and pinned comments
engineered according to the signature Claude + Apple editorial standard.
"""

from typing import Dict, Any, List, Optional


def generate_linkedin_post(
    topic: str,
    format_type: str = "teardown",
    cta_keyword: str = "FUNNEL",
    repo_url: str = "https://github.com/Aditya-chouhan/linkedin-funnel",
    pillars: Optional[List[Dict[str, str]]] = None,
    custom_hook: Optional[str] = None
) -> Dict[str, Any]:
    """Generates a complete Claude + Apple styled LinkedIn post with pinned comment.
    
    Args:
        topic: The central topic, architecture, or project.
        format_type: One of 'teardown', 'waterfall', 'benchmark', 'release'.
        cta_keyword: The single-word comment velocity trigger (e.g., 'FUNNEL', 'CODE').
        repo_url: Destination URL for the pinned first comment.
        pillars: Optional list of {'title': '...', 'desc': '...'} technical points.
        custom_hook: Optional custom opening hook.
    """
    cta_keyword = cta_keyword.strip().upper()

    # Default pillars if none provided
    if not pillars:
        if format_type == "waterfall":
            hook = custom_hook or "Most content creates vanity impressions, not pipeline."
            diagnosis = (
                "You spend 20 hours a week writing across five channels, get a handful of likes from peers, "
                "and exactly zero qualified inbound sales conversations.\n\n"
                "The problem isn't your work ethic. It's the absence of a content waterfall."
            )
            pillars_data = [
                {"title": "The Single-Video Trunk", "desc": "1 high-density 4K video/week answers the core ICP objections directly on tape."},
                {"title": "The 3 Core Roots", "desc": "Extract raw media clips, the core logical framework, and the timestamped transcript."},
                {"title": "Multi-Channel Splintering", "desc": "Repurpose into LinkedIn carousels, X longform essays, a deep newsletter, and YouTube shorts."},
                {"title": "Inbound Lead Conversion", "desc": "Auto-enroll content engagers into consultative, chapter-based DM conversations."},
            ]
        elif format_type == "benchmark":
            hook = custom_hook or "Cold outbound didn't die. 1-dimensional filters did."
            diagnosis = (
                "Traditional sales teams blast 10,000 cold emails based on job titles alone, burn their domains, "
                "and wonder why reply rates are sub-0.5%.\n\n"
                "Here is the exact qualification architecture we implemented to reach 14% meeting conversion."
            )
            pillars_data = [
                {"title": "Company Fit Scoring (0-100)", "desc": "Evaluate headcount velocity, B2B SaaS model, and active tech stack requirements."},
                {"title": "Persona Authority Scoring (0-100)", "desc": "Verify functional budget ownership and decision-making authority before outreach."},
                {"title": "Deterministic 2D Threshold", "desc": "Only leads scoring >= 70 on both axes are routed to personalized sequences."},
                {"title": "Zero-Pitch Consultative DMs", "desc": "Deliver verified architectural receipts and templates instead of generic discovery questions."},
            ]
        else: # teardown or release
            hook = custom_hook or f"Most B2B systems break because they lack an engineered funnel."
            diagnosis = (
                "You spend hours drafting posts, get 5,000 views, a handful of likes from peers, "
                "and exactly zero qualified sales conversations.\n\n"
                f"The issue isn't the algorithm. Over the past few weeks, we codified the entire {topic} system—"
                "and just open-sourced the full codebase and architecture for free."
            )
            pillars_data = [
                {"title": "The Content Waterfall Architecture", "desc": "Turn 1 core technical thesis a week into 10+ cross-channel assets without burning out."},
                {"title": "50 Standalone Agent Skills", "desc": "Pre-built modular agent instructions for Claude Code, Codex, and Antigravity covering research, 3D dioramas, editing, and copywriting."},
                {"title": "2D Deterministic ICP Qualification Engine", "desc": "Scores every post engager across Company Fit (0-100) and Persona Fit (0-100). Only accounts hitting >= 70 on both gates get routed to outreach."},
                {"title": "Consultative DM Conversion Loops", "desc": "Non-salesy conversation frameworks and automated keyword-to-delivery workflows that deliver value upfront and book discovery calls."},
                {"title": "Production Python Package & CLI", "desc": "Includes `linkedin-funnel` CLI, full unit test suite (100% pass), and GitHub Actions CI."},
            ]
    else:
        hook = custom_hook or f"The real bottleneck in {topic} isn't effort. It's system design."
        diagnosis = (
            f"Most teams try to solve {topic} by throwing more hours at manual tasks.\n\n"
            "Here is the engineered system architecture we built to automate it completely."
        )
        pillars_data = pillars

    # Build formatted body
    body_lines = [
        hook,
        "",
        diagnosis,
        "",
        "Here is what's inside the system:",
        ""
    ]

    for i, p in enumerate(pillars_data, start=1):
        body_lines.append(f"{i}. {p['title']}")
        body_lines.append(f"{p['desc']}\n")

    body_lines.append("Everything is open source under MIT. You can fork it, inspect the schemas, and run it directly in your own agent workspace.\n")
    body_lines.append("Want the repository?\n")
    body_lines.append(f"Drop a comment with \"{cta_keyword}\" below, and I'll DM you the direct GitHub repo link + the editable Excalidraw system architecture maps.\n")
    body_lines.append("(Link is also pinned in the first comment).\n")

    # Semantic hashtags
    hashtags = ["#GTM", "#B2BMarketing", "#ClaudeAI", "#AIAutomation", "#OpenSource"]
    body_lines.append(" ".join(hashtags))

    full_post_text = "\n".join(body_lines)

    # Pinned comment
    pinned_comment = (
        f"Here is the direct GitHub repository link:\n"
        f"{repo_url}\n\n"
        f"Everything (all skills, Python CLI, and test suite) is open source under MIT. Star the repo if you find it useful!"
    )

    return {
        "topic": topic,
        "format": format_type,
        "hook": hook,
        "cta_keyword": cta_keyword,
        "hashtags": hashtags,
        "post_body": full_post_text,
        "pinned_comment": pinned_comment,
        "full_output": (
            f"=== MAIN LINKEDIN POST ===\n\n"
            f"{full_post_text}\n\n"
            f"=== PINNED FIRST COMMENT ===\n\n"
            f"{pinned_comment}\n"
        )
    }
