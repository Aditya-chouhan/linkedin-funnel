---
name: claude-unibox
description: Triage LinkedIn inbox threads and conversation replies, draft consultative responses, and route qualified opportunities to demo booking.
---

# Claude Inbox Triage & Consultative Conversation Engine

<context>
Manages active, multi-turn direct message conversations across LinkedIn and connected channels. Triages inbound responses, answers technical questions, navigates consultative problem discovery, and books discovery calls.
</context>

<workflow>
```
[Inbound Reply Received]
        │
        ▼
[Claude Analysis: Intent Classification]
   ├── Positive / Curious ──> [Consultative Problem Discovery]
   ├── Resource Received ────> [Value Check & Discussion Opener]
   ├── Technical Question ───> [Technical Architecture Deep Dive]
   └── Objection / Not Fit ──> [Graceful Close & Knowledge Log]
        │
        ▼
[Demo / Discovery Call Booking via Cal.com or Calendly]
```
</workflow>

<instructions>
1. **Thread Ingestion & Triage**:
   - Ingest unanswered conversations using LinkedIn MCP.
   - Classify conversation state: Active Discovery, Objection, Follow-up Required, Call Scheduled.

2. **Drafting Consultative Replies**:
   - Adopt a collegial, peer-to-peer technical engineering tone.
   - Address the prospect's exact question before pivoting to discovery.
   - Offer specific, actionable insights rather than canned responses.

3. **Call Conversion**:
   - When pain is validated and fit is established, suggest a short, zero-pressure architecture review call.
</instructions>
