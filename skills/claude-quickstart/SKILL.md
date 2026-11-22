---
name: claude-quickstart
description: Connect LinkedIn Funnel to Anthropic Claude Code, configure Model Context Protocol (MCP) servers, and verify pipeline execution.
---

# Start with Claude & Model Context Protocol (MCP)

<context>
This skill establishes the runtime connection between this LinkedIn inbound pipeline kit, Anthropic Claude Code, and configured Model Context Protocol (MCP) servers. It provides the initial environment verification, account authentication, and qualification preview.
</context>

<instructions>
For the initial runtime initialization:

1. **Verify Claude Environment & MCP Tooling**:
   - Check Claude Code CLI availability: `claude --version`
   - List connected MCP servers: `claude mcp list`
   - Validate repository integrity: `linkedin-funnel verify`

2. **Verify Signal Sources & Connected Accounts**:
   - Inspect connected LinkedIn and CRM MCP servers for account health, rate limits, and permission scopes.
   - Preview active audience signals and profile engagers using `guides/profile-watcher.md`.

3. **Calibrate Pipeline Rubric**:
   - Verify company parameters and persona scoring rules in `company/` (`company_rubric.json`, `persona_rubric.json`).
   - Run sample qualification test: `linkedin-funnel qualify --profile examples/decisions.json`

4. **Sequence Orchestration & Activation**:
   - Review draft schedule with `linkedin-funnel waterfall`.
   - Route execution to `claude-linkedin-marketing` and consultative DM workflows in `guides/dm-conversion.md`.
</instructions>

<guidelines>
- Always verify recipient context and company fit independently before suggesting sequence enrollment.
- Engagement signals alone do not establish sales qualification; maintain strict threshold gates.
- All outbound and follow-up messaging requires explicit author approval before transmission.
</guidelines>
