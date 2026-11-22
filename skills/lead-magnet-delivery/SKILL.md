---
name: lead-magnet-delivery
description: Deliver a promised lead magnet or resource to post commenters via LinkedIn MCP with verification, ledger tracking, and rate limits.
---

# Claude Lead Magnet Delivery Engine

<context>
When an author publishes a lead-magnet post with a keyword call-to-action (e.g. "Comment FUNNEL to get the editable template"), this skill reads post comments, filters for keyword opt-ins, sends frictionless direct messages with the resource, and maintains a local delivery ledger.
</context>

<workflow>
```
[Post Comment Ingested via LinkedIn MCP]
                │
                ▼
      [Keyword Match Filter]
     (Check for trigger word)
                │
         Yes ───┴─── No ──> [Ignored]
          ▼
 [Check Delivery Ledger: Dedupe]
 (Has lead received this link?)
          │
      No ─┴─ Yes ──> [Skip: Already Delivered]
          ▼
[Send Frictionless DM with Resource Link]
          │
          ▼
[Record Delivery in Ledger / CRM MCP]
```
</workflow>

<instructions>
1. **Comment Monitoring**:
   - Query comments on the target post URL using connected LinkedIn MCP tools.
   - Filter for exact keyword match or affirmative intent.

2. **Deduplication & Ledger**:
   - Check local delivery ledger (`examples/delivery_ledger.json`) or connected database.
   - Never send duplicate delivery messages to the same recipient.

3. **Message Generation & Delivery**:
   - Draft a natural, frictionless message delivering the direct URL immediately without gatekeeping.
   - Example:
     > "Hey [Name] — saw your comment on the LinkedIn funnel breakdown. Here's the direct editable link: [URL]. Let me know what you think of the waterfall structure!"

4. **Rate Limiting & Safety**:
   - Limit deliveries to a safe rate: maximum 20 to 25 DMs per hour with natural jitter (90-150 seconds between actions).
   - Log all completed transmissions with timestamp and recipient ID.
</instructions>
