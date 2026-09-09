# DSA Practice

LeetCode-style practice, organized by difficulty and pattern.

## How to use

No dependencies. Each problem's test file is a plain script that prints PASS or FAIL per case.

```bash
python3 easy/001-two-sum/test_two_sum.py
```

Open `index.html` in a browser for a home page with a Concepts / Easy / Medium menu. Each section links to its pages and can be filtered by pattern.

**Per session:**
1. Check the **Due for review** list below. Re-solve those first: delete the solution file, keep the tests, write it again from scratch, run the tests.
2. Take a new problem. The folder is created from `templates/problem/` with only the statement and tests.
3. Attempt it. Ask for hints before looking at the answer.
4. After review, fill in the solution, the annotated version, and `notes.md`.
5. Update the index below, the relevant page in `patterns/`, and add a card to the matching section of `index.html` if a walkthrough was written.

**Before a new pattern:** read its page under `concepts/` first. They explain each pattern from scratch with a hand-traced example.

**Confidence scale:** 1 = needed the full answer, 2 = needed a hint, 3 = solved but slow or messy, 4 = clean solve, 5 = could teach it.

**Review spacing:** next review is roughly 3 days after confidence 1-2, 1 week after 3, 3 weeks after 4, and 6 weeks after 5.

## Index

Problems are chosen by interview frequency: the easy and medium tiers of the Blind 75 and NeetCode 150 lists, which are built from what companies actually ask. Folders easy/002 onward and all of medium/ were generated as reference material and are not solved yet, so their first session is a from-scratch attempt.

