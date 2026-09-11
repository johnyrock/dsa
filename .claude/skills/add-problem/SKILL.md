---
name: add-problem
description: Scaffold a new easy/medium DSA problem entry (README, solution, annotated solution, tests, notes, narrated walkthrough) from a problem name or description, matching this repo's existing structure, and wire it into index.html and README.md.
---

# Add Problem

Use when the user asks to create/add a problem entry from a name or short description, e.g. `create "climbing stairs"`, `add two sum`, `add a problem about detecting a cycle in a linked list`.

## 1. Identify the problem

- Match the prompt to a specific, well-known LeetCode problem (title, number, canonical difficulty).
- Only Easy and Medium are in scope. If the best match is Hard, or the prompt is too vague to name a specific problem, say so and stop rather than guessing at a completely different problem.
- **If the prompt is ambiguous** (multiple plausible LeetCode problems fit, e.g. "cycle" could mean Linked List Cycle, Linked List Cycle II, or Find the Duplicate Number) — do not pick one silently. Present the candidates with a one-line brief each (name, LeetCode #, difficulty, what it asks) and ask the user to choose before doing anything else.
- Otherwise (a single clear match), proceed without asking for confirmation.
- **Before creating anything**, check `easy/` and `medium/` for a folder already covering this LeetCode number or an equivalent slug. If it already exists, tell the user which folder it is and stop — do not duplicate or overwrite it.

## 2. Assign folder, number, and pattern

- Scan `easy/` or `medium/` (whichever tier matches) for the highest existing `NNN` prefix and use the next number. Never assume from memory — list the directory.
- Slug: kebab-case of the problem title, matching existing folder names (e.g. `012-linked-list-cycle`).
- Pattern: pick the closest fit among patterns that already have both a `patterns/<pattern>.md` and `concepts/<pattern-or-concept-slug>.html` in this repo (check `patterns/` and `concepts/` — do not assume, list them). Reuse an existing pattern whenever reasonable.
  - If genuinely no existing pattern fits, make your best-effort guess at a new pattern name, create `patterns/<pattern>.md` for it (same shape as `patterns/graph.md`: When to use / Templates / Problems table / Common mistakes), and flag in your final report that this was a new pattern you introduced.

## 3. Generate the files

Use `easy/010-climbing-stairs` and `medium/012-longest-palindromic-substring` as the canonical templates for shape, tone, and file naming. For linked-list or tree problems, reuse the existing `ListNode`/`TreeNode` + `from_list`/`to_list`/`build_tree`/`tree_to_list` helper conventions already established in `easy/007-reverse-linked-list` and the tree problems under `medium/014`–`023` rather than inventing new ones.

Create, in `<tier>/<NNN>-<slug>/`:

1. `README.md` — difficulty/pattern/source line, Problem, Examples, Constraints, Walkthrough (link to `walkthrough.html`), Follow-up
2. `<slug>.py` — clean `Solution` class, no comments
3. `<slug>_annotated.py` — identical solution with a WHY-comment on every meaningful line
4. `main.py` — tiny demo script exercising the solution
5. `test_<slug>.py` — `unittest.TestCase`, a `cases` list of tuples with inline comments on tricky cases, driven via `subTest`
6. `notes.md` — Attempts (mark as "generated as reference material, not solved independently"; first review should be a from-scratch re-solve) / Key insight / Complexity / Mistakes to watch for / Related
7. `walkthrough.html` — copy the CSS/JS scaffold from the templates above verbatim; customize only:
   - `<title>`, the `.tag` line, `<h1>`, intro `<p>`, and `.pattern-used` line in `<header>`
   - 7–10 `.step` sections: problem statement → brute force → key insight → optimal approach → 2–3 traces through a running example → a pitfalls step → a complexity table → final solution recap
   - the `STATES` object driving the side panel (adapt the visualization to the data shape — array cells, tree/graph rendered as simple divs, or plain textual state — favor the existing patterns already used elsewhere in the repo over inventing new visuals)
   - the `CODE` array and footer source links

## 4. Wire it in

- `index.html`: add a `<div class="card">` (mirroring an existing card's markup exactly — title, `data-pattern`, `<div class="meta">easy/NNN · LeetCode #X</div>`, description `<p>`, foot/pill) into the correct `#sec-easy` or `#sec-medium` section.
- `README.md`: add a row to the big problem table (`- / - / not yet solved`) and to the pattern-summary table at the bottom (create a new pattern row if step 2 introduced one).
- If a new `patterns/<pattern>.md` was created in step 2, make sure its `## Problems` table includes this problem.

## 5. Verify

Run `python3 -m unittest <tier>/<NNN>-<slug>/test_<slug>.py` (or `python3 -m unittest discover` scoped to the new folder) from the repo root and confirm it passes before reporting done. Also re-check there's no numbering collision with anything else that may have been added concurrently.

## 6. Report

State plainly: the folder path, LeetCode number, difficulty, pattern used, whether a new pattern doc was created, and the test result. If the problem already existed (step 1), that's the entire report — nothing else gets created.
