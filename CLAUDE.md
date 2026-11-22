# Working in LinkedIn Funnel

Read README.md, then the relevant skill in skills/. This is an enterprise-grade system for building authority, qualifying inbound engagement, and converting conversations into sales pipeline.

- The canonical skill files are in `skills/`. `.agents/skills` and `.claude/skills` point to that directory. Update `skills/catalog.json` if a skill's name or description changes.
- Read `context/AGENTS.md` before editing author context. Context-relative paths in those skills resolve from `context/`. Unknown author facts stay unknown; synthetic examples are not the author's proof.
- Follow the user's scope and existing authorization. Draft content can stay in chat. Inspect the intended workspace, author, exact content and destination before publishing or sending.
- Read `guides/oxygen.md` before OXYGEN work, then the narrower guide. Profile Watcher collection, AI qualification, Sequence enrollment and message delivery are distinct operations. Inspect current schemas, actual evidence, recurring scope and credit caps.
- Keep credentials, local connection IDs, private buyer rubrics, real prospect data and raw private sources out of public commits. A populated context belongs in the user's private working copy.
- Preserve clean git history. Before committing template changes, run `python3 scripts/check-template.py` and `python3 context/scripts/wiki_lint.py`. Check new or changed executable helpers with unit tests.

This repository provides instructions, prompts, schemas, test suites, and editable assets. It does not run automated daemons, schedule posts, or dispatch messages without explicit user review and command execution.
