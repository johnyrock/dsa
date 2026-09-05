# DSA Practice

LeetCode-style practice, organized by difficulty and pattern.

## How to use

No dependencies. Each problem's test file is a plain script that prints PASS or FAIL per case.

```bash
python3 easy/001-two-sum/test_two_sum.py
```

**Per session:**
1. Check the **Due for review** list below. Re-solve those first: delete the solution file, keep the tests, write it again from scratch, run the tests.
2. Take a new problem. The folder is created from `templates/problem/` with only the statement and tests.
3. Attempt it. Ask for hints before looking at the answer.
4. After review, fill in the solution, the annotated version, and `notes.md`.
5. Update the index below and the relevant page in `patterns/`.

**Confidence scale:** 1 = needed the full answer, 2 = needed a hint, 3 = solved but slow or messy, 4 = clean solve, 5 = could teach it.

**Review spacing:** next review is roughly 3 days after confidence 1-2, 1 week after 3, 3 weeks after 4, and 6 weeks after 5.

## Index

| # | Problem | Difficulty | Pattern | Solved | Confidence | Next review |
|---|---------|------------|---------|--------|------------|-------------|
| easy/001 | [Two Sum](easy/001-two-sum/) | Easy | [hash-map](patterns/hash-map.md) | 2026-09-04 | 4 | 2026-09-25 |

## Due for review

_(Problems whose next review date has passed. Updated at the start of each session.)_

- none yet

## Patterns

| Pattern | Problems |
|---------|----------|
| [hash-map](patterns/hash-map.md) | easy/001 |

## Layout

```
easy/NNN-slug/
  README.md               statement, examples, constraints
  <slug>.py               clean interview version, e.g. two_sum.py
  <slug>_annotated.py     line-by-line commented version
  test_<slug>.py          plain script, prints PASS/FAIL per case
  notes.md                attempts, sticking points, key insight, complexity
medium/NNN-slug/          same shape, numbering restarts per difficulty
patterns/<name>.md        when to use it, template code, problems that use it
templates/problem/        skeleton copied for each new problem (see templates/README.md)
```
