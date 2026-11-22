---
name: claude-sequencer
description: Operate Claude-native consultative outreach sequences and multi-touch cadences with strict personalization, rate limits, and stop triggers.
---

# Claude Consultative Outreach & Sequence Engine

<context>
Governs cadenced, personalized outreach sequences to qualified inbound leads on LinkedIn. Designed for consultative, high-trust pipeline generation rather than generic mass messaging.
</context>

<principles>
- **Context-Grounded**: Every message must cite the recipient's specific engagement, industry challenge, or stated priority.
- **Strictly Bounded**: Maximum 25-30 new touchpoints per day per account to maintain sender reputation and authentic engagement.
- **Instant Stop on Reply**: The sequence terminates immediately upon any human response, transferring ownership to consultative triage (`claude-unibox`).
- **Zero Pitch Slapping**: No unsolicited sales pitches in message 1. Message 1 delivers requested value or opens a consultative dialogue.
</principles>

<instructions>
1. **Pre-Sequence Readiness Check**:
   - Verify connection state: if connected, proceed to LinkedIn DM; if not, send a personalized connection request citing their comment/interaction.
   - Inspect account daily dispatch limits and suppression lists.

2. **Sequence Structure & Delays**:
   - **Step 1 (Day 0)**: Resource Delivery / Frictionless Value (deliver lead magnet + consultative observation).
   - **Step 2 (Day 2-3)**: Value Expansion (share relevant architectural case study or specific implementation insight).
   - **Step 3 (Day 5-6)**: Consultative Discovery Invite (propose low-friction problem-solving discussion).

3. **Execution via MCP**:
   - Render variables dynamically with real context.
   - Dispatch through connected LinkedIn MCP tools with full audit logging.
</instructions>
