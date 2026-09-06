# DSA Practice

LeetCode-style practice, organized by difficulty and pattern.

## How to use

No dependencies. Each problem's test file is a plain script that prints PASS or FAIL per case.

```bash
python3 easy/001-two-sum/test_two_sum.py
```

Open `index.html` in a browser for a home page that links to every walkthrough, filterable by pattern.

**Per session:**
1. Check the **Due for review** list below. Re-solve those first: delete the solution file, keep the tests, write it again from scratch, run the tests.
2. Take a new problem. The folder is created from `templates/problem/` with only the statement and tests.
3. Attempt it. Ask for hints before looking at the answer.
4. After review, fill in the solution, the annotated version, and `notes.md`.
5. Update the index below, the relevant page in `patterns/`, and add a card to `index.html` if a walkthrough was written.

**Confidence scale:** 1 = needed the full answer, 2 = needed a hint, 3 = solved but slow or messy, 4 = clean solve, 5 = could teach it.

**Review spacing:** next review is roughly 3 days after confidence 1-2, 1 week after 3, 3 weeks after 4, and 6 weeks after 5.

## Index

Problems are chosen by interview frequency: the easy tier of the Blind 75 and NeetCode 150 lists, which are built from what companies actually ask. Folders 002 onward were generated as reference material and are not solved yet, so their first session is a from-scratch attempt.

| # | Problem | Difficulty | Pattern | Solved | Confidence | Next review |
|---|---------|------------|---------|--------|------------|-------------|
| easy/001 | [Two Sum](easy/001-two-sum/) | Easy | [hash-map](patterns/hash-map.md) | 2026-09-04 | 4 | 2026-09-25 |
| easy/002 | [Valid Anagram](easy/002-valid-anagram/) | Easy | [hash-map](patterns/hash-map.md) | - | - | not yet solved |
| easy/003 | [Contains Duplicate](easy/003-contains-duplicate/) | Easy | [hash-set](patterns/hash-set.md) | - | - | not yet solved |
| easy/004 | [Valid Parentheses](easy/004-valid-parentheses/) | Easy | [stack](patterns/stack.md) | - | - | not yet solved |
| easy/005 | [Best Time to Buy and Sell Stock](easy/005-best-time-to-buy-and-sell-stock/) | Easy | [sliding-window](patterns/sliding-window.md) | - | - | not yet solved |
| easy/006 | [Valid Palindrome](easy/006-valid-palindrome/) | Easy | [two-pointers](patterns/two-pointers.md) | - | - | not yet solved |
| easy/007 | [Reverse Linked List](easy/007-reverse-linked-list/) | Easy | [linked-list](patterns/linked-list.md) | - | - | not yet solved |
| easy/008 | [Merge Two Sorted Lists](easy/008-merge-two-sorted-lists/) | Easy | [linked-list](patterns/linked-list.md) | - | - | not yet solved |
| easy/009 | [Binary Search](easy/009-binary-search/) | Easy | [binary-search](patterns/binary-search.md) | - | - | not yet solved |
| easy/010 | [Climbing Stairs](easy/010-climbing-stairs/) | Easy | [dynamic-programming](patterns/dynamic-programming.md) | - | - | not yet solved |

## Due for review

_(Problems whose next review date has passed. Updated at the start of each session.)_

- none yet

## Patterns

| Pattern | Problems |
|---------|----------|
| [hash-map](patterns/hash-map.md) | easy/001, easy/002 |
| [hash-set](patterns/hash-set.md) | easy/003 |
| [stack](patterns/stack.md) | easy/004 |
| [sliding-window](patterns/sliding-window.md) | easy/005 |
| [two-pointers](patterns/two-pointers.md) | easy/006 |
| [linked-list](patterns/linked-list.md) | easy/007, easy/008 |
| [binary-search](patterns/binary-search.md) | easy/009 |
| [dynamic-programming](patterns/dynamic-programming.md) | easy/010 |

## Layout

```
index.html                home page linking to every walkthrough, open in a browser
easy/NNN-slug/
  README.md               statement, examples, constraints
  <slug>.py               clean interview version, e.g. two_sum.py
  <slug>_annotated.py     line-by-line commented version
  test_<slug>.py          plain script, prints PASS/FAIL per case
  notes.md                attempts, sticking points, key insight, complexity
  walkthrough.html        optional: scroll-driven narration of the solution, open in a browser
medium/NNN-slug/          same shape, numbering restarts per difficulty
patterns/<name>.md        when to use it, template code, problems that use it
templates/problem/        skeleton copied for each new problem (see templates/README.md)
```