| # | Problem | Difficulty | Pattern | Solved | Confidence | Next review |
|---|---------|------------|---------|--------|------------|-------------|
| easy/001 | [Two Sum](easy/001-two-sum/) | Easy | [hash-map](patterns/hash-map.md) · [explained](concepts/hash-map.html) | 2026-09-04 | 4 | 2026-09-25 |
| easy/002 | [Valid Anagram](easy/002-valid-anagram/) | Easy | [hash-map](patterns/hash-map.md) · [explained](concepts/hash-map.html) | - | - | not yet solved |
| easy/003 | [Contains Duplicate](easy/003-contains-duplicate/) | Easy | [hash-set](patterns/hash-set.md) · [explained](concepts/hash-map.html) | - | - | not yet solved |
| easy/004 | [Valid Parentheses](easy/004-valid-parentheses/) | Easy | [stack](patterns/stack.md) · [explained](concepts/stack.html) | - | - | not yet solved |
| easy/005 | [Best Time to Buy and Sell Stock](easy/005-best-time-to-buy-and-sell-stock/) | Easy | [sliding-window](patterns/sliding-window.md) · [explained](concepts/sliding-window.html) | - | - | not yet solved |
| easy/006 | [Valid Palindrome](easy/006-valid-palindrome/) | Easy | [two-pointers](patterns/two-pointers.md) · [explained](concepts/two-pointers.html) | - | - | not yet solved |
| easy/007 | [Reverse Linked List](easy/007-reverse-linked-list/) | Easy | [linked-list](patterns/linked-list.md) · [explained](concepts/linked-list.html) | - | - | not yet solved |
| easy/008 | [Merge Two Sorted Lists](easy/008-merge-two-sorted-lists/) | Easy | [linked-list](patterns/linked-list.md) · [explained](concepts/linked-list.html) | - | - | not yet solved |
| easy/009 | [Binary Search](easy/009-binary-search/) | Easy | [binary-search](patterns/binary-search.md) · [explained](concepts/binary-search.html) | - | - | not yet solved |
| easy/010 | [Climbing Stairs](easy/010-climbing-stairs/) | Easy | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/001 | [Group Anagrams](medium/001-group-anagrams/) | Medium | [hash-map](patterns/hash-map.md) · [explained](concepts/hash-map.html) | - | - | not yet solved |
| medium/002 | [Product of Array Except Self](medium/002-product-of-array-except-self/) | Medium | [prefix-sum](patterns/prefix-sum.md) · [explained](concepts/prefix-sum.html) | - | - | not yet solved |
| medium/003 | [Longest Substring Without Repeating Characters](medium/003-longest-substring-without-repeating-characters/) | Medium | [sliding-window](patterns/sliding-window.md) · [explained](concepts/sliding-window.html) | - | - | not yet solved |
| medium/004 | [3Sum](medium/004-3sum/) | Medium | [two-pointers](patterns/two-pointers.md) · [explained](concepts/two-pointers.html) | - | - | not yet solved |
| medium/005 | [Container With Most Water](medium/005-container-with-most-water/) | Medium | [two-pointers](patterns/two-pointers.md) · [explained](concepts/two-pointers.html) | - | - | not yet solved |
| medium/006 | [Add Two Numbers](medium/006-add-two-numbers/) | Medium | [linked-list](patterns/linked-list.md) · [explained](concepts/linked-list.html) | - | - | not yet solved |
| medium/007 | [Maximum Subarray](medium/007-maximum-subarray/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/008 | [Coin Change](medium/008-coin-change/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/009 | [Merge Intervals](medium/009-merge-intervals/) | Medium | [intervals](patterns/intervals.md) · [explained](concepts/intervals.html) | - | - | not yet solved |
| medium/010 | [Number of Islands](medium/010-number-of-islands/) | Medium | [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | - | - | not yet solved |
| medium/011 | [LRU Cache](medium/011-lru-cache/) | Medium | [linked-list](patterns/linked-list.md) · [explained](concepts/linked-list.html) | - | - | not yet solved |
| medium/012 | [Longest Palindromic Substring](medium/012-longest-palindromic-substring/) | Medium | [two-pointers](patterns/two-pointers.md) · [explained](concepts/two-pointers.html) | - | - | not yet solved |

## Due for review

_(Problems whose next review date has passed. Updated at the start of each session.)_

- none yet

## Concepts

Beginner explainers under `concepts/`, one per pattern. Suggested reading order, top to bottom.

| Group | Pages |
|-------|-------|
| Foundations | [Time & Space Complexity](concepts/time-space-complexity.html), [Recursion](concepts/recursion.html) |
| Data structures | [Hash Maps & Sets](concepts/hash-map.html), [Linked Lists](concepts/linked-list.html), [Stacks & Monotonic Stacks](concepts/stack.html), [Heaps & Top-K](concepts/heap.html), [Tries](concepts/trie.html) |
| Array & string patterns | [Two Pointers](concepts/two-pointers.html), [Sliding Window](concepts/sliding-window.html), [Fast & Slow Pointers](concepts/fast-slow-pointers.html), [Prefix Sums](concepts/prefix-sum.html), [Cyclic Sort](concepts/cyclic-sort.html), [Binary Search](concepts/binary-search.html), [Merge Intervals](concepts/intervals.html), [Bit Manipulation](concepts/bit-manipulation.html) |
| Recursion, search & optimisation | [Backtracking](concepts/backtracking.html), [Dynamic Programming](concepts/dynamic-programming.html), [Greedy](concepts/greedy.html) |
| Trees & graphs | [Tree Traversal](concepts/tree-traversal.html), [Graph Traversal](concepts/graph-traversal.html), [Topological Sort](concepts/topological-sort.html) |

## Patterns

| Pattern | Problems |
|---------|----------|
| [hash-map](patterns/hash-map.md) · [explained](concepts/hash-map.html) | easy/001, easy/002, medium/001 |
| [hash-set](patterns/hash-set.md) · [explained](concepts/hash-map.html) | easy/003 |
| [stack](patterns/stack.md) · [explained](concepts/stack.html) | easy/004 |
| [sliding-window](patterns/sliding-window.md) · [explained](concepts/sliding-window.html) | easy/005, medium/003 |
| [two-pointers](patterns/two-pointers.md) · [explained](concepts/two-pointers.html) | easy/006, medium/004, medium/005, medium/012 |
| [linked-list](patterns/linked-list.md) · [explained](concepts/linked-list.html) | easy/007, easy/008, medium/006, medium/011 |
| [binary-search](patterns/binary-search.md) · [explained](concepts/binary-search.html) | easy/009 |
| [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | easy/010, medium/007, medium/008 |
| [prefix-sum](patterns/prefix-sum.md) · [explained](concepts/prefix-sum.html) | medium/002 |
| [intervals](patterns/intervals.md) · [explained](concepts/intervals.html) | medium/009 |
| [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | medium/010 |

## Layout

```
index.html                home page with a Concepts / Easy / Medium menu, open in a browser
easy/NNN-slug/
  README.md               statement, examples, constraints
  <slug>.py               clean interview version, e.g. two_sum.py
  <slug>_annotated.py     line-by-line commented version
  test_<slug>.py          plain script, prints PASS/FAIL per case
  notes.md                attempts, sticking points, key insight, complexity
  walkthrough.html        optional: scroll-driven narration of the solution, open in a browser
medium/NNN-slug/          same shape, numbering restarts per difficulty
patterns/<name>.md        when to use it, template code, problems that use it
concepts/<slug>.html      from-scratch explainer per pattern or data structure, open in a browser
templates/problem/        skeleton copied for each new problem (see templates/README.md)
```
