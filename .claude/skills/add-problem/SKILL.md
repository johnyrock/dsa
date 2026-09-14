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
   - **Problem** is a real 2–4 sentence paraphrase of the LeetCode statement naming the input and what to return. Never a placeholder like "Implement the requested operation for X".
   - **Examples**: 2–3, each with a `# comment` explaining why the output is what it is (see 010). Use the same running example the walkthrough traces.
   - **Constraints**: the actual LeetCode constraints for this problem number — check them, don't guess.
   - **Follow-up**: 2–3 questions specific to this problem (a variant, a harder constraint, a different data shape). Never generic ("can you explain the invariant?").
2. `<slug>.py` — clean `Solution` class, no comments
3. `<slug>_annotated.py` — identical solution with a WHY-comment on every meaningful line
4. `main.py` — tiny demo script exercising the solution
5. `test_<slug>.py` — `unittest.TestCase`, a `cases` list of tuples with inline comments on tricky cases, driven via `subTest`
6. `notes.md` — Attempts (mark as "generated as reference material, not solved independently"; first review should be a from-scratch re-solve) / Key insight / Complexity / Mistakes to watch for / Related
   - **Key insight**: 2–4 sentences that match the actual solution in `<slug>.py`.
   - **Mistakes to watch for**: 3–4 concrete bugs for *this* problem — the exact wrong base case, loop bound, sign, or operator, and what wrong output it gives. Never filler like "missing the smallest valid input".
   - **Related**: 2–3 real problems that exist in this repo, by folder path, plus the pattern doc.
7. `walkthrough.html` — see §3a. This is the file most likely to come out wrong; follow §3a to the letter and run the checker in §5.

### 3a. Walkthrough rules

The page is two columns: narration steps on the left, a sticky state panel on the right that re-renders per step. Both must be built **for this problem** — the scaffold is reusable, the content is not.

**Scaffold (copy verbatim from `easy/010-climbing-stairs/walkthrough.html`):** the CSS, the `.panel-wrap` block structure (caption → main figure block → vars/dict block → hidden `#bigwrap` → Code block → `#code-final`), the `$`/`el` helpers, and the whole scroll/IntersectionObserver tail of the script. Do not restructure these.

**Customize — header:**
- `<title>` must be `<Problem Title> Walkthrough` and `<h1>` must be `<Problem Title>, narrated`. A leftover `Climbing Stairs Walkthrough` title is the #1 sign the file was not adapted.
- The `.tag`, intro `<p>`, and `.pattern-used` line are problem-specific.

