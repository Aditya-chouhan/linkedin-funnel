# System Architecture and Specifications

[Back to LinkedIn Funnel](../README.md)

LinkedIn Funnel is a modular, full-funnel B2B pipeline engineering system designed to bridge the gap between organic audience attention and closed revenue.

---

## Core System Architecture

The system operates across three tightly integrated layers:

```
┌────────────────────────────────────────────────────────┐
│           1. ATTENTION & CONTENT WATERFALL             │
│   Source Insights ──> Core Video/Article ──> Posts     │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│          2. SOCIAL SIGNAL & ICP QUALIFICATION          │
│   Post Interactions ──> Profile Watcher ──> 2D Rubric  │
│   (Company Fit + Person Fit + Need & Timing Evidence)   │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│        3. CONVERSATIONAL CONVERSION & PIPELINE         │
│   Keyword Comment ──> Automated DM Asset Delivery      │
│   Consultative Problem Discovery ──> Discovery Call    │
└────────────────────────────────────────────────────────┘
```

---

## Component Breakdown

| Layer | Primary Objective | Supporting Artifacts & Skills |
|---|---|---|
| **Author Context & Voice** | Ingest raw operator experience, positioning, proof, and calibrated tone without artificial fluff. | `context/`, `capture-context`, `voice-calibration`, `setup-workspace` |
| **Content Strategy & Waterfall** | Transform 1 core technical breakdown or thesis per week into 10+ high-leverage assets across formats. | `guides/content-waterfall.md`, `content-waterfall`, `linkedin-copywriter`, `week-posts`, `lead-magnet-creator` |
| **Visuals & Media System** | Render clean architectural flowcharts, 3D system dioramas, and structured carousels. | `skills/flowchart`, `skills/diorama-3d`, `skills/graphics-designer` |
| **Social Signal Capture** | Monitor profile engagement, comment keywords, and high-intent industry interactions. | `guides/profile-watcher.md`, `skills/claude-linkedin-marketing` |
| **Two-Dimensional Qualification** | Filter high-volume engagement through strict Company Fit and Person Fit rubrics to eliminate tire-kickers. | `guides/qualification.md`, `templates/icp-rubric.md`, `templates/qualification-output.schema.json` |
| **Consultative DM Conversion** | Deliver promised resources seamlessly and convert interest into structured discovery conversations. | `guides/dm-conversion.md`, `guides/lead-magnet-delivery.md`, `skills/linkedin-unibox-reply` |

---

## Validation & Quality Gates

The system includes strict deterministic validation gates:

1. **Skill Discovery & Frontmatter Verification**: Every skill adheres to the Agent Skill Specification (`name`, `description`, structured input parameters). Checked via `scripts/check-template.py`.
2. **Schema Enforcement**: Qualification outputs conform to Draft-07 JSON Schema specifications (`templates/qualification-output.schema.json`).
3. **Context Graph Integrity**: Local markdown link and wiki-link validation across all context and guide directories (`context/scripts/wiki_lint.py`).
4. **Deterministic Qualification CLI**: Deterministic scoring logic and test suites verifying ICP thresholding and reason-attribution logic (`tests/test_qualification.py`).

---

## License

This system is licensed under the [MIT License](../LICENSE). Created by **Aditya Chouhan**.
