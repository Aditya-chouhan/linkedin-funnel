# The Content Waterfall Architecture

[Back to LinkedIn Funnel](../README.md)

**Turn 1 core technical thesis or video each week into a complete multi-platform inbound engine.**

AI agent skills handle research, structuring, drafting, and cross-channel adaptation; you provide the core operator experience, insights, and editorial review.

![The Content Waterfall](../assets/content-waterfall.gif)

[High-Resolution Graphic](../assets/content-waterfall@2x.png) · [Editable Map (Excalidraw)](../assets/content-waterfall.excalidraw) · [System Map PNG](../assets/content-waterfall-map.png) · [Content Waterfall Skill](../skills/content-waterfall/SKILL.md)

---

## The 5 Stages & Execution Skills

| Stage | What Happens | Core Skills |
|---|---|---|
| **0. Thesis & Demand Research** | Validate topic demand across technical discussions, identify packaging angles, and evaluate search interest. | [youtube-video-research](../skills/youtube-video-research/SKILL.md), [x-research](../skills/x-research/SKILL.md), [youtube-title-outlier-packaging](../skills/youtube-title-outlier-packaging/SKILL.md), [youtube-thumbnail-outlier-research](../skills/youtube-thumbnail-outlier-research/SKILL.md), [x-planner](../skills/x-planner/SKILL.md) |
| **1. Core Long-Form Asset** | Package title and thumbnail first, outline structural arguments, record demo/talking head, cut, and finalize asset. | [youtube-script](../skills/youtube-script/SKILL.md), [talking-head-video-cut](../skills/talking-head-video-cut/SKILL.md), [video-editor](../skills/video-editor/SKILL.md), [longform-edit](../skills/longform-edit/SKILL.md), [youtube-thumbnail](../skills/youtube-thumbnail/SKILL.md), [youtube-description](../skills/youtube-description/SKILL.md) |
| **2. Multi-Channel Waterfall** | Distribute core argument into deep-dive technical essays, native LinkedIn posts, carousels, architecture flowcharts, and 3D system dioramas. | [newsletter-writer](../skills/newsletter-writer/SKILL.md), [x-article-writer](../skills/x-article-writer/SKILL.md), [linkedin-article-adapter](../skills/linkedin-article-adapter/SKILL.md), [linkedin-copywriter](../skills/linkedin-copywriter/SKILL.md), [linkedin-hook-writer](../skills/linkedin-hook-writer/SKILL.md), [x-planner](../skills/x-planner/SKILL.md), [graphics-designer](../skills/graphics-designer/SKILL.md), [diorama-3d](../skills/diorama-3d/SKILL.md), [flowchart](../skills/flowchart/SKILL.md), [repurpose-content](../skills/repurpose-content/SKILL.md) |
| **3. Scheduling & Cadence** | Map the week's posts into an integrated editorial calendar, sequenced around the core release. | [content-waterfall](../skills/content-waterfall/SKILL.md), [Notion Guide](notion.md), [oxygen-linkedin-marketing](../skills/oxygen-linkedin-marketing/SKILL.md) |
| **4. Conversational Conversion** | Capture profile viewers and post engagers, score ICP fit, trigger automated lead magnet delivery, and initiate consultative discovery. | [Profile Watcher Guide](profile-watcher.md), [Qualification Guide](qualification.md), [lead-magnet-delivery](../skills/lead-magnet-delivery/SKILL.md), [oxygen-sequencer](../skills/oxygen-sequencer/SKILL.md), [linkedin-unibox-reply](../skills/linkedin-unibox-reply/SKILL.md), [DM Conversion Guide](dm-conversion.md) |

---

## Agent Prompt Walkthrough

### Step 1: Initialize the Weekly Waterfall

In your AI agent (OpenAI Codex, Claude Code, or Antigravity), initiate the sprint:

```text
Read AGENTS.md, README.md and guides/content-waterfall.md. Run the
content-waterfall skill for this week. My idea: [YOUR TOPIC/THESIS, OR "generate a slate from our pillars"].
My primary asset goes live on [DATE]. Start with stage 0 if we need packaging validation,
otherwise draft the core brief and map out the derived platform assets.
```

### Step 2: Ingest Raw Footage or Transcript

Once the primary asset or recording is ready:

```text
Here is my recording transcript / notes: [PATH OR TEXT]. Continue the content
waterfall from stage 2: draft the core technical newsletter first, then derive
the LinkedIn post slate, hook variations, and architecture graphic briefs.
```

---

## Operating Principles

- **One Deep Thesis Drives the Entire Week**: High-converting pipeline comes from intellectual depth and proven receipts, not superficial volume.
- **Batch Production, Continuous Pipeline**: 1 day dedicated to thesis recording and review supplies an entire week of qualified conversational touchpoints.
- **Zero Hallucinated Proof**: Never publish synthetic metrics or claims not explicitly backed by context files in `context/identity/proof.md`.
