# Working in LinkedIn Funnel

Read README.md, then the relevant skill in skills/. This is an enterprise-grade system for building authority, qualifying inbound engagement, and converting conversations into sales pipeline.

- The canonical skill files are in `skills/`. `.agents/skills` and `.claude/skills` point to that directory. Update `skills/catalog.json` if a skill's name or description changes.
- Read `context/AGENTS.md` before editing author context. Context-relative paths in those skills resolve from `context/`. Unknown author facts stay unknown; synthetic examples are not the author's proof.
- Follow the user's scope and existing authorization. Draft content can stay in chat. Inspect the intended workspace, author, exact content and destination before publishing or sending.
- When drafting or editing LinkedIn posts or responding to user requests for posts, follow `context/voice/linkedin-voice.md`, `context/voice/formats.md`, and `skills/linkedin-copywriter/SKILL.md`. Always apply the Claude + Apple editorial standard: contrarian or razor-sharp hook under 12 words, calm authority, diagnosis, 3–5 technical pillars with specific metrics/mechanisms, single-word velocity comment CTA, exactly 3–5 semantic hashtags, and all external links in the pinned first comment (zero URLs in post body). Use `linkedin-funnel post` or `linkedin_funnel.post_writer.generate_linkedin_post` for generation.
- Read `guides/claude-mcp.md` for Claude Code & Model Context Protocol (MCP) integrations, then the narrower guide. Signal collection, qualification scoring, consultative sequence enrollment, and direct messaging are distinct, inspectable operations. Inspect schemas, evidence, and rate limits.
- Keep credentials, local connection IDs, private buyer rubrics, real prospect data and raw private sources out of public commits. A populated context belongs in the user's private working copy.
- Preserve clean git history. Before committing template changes, run `python3 scripts/check-template.py` and `python3 context/scripts/wiki_lint.py`. Check new or changed executable helpers with unit tests.

This repository provides instructions, prompts, schemas, test suites, and editable assets. It does not run automated daemons, schedule posts, or dispatch messages without explicit user review and command execution.
