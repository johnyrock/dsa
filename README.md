# DSA Practice

LeetCode-style practice, organized by difficulty and pattern.

## How to use

No dependencies beyond the standard library. Every problem follows the same shape as `practice/src`:
the solution is a `Solution` class with a type-hinted method, `test_<slug>.py` is a `unittest.TestCase`
(one `subTest` per case), and `main.py` is a small demo runner. Run them from inside the folder:

```bash
cd easy/001-two-sum
python3 test_two_sum.py -v
python3 main.py
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
| easy/011 | [Invert Binary Tree](easy/011-invert-binary-tree/) | Easy | [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | - | - | not yet solved |
| easy/012 | [Linked List Cycle](easy/012-linked-list-cycle/) | Easy | [fast-slow-pointers](patterns/fast-slow-pointers.md) · [explained](concepts/fast-slow-pointers.html) | - | - | not yet solved |
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
| medium/013 | [Longest Repeating Character Replacement](medium/013-longest-repeating-character-replacement/) | Medium | [sliding-window](patterns/sliding-window.md) · [explained](concepts/sliding-window.html) | - | - | not yet solved |
| medium/014 | [Binary Tree Level Order Traversal](medium/014-binary-tree-level-order-traversal/) | Medium | [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | - | - | not yet solved |
| medium/015 | [Validate Binary Search Tree](medium/015-validate-binary-search-tree/) | Medium | [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | - | - | not yet solved |
| medium/016 | [Lowest Common Ancestor of a BST](medium/016-lowest-common-ancestor-of-a-bst/) | Medium | [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | - | - | not yet solved |
| medium/017 | [Kth Smallest Element in a BST](medium/017-kth-smallest-element-in-a-bst/) | Medium | [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | - | - | not yet solved |
| medium/018 | [Course Schedule](medium/018-course-schedule/) | Medium | [topological-sort](patterns/topological-sort.md) · [explained](concepts/topological-sort.html) | - | - | not yet solved |
| medium/019 | [Clone Graph](medium/019-clone-graph/) | Medium | [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | - | - | not yet solved |
| medium/020 | [Insert Interval](medium/020-insert-interval/) | Medium | [intervals](patterns/intervals.md) · [explained](concepts/intervals.html) | - | - | not yet solved |
| medium/021 | [Search in Rotated Sorted Array](medium/021-search-in-rotated-sorted-array/) | Medium | [binary-search](patterns/binary-search.md) · [explained](concepts/binary-search.html) | - | - | not yet solved |
| medium/022 | [Random Pick with Weight](medium/022-random-pick-with-weight/) | Medium | [prefix-sum](patterns/prefix-sum.md) · [explained](concepts/prefix-sum.html) | - | - | not yet solved |
| medium/023 | [Serialize and Deserialize Binary Tree](medium/023-serialize-and-deserialize-binary-tree/) | Medium | [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | - | - | not yet solved |
| medium/024 | [Word Container](medium/024-word-container/) | Medium | [trie](patterns/trie.md) · [explained](concepts/trie.html) | - | - | not yet solved |

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
| [sliding-window](patterns/sliding-window.md) · [explained](concepts/sliding-window.html) | easy/005, medium/003, medium/013 |
| [two-pointers](patterns/two-pointers.md) · [explained](concepts/two-pointers.html) | easy/006, medium/004, medium/005, medium/012 |
| [linked-list](patterns/linked-list.md) · [explained](concepts/linked-list.html) | easy/007, easy/008, medium/006, medium/011 |
| [binary-search](patterns/binary-search.md) · [explained](concepts/binary-search.html) | easy/009, medium/021 |
| [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | easy/010, medium/007, medium/008 |
| [prefix-sum](patterns/prefix-sum.md) · [explained](concepts/prefix-sum.html) | medium/002, medium/022 |
| [intervals](patterns/intervals.md) · [explained](concepts/intervals.html) | medium/009, medium/020 |
| [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | medium/010, medium/019 |
| [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | easy/011, medium/014, medium/015, medium/016, medium/017, medium/023 |
| [trie](patterns/trie.md) · [explained](concepts/trie.html) | medium/024 |
| [fast-slow-pointers](patterns/fast-slow-pointers.md) · [explained](concepts/fast-slow-pointers.html) | easy/012 |
| [topological-sort](patterns/topological-sort.md) · [explained](concepts/topological-sort.html) | medium/018 |

## Layout

```
index.html                home page with a Concepts / Easy / Medium menu, open in a browser
easy/NNN-slug/
  README.md               statement, examples, constraints
  <slug>.py               clean interview version: class Solution with a type-hinted method
  <slug>_annotated.py     line-by-line commented version, same shape
  test_<slug>.py          unittest.TestCase, a cases table checked with subTest, run directly
  main.py                 demo runner that imports Solution and prints a few example calls
  notes.md                attempts, sticking points, key insight, complexity
  walkthrough.html        optional: scroll-driven narration of the solution, open in a browser
medium/NNN-slug/          same shape, numbering restarts per difficulty
patterns/<name>.md        when to use it, template code, problems that use it
concepts/<slug>.html      from-scratch explainer per pattern or data structure, open in a browser
templates/problem/        skeleton copied for each new problem (see templates/README.md)
practice/src/             reference for the file structure and coding style (echo.py / tests.py / main.py)
```
