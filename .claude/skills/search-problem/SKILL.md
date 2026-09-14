---
name: search-problem
description: Find the existing DSA problems in this repo that best match a title, question, or scenario. Triggered by a prompt starting with `search:` (e.g. `search: two sum`, `search: count ways to climb stairs taking 1 or 2 steps`). Outputs title, clickable walkthrough path, and a 1-100 match level.
---

# Search Problem

Use when the user types `search: <problem title | question text | scenario>`.

## 1. Build the candidate list

- List `easy/*/` and `medium/*/` directories — never rely on memory; problems get added.
- For each candidate that could plausibly match, read the first ~20 lines of its `README.md` (title, Pattern, LeetCode #, Problem statement). Skim `patterns/*.md` only if the query names a technique rather than a problem.
- Match on any of: exact/near title, LeetCode number, the problem statement's meaning, or the underlying pattern (e.g. "longest run after k swaps" → longest-repeating-character-replacement; "shortest path in a grid" → number-of-islands / graph pattern as a related match).

## 2. Score

Match level is 1–100:

- **95–100** — same problem (title/LeetCode # match, or the described task is exactly this problem).
- **75–94** — clear variant or the same core problem with a twist (e.g. Linked List Cycle II vs Linked List Cycle).
- **50–74** — same pattern and similar shape; a good study reference but a different task.
- **25–49** — shares the pattern only.
- Below 25 — don't list.

## 3. Output

Return at most 5 matches, highest first, as a table:

| Match | Title | Walkthrough |
|---|---|---|
| 98 | 010. Climbing Stairs (Easy) | `easy/010-climbing-stairs/walkthrough.html` |

- Path is repo-relative in backticks so it is Cmd+clickable in the terminal.
- After the table, one line explaining the top match (or why the top score is low). If nothing scores ≥ 50, say there is no real match, name the closest pattern doc (`patterns/<name>.md`), and offer `add <problem>` via the add-problem skill.
- Do not open browsers, create files, or modify anything. Read-only.
