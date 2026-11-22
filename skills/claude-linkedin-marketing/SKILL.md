---
name: claude-linkedin-marketing
description: Orchestrate Claude-native LinkedIn content delivery, warm-signal capture, MCP qualification, and consultative conversion sequences.
---

# Claude-Native LinkedIn Pipeline Orchestration

<context>
Orchestrates end-to-end inbound pipeline generation on LinkedIn using Anthropic Claude Code and Model Context Protocol (MCP) servers. Bridges top-of-funnel content to qualified pipeline through structured signal monitoring, AI qualification scoring, and consultative DM conversion.
</context>

<workflow>
| Motion | Native MCP / Engine Surface | Output Artifact |
|---|---|---|
| **Content Creation** | `linkedin-copywriter`, `claude-code` | Production post draft, carousels, text artifacts |
| **Publishing & Cadence** | `content-waterfall`, Scheduling MCP | 7-day sequenced calendar, scheduled release slots |
| **Signal Capture** | Profile Watcher MCP, LinkedIn Engager Feed | Real-time engagers, commenters, profile visitors |
| **ICP Qualification** | `linkedin-funnel qualify`, Claude Rubric | Scored candidate records (Company Fit, Persona Fit) |
| **Consultative DM** | `claude-sequencer`, LinkedIn Messaging MCP | Personalized problem discovery, tailored resource DM |
| **Inbox Triage** | `claude-unibox`, Unibox MCP | Categorized conversation threads, demo booking |
</workflow>

<instructions>
1. **Signal Processing & Ingestion**:
   - Ingest post engagers (likes, comments, reposts) and profile views via LinkedIn MCP.
   - Separate active comment leads (explicit opt-ins) from passive likers.

2. **Rigorous ICP Qualification**:
   - Evaluate each lead against the calibrated ICP criteria: B2B focus, headcount (20-250 sweet spot), decision-maker seniority.
   - Run verification via `linkedin-funnel qualify --profile <lead_json>`.
   - Never enroll unqualified or borderline leads into active sales motions.

3. **Resource & Lead Magnet Fulfillment**:
   - When leads comment with trigger keywords, generate personalized delivery via `lead-magnet-delivery`.
   - Ensure delivery includes direct links, contextual commentary, and consultative follow-up questions.

4. **Pipeline Tracking & Handoff**:
   - Attribute pipeline to specific source posts and content waterfall tiers (TOFU, MOFU, BOFU).
   - Sync qualified opportunities to CRM via MCP.
</instructions>
