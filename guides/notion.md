# Set Up Your Notion Content Board

[Back to LinkedIn Funnel](../README.md)

This guide walks you through setting up a structured Notion content board linked to your personal-brand second brain.

---

## Content Board Architecture

A clean content board separates strategic pillars from individual editorial execution:

```
┌────────────────────────────────────────────────────────┐
│                   PILLARS & TOPICS                     │
│  Foundational topics, sub-arguments, and funnel jobs   │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│                    CONTENT BOARD                       │
│  Individual posts, draft states, scheduled dates,      │
│  and platform distribution                             │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│                     HOOK LIBRARY                       │
│  High-performing opening hooks, templates, and angles  │
└────────────────────────────────────────────────────────┘
```

---

## Quick Setup with Your AI Agent

Provide your agent with your Notion workspace parent page and prompt it:

```text
Use setup-workspace. Set up the content system under this Notion parent:
[MY PARENT PAGE URL]. Read context/strategy/notion-schema.md. Inspect the
parent first and reuse matching databases if present. Create or map Content
Board, Pillars & Topics, Hooks and Creator Inspo DB. Keep author-specific rows
empty until we define them. Store verified IDs in
context/strategy/notion.local.json. Verify the resulting schemas and summarize
the database setup.
```

The database [schema](../context/strategy/notion-schema.md) and [page templates](../context/templates) are included in this repository.

---

## Core Database Schema

| Database | Primary Attributes | Purpose |
|---|---|---|
| **Content Board** | Name, Status, Pillar, Platform, Publish Date, Format | Production calendar and drafted posts |
| **Pillars & Topics** | Topic Name, Pillar Category, Funnel Tier (TOFU/MOFU/BOFU), Status | Core thesis and subject areas |
| **Hook Library** | Hook String, Hook Category, Performance Score | Reusable opening hooks |
| **Inspiration Board** | Creator Name, Source URL, Takeaway Notes | Reference models and formatting benchmarks |

---

## Best Practices

1. **One Core Pillar per Asset**: Avoid diluting content with multiple conflicting themes.
2. **Preserve Drafts in Markdown**: Store canonical copies of posts inside your local git-backed `context/` directory so you retain full ownership of your intellectual property.
3. **Draft to Publish Flow**: Move cards through `Idea` → `Drafting` → `Calibrated Review` → `Scheduled` → `Published`.
