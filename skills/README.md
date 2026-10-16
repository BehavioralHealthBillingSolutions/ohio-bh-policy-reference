# Skills

Two agent skills produce the material in this repository. Each is a folder with a `SKILL.md`
(the instructions an AI agent follows) plus scripts and references. They work in Claude Code,
Codex, or any agent runtime that reads `SKILL.md` files; the scripts also run on their own.

| Skill | What it does | Run on its own |
|---|---|---|
| [`ohio-laws-to-markdown`](ohio-laws-to-markdown/SKILL.md) | Pulls any codes.ohio.gov chapter, rule, or section into citation-ready Markdown with paragraph hierarchy, effective dates, and supplemental history. Python 3.8+, standard library only. | `python3 skills/ohio-laws-to-markdown/scripts/ohio_laws_to_markdown.py 5122-29 -o out.md` |
| [`ohio-policy-change-report`](ohio-policy-change-report/SKILL.md) | Builds a linked change-and-impact report from a JSON comparison spec: per-rule summary, likely impact, owner-ready action, full current and proposed text, reproducible diffs, and source hashes. | `python3 skills/ohio-policy-change-report/scripts/build_report.py spec.json --output report.md` |

Commands in this table use **macOS/Linux desktop → Terminal → bash/zsh**, with Python 3 installed
and the **repository root** as the working folder. For Windows Terminal → PowerShell, use the
examples in [RUNNING_TOOLS.md](../docs/RUNNING_TOOLS.md). Output files are local, not published.

To use a skill through an agent, follow the chosen application's supported installation
instructions; installation directories differ. Downloading a folder does not activate it.
See [WORKFLOW.md](../docs/WORKFLOW.md) for how the two skills fit together.

