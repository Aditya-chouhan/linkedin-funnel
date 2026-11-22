# Profile Watcher Guide: Signal Ingestion with Claude & MCP

The Profile Watcher captures warm inbound signals from LinkedIn: profile visitors, post engagers, and comment triggers. It operates through connected Model Context Protocol (MCP) servers and feeds directly into Claude Code's qualification and consultative conversion engine.

---

## 1. Overview & Mechanics

```
┌────────────────────────┐
│ Public LinkedIn Signals │ (Post Likers, Commenters, Profile Views)
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│   LinkedIn MCP Server  │ (Discovers and queries engager stream)
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│ Claude Code Evaluator  │ (Evaluates ICP fit via `linkedin-funnel qualify`)
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│ Consultative Sequence  │ (`claude-sequencer` / personalized DM delivery)
└────────────────────────┘
```

---

## 2. Setting Up Signal Ingestion via Claude Code & MCP

Verify that your LinkedIn MCP server or local signal capture tool is connected to Claude Code:

```bash
# Check connected MCP tools in Claude Code
claude mcp list

# Run pipeline environment verification
python3 -m linkedin_funnel verify
```

### Previewing Watched Profiles with Claude

Prompt Claude Code to inspect target profiles and review incoming engagement:

```bash
claude "Inspect engagers on my recent LinkedIn post and preview ICP fit"
```

Or run the local pipeline signal parser directly:

```bash
python3 -m linkedin_funnel qualify --profile examples/decisions.json
```

---

## 3. Qualification Integrity Principles

- **Preserve Source Evidence**: Retain the exact post URL, comment timestamp, and engagement context with each lead record.
- **Separate Signal from Authorization**: A "like" or profile view is an observed signal, not an explicit opt-in for aggressive sales pitches.
- **Strict ICP Gating**: Never enroll un-enriched contacts. Feed raw signals through [the qualification rubric](qualification.md) before initiating consultative direct messaging.

---

## 4. Next Steps

1. Review and calibrate your ICP scoring rubric in [`guides/qualification.md`](qualification.md).
2. Configure automated resource delivery via [`lead-magnet-delivery`](../skills/lead-magnet-delivery/SKILL.md).
3. Operate consultative direct message cadences with [`claude-sequencer`](../skills/claude-sequencer/SKILL.md) and [`claude-unibox`](../skills/claude-unibox/SKILL.md).
