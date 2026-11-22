# Claude Code & Model Context Protocol (MCP) Runtime Guide

The LinkedIn Funnel and Content Waterfall system is built natively for **Anthropic Claude Code** and uses the open **Model Context Protocol (MCP)** to interact with real-world marketing and pipeline infrastructure.

---

## 1. Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Anthropic Claude Code                     │
│      (Claude 3.7 Sonnet / Claude 3.5 Sonnet Engine)         │
└──────────────────────────────┬──────────────────────────────┘
                               │
                Model Context Protocol (MCP)
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
┌──────────────┐        ┌──────────────┐        ┌──────────────┐
│ LinkedIn MCP │        │   CRM MCP    │        │  Local CLI   │
│  (Profiles,  │        │ (HubSpot /   │        │  (Audience   │
│   Posts, DMs)│        │  Attio / DB) │        │ Qualification│
└──────────────┘        └──────────────┘        └──────────────┘
```

The system operates across three tiers:
1. **Local Reasoning Tier**: Skills, prompts, rubrics, and content planners run completely locally inside Claude Code without third-party platform lock-in.
2. **MCP Integration Tier**: External tools (LinkedIn profile monitoring, scheduled publishing, CRM record updates) connect via standardized MCP servers.
3. **Execution & Validation Tier**: The local Python package `linkedin_funnel` validates data models, verifies candidate records, and computes weekly content waterfalls.

---

## 2. Setting Up Claude Code with MCP

Verify your Claude Code installation and inspect connected MCP servers:

```bash
# Check Claude Code CLI version
claude --version

# List active MCP servers
claude mcp list
```

### Adding Recommended MCP Servers to Claude Code

Add the relevant MCP servers to your Claude Code configuration (`~/.claude.json` or project-level configuration):

```bash
# Example: Adding a local CRM or database MCP server
claude mcp add crm-sync -- /usr/local/bin/node /path/to/crm-mcp-server/index.js

# Example: Adding filesystem or API bridges
claude mcp add linkedin-bridge -- python3 -m linkedin_bridge_mcp
```

---

## 3. Core Claude-Native Skills

| Skill | Role | Primary Command / Surface |
|---|---|---|
| [`claude-quickstart`](../skills/claude-quickstart/SKILL.md) | Verify environment & initialize pipeline | `claude` |
| [`claude-linkedin-marketing`](../skills/claude-linkedin-marketing/SKILL.md) | End-to-end inbound marketing orchestration | Claude Code + MCP |
| [`claude-sequencer`](../skills/claude-sequencer/SKILL.md) | Bounded, consultative outreach cadences | Claude Code Messaging MCP |
| [`claude-unibox`](../skills/claude-unibox/SKILL.md) | Direct message triage and conversation closing | Claude Code Unibox MCP |

---

## 4. Local CLI Operations

The repository provides a fast, standalone CLI that Claude Code calls during autonomous workflows:

```bash
# Verify all schemas, assets, and 50 skills
python3 -m linkedin_funnel verify

# Score and qualify an inbound candidate
python3 -m linkedin_funnel qualify --profile examples/decisions.json

# Generate a 7-day content waterfall schedule
python3 -m linkedin_funnel waterfall --topic "B2B AI Pipeline Engineering"
```

---

## 5. Security & Rate-Limiting Principles

- **Zero Blind Outbound**: Claude Code never sends unverified mass messages. Every candidate record is scored against the company and persona rubrics.
- **Strict Caps**: Limit daily connection requests to 20-25 and direct messages to 30 to preserve sender domain and account standing.
- **Explicit Stops**: Sequences abort immediately when a recipient replies, scheduling a call, or opting out.