**Customize — state panel (the right column):**
- The figure must fit the data shape. Reuse an existing renderer rather than inventing: trees → `renderTree`/`POS` + `<svg class="tree" id="tree">` from `easy/011-invert-binary-tree` (supports null slots; two trees side by side for compare problems, see `easy/016-same-tree`); heaps → the same tree renderer (level-order layout) plus the heap array row (`easy/019-last-stone-weight`); arrays / DP tables → the `.array` cell grid with `.cur`/`.hit`/`.dim`/`.idx` (`easy/010`, `easy/001-two-sum`); intervals → the timeline bars in `medium/009-merge-intervals`; linked lists / cycle detection → `easy/012-linked-list-cycle`; bit manipulation → the bit-row cells in `easy/025-number-of-1-bits`; digits with carry → `easy/023-plus-one`. **Never leave 010's staircase for a non-staircase problem.**
- The `<h3>` labels in the panel name the actual structure and running example (`tree · root = [3,9,20,null,null,15,7]`, not `ways to reach each step`).
- `CODE` is the `class Solution:` body from `<slug>.py` only — no `from __future__`, no `TreeNode`/`ListNode` class definitions, no imports. `hl` indices are 0-based into that array.
- `STATES` has exactly one entry per `data-state` on the page. Every entry holds **real values from one concrete running example** (the README's first example) at that moment of the algorithm — actual heap layouts (check with `heapq`), actual XOR accumulators, actual heights. Cells labelled "input"/"state"/"answer" are a placeholder, not a state.
- The script is JavaScript. Watch for Python leaking in: `len(x)`, `None`, `True`/`False`, `elif`, `and`/`or`, `x[-1]`. One `len(source)` in an `hl` array throws at load and blanks the entire panel.
- The pitfall state shows the wrong output the bug produces (e.g. `13, not 8`), using the same example.

**Customize — narration (the left column):** match the depth of `easy/010` / `easy/012`, not a one-liner per step. 7–10 `<section class="step" data-state="…">` blocks in this order:
1. **Problem** — what's asked, the running example in a `<div class="callout">`, what "answer" means; multiple paragraphs.
2. **Brute force** — a *real* naive approach for this problem, with a short `<pre class="code">` snippet and its complexity. Never the generic "a direct approach can re-scan the structure" sentence.
3. **Key insight** — the one idea, tied to the code lines it produces.
4. **Approach** — the algorithm as a `<ul>` of the code lines.
5–7. **Traces** (2–3) — each narrates exactly the values the panel shows in that state, several sentences, with the arithmetic written out (`max(1, 2) + 1 = 3`).
8. **Pitfalls** — at least two concrete bugs, each with the wrong code in `<code>` and the wrong output it produces on the running example; the first must match the panel's pitfall state. `<div class="callout warn">` for the rule to remember.
9. **Complexity** — a `<table>` comparing brute force / intermediate / final like 010's.
10. **Final solution** — a `<ul>` with one `<li>` per meaningful code line, then a `<div class="callout">` one-line summary to remember.

Quote code inline with `<code>…</code>` every time a step refers to a line, variable, or expression (010 has 26; target ≥ 15 overall, more for longer solutions). Escape `<`, `>`, `&` inside `<code>`. Prose and panel must agree: if a step says `4 ^ 1 ^ 2 = 7`, the panel's `vars` for that state shows 7.

## 4. Wire it in

- `index.html`: add a `<div class="card">` (mirroring an existing card's markup exactly — title, `data-pattern`, `<div class="meta">easy/NNN · LeetCode #X</div>`, description `<p>`, foot/pill) into the correct `#sec-easy` or `#sec-medium` section.
- `README.md`: add a row to the big problem table (`- / - / not yet solved`) and to the pattern-summary table at the bottom (create a new pattern row if step 2 introduced one).
- If a new `patterns/<pattern>.md` was created in step 2, make sure its `## Problems` table includes this problem.

## 5. Verify

1. Tests: `cd <tier>/<NNN>-<slug> && python3 -m unittest -q test_<slug>.py` (the folders are not packages, so `unittest discover` from the root finds nothing) and `python3 main.py`. Both must pass.
2. Walkthrough: `node .claude/skills/add-problem/scripts/check-walkthrough.js <tier>/<NNN>-<slug>/walkthrough.html` must print `ok`. It parses the script, executes it under a DOM stub, calls `render()` for every `data-state`, and fails on Python-in-JS, missing states, out-of-range `hl`, boilerplate `CODE`, a template `<title>`, the generic brute-force sentence, or thin narration (< 15 inline `<code>` refs / a step under 15 words). Fix the file, not the checker.
3. Boilerplate grep must be empty: `grep -l "Implement the requested operation\|Choosing a brute-force scan where the stated pattern\|A direct approach can repeatedly" <tier>/<NNN>-<slug>/*`.
4. Open `walkthrough.html` in a browser (`python3 -m http.server` from the repo root, then scroll the page): the panel must change per step, show a figure that matches the data shape, and the console must be clean.
5. Re-check there's no numbering collision with anything added concurrently.

## 6. Report

State plainly: the folder path, LeetCode number, difficulty, pattern used, whether a new pattern doc was created, the test result, the checker output line, and which renderer the walkthrough panel reuses. If the problem already existed (step 1), that's the entire report — nothing else gets created.
