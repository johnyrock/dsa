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
| easy/013 | [Maximum Depth of Binary Tree](easy/013-maximum-depth-of-binary-tree/) | Easy | [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | - | - | not yet solved |
| easy/014 | [Diameter of Binary Tree](easy/014-diameter-of-binary-tree/) | Easy | [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | - | - | not yet solved |
| easy/015 | [Balanced Binary Tree](easy/015-balanced-binary-tree/) | Easy | [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | - | - | not yet solved |
| easy/016 | [Same Tree](easy/016-same-tree/) | Easy | [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | - | - | not yet solved |
| easy/017 | [Subtree of Another Tree](easy/017-subtree-of-another-tree/) | Easy | [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | - | - | not yet solved |
| easy/018 | [Kth Largest Element in a Stream](easy/018-kth-largest-element-in-a-stream/) | Easy | [heap](patterns/heap.md) · [explained](concepts/heap.html) | - | - | not yet solved |
| easy/019 | [Last Stone Weight](easy/019-last-stone-weight/) | Easy | [heap](patterns/heap.md) · [explained](concepts/heap.html) | - | - | not yet solved |
| easy/020 | [Min Cost Climbing Stairs](easy/020-min-cost-climbing-stairs/) | Easy | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| easy/021 | [Meeting Rooms](easy/021-meeting-rooms/) | Easy | [intervals](patterns/intervals.md) · [explained](concepts/intervals.html) | - | - | not yet solved |
| easy/022 | [Happy Number](easy/022-happy-number/) | Easy | [fast-slow-pointers](patterns/fast-slow-pointers.md) · [explained](concepts/fast-slow-pointers.html) | - | - | not yet solved |
| easy/023 | [Plus One](easy/023-plus-one/) | Easy | [two-pointers](patterns/two-pointers.md) · [explained](concepts/two-pointers.html) | - | - | not yet solved |
| easy/024 | [Single Number](easy/024-single-number/) | Easy | [bit-manipulation](patterns/bit-manipulation.md) · [explained](concepts/bit-manipulation.html) | - | - | not yet solved |
| easy/025 | [Number of 1 Bits](easy/025-number-of-1-bits/) | Easy | [bit-manipulation](patterns/bit-manipulation.md) · [explained](concepts/bit-manipulation.html) | - | - | not yet solved |
| easy/026 | [Counting Bits](easy/026-counting-bits/) | Easy | [bit-manipulation](patterns/bit-manipulation.md) · [explained](concepts/bit-manipulation.html) | - | - | not yet solved |
| easy/027 | [Reverse Bits](easy/027-reverse-bits/) | Easy | [bit-manipulation](patterns/bit-manipulation.md) · [explained](concepts/bit-manipulation.html) | - | - | not yet solved |
| easy/028 | [Missing Number](easy/028-missing-number/) | Easy | [bit-manipulation](patterns/bit-manipulation.md) · [explained](concepts/bit-manipulation.html) | - | - | not yet solved |
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
| medium/025 | [Top K Frequent Elements](medium/025-top-k-frequent-elements/) | Medium | [heap](patterns/heap.md) · [explained](concepts/heap.html) | - | - | not yet solved |
| medium/026 | [Encode and Decode Strings](medium/026-encode-and-decode-strings/) | Medium | [hash-map](patterns/hash-map.md) · [explained](concepts/hash-map.html) | - | - | not yet solved |
| medium/027 | [Valid Sudoku](medium/027-valid-sudoku/) | Medium | [hash-set](patterns/hash-set.md) · [explained](concepts/hash-map.html) | - | - | not yet solved |
| medium/028 | [Longest Consecutive Sequence](medium/028-longest-consecutive-sequence/) | Medium | [hash-set](patterns/hash-set.md) · [explained](concepts/hash-map.html) | - | - | not yet solved |
| medium/029 | [Two Sum II - Input Array Is Sorted](medium/029-two-sum-ii-input-array-is-sorted/) | Medium | [two-pointers](patterns/two-pointers.md) · [explained](concepts/two-pointers.html) | - | - | not yet solved |
| medium/030 | [Permutation in String](medium/030-permutation-in-string/) | Medium | [sliding-window](patterns/sliding-window.md) · [explained](concepts/sliding-window.html) | - | - | not yet solved |
| medium/031 | [Min Stack](medium/031-min-stack/) | Medium | [stack](patterns/stack.md) · [explained](concepts/stack.html) | - | - | not yet solved |
| medium/032 | [Evaluate Reverse Polish Notation](medium/032-evaluate-reverse-polish-notation/) | Medium | [stack](patterns/stack.md) · [explained](concepts/stack.html) | - | - | not yet solved |
| medium/033 | [Generate Parentheses](medium/033-generate-parentheses/) | Medium | [backtracking](patterns/backtracking.md) · [explained](concepts/backtracking.html) | - | - | not yet solved |
| medium/034 | [Daily Temperatures](medium/034-daily-temperatures/) | Medium | [stack](patterns/stack.md) · [explained](concepts/stack.html) | - | - | not yet solved |
| medium/035 | [Car Fleet](medium/035-car-fleet/) | Medium | [stack](patterns/stack.md) · [explained](concepts/stack.html) | - | - | not yet solved |
| medium/036 | [Search a 2D Matrix](medium/036-search-a-2d-matrix/) | Medium | [binary-search](patterns/binary-search.md) · [explained](concepts/binary-search.html) | - | - | not yet solved |
| medium/037 | [Koko Eating Bananas](medium/037-koko-eating-bananas/) | Medium | [binary-search](patterns/binary-search.md) · [explained](concepts/binary-search.html) | - | - | not yet solved |
| medium/038 | [Find Minimum in Rotated Sorted Array](medium/038-find-minimum-in-rotated-sorted-array/) | Medium | [binary-search](patterns/binary-search.md) · [explained](concepts/binary-search.html) | - | - | not yet solved |
| medium/039 | [Time Based Key-Value Store](medium/039-time-based-key-value-store/) | Medium | [binary-search](patterns/binary-search.md) · [explained](concepts/binary-search.html) | - | - | not yet solved |
| medium/040 | [Reorder List](medium/040-reorder-list/) | Medium | [linked-list](patterns/linked-list.md) · [explained](concepts/linked-list.html) | - | - | not yet solved |
| medium/041 | [Remove Nth Node From End of List](medium/041-remove-nth-node-from-end-of-list/) | Medium | [two-pointers](patterns/two-pointers.md) · [explained](concepts/two-pointers.html) | - | - | not yet solved |
| medium/042 | [Copy List with Random Pointer](medium/042-copy-list-with-random-pointer/) | Medium | [hash-map](patterns/hash-map.md) · [explained](concepts/hash-map.html) | - | - | not yet solved |
| medium/043 | [Find the Duplicate Number](medium/043-find-the-duplicate-number/) | Medium | [fast-slow-pointers](patterns/fast-slow-pointers.md) · [explained](concepts/fast-slow-pointers.html) | - | - | not yet solved |
| medium/044 | [Binary Tree Right Side View](medium/044-binary-tree-right-side-view/) | Medium | [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | - | - | not yet solved |
| medium/045 | [Count Good Nodes in Binary Tree](medium/045-count-good-nodes-in-binary-tree/) | Medium | [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | - | - | not yet solved |
| medium/046 | [Construct Binary Tree from Preorder and Inorder Traversal](medium/046-construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | - | - | not yet solved |
| medium/047 | [Implement Trie (Prefix Tree)](medium/047-implement-trie-prefix-tree/) | Medium | [trie](patterns/trie.md) · [explained](concepts/trie.html) | - | - | not yet solved |
| medium/048 | [Design Add and Search Words Data Structure](medium/048-design-add-and-search-words-data-structure/) | Medium | [trie](patterns/trie.md) · [explained](concepts/trie.html) | - | - | not yet solved |
| medium/049 | [K Closest Points to Origin](medium/049-k-closest-points-to-origin/) | Medium | [heap](patterns/heap.md) · [explained](concepts/heap.html) | - | - | not yet solved |
| medium/050 | [Kth Largest Element in an Array](medium/050-kth-largest-element-in-an-array/) | Medium | [heap](patterns/heap.md) · [explained](concepts/heap.html) | - | - | not yet solved |
| medium/051 | [Task Scheduler](medium/051-task-scheduler/) | Medium | [heap](patterns/heap.md) · [explained](concepts/heap.html) | - | - | not yet solved |
| medium/052 | [Design Twitter](medium/052-design-twitter/) | Medium | [heap](patterns/heap.md) · [explained](concepts/heap.html) | - | - | not yet solved |
| medium/053 | [Subsets](medium/053-subsets/) | Medium | [backtracking](patterns/backtracking.md) · [explained](concepts/backtracking.html) | - | - | not yet solved |
| medium/054 | [Combination Sum](medium/054-combination-sum/) | Medium | [backtracking](patterns/backtracking.md) · [explained](concepts/backtracking.html) | - | - | not yet solved |
| medium/055 | [Permutations](medium/055-permutations/) | Medium | [backtracking](patterns/backtracking.md) · [explained](concepts/backtracking.html) | - | - | not yet solved |
| medium/056 | [Subsets II](medium/056-subsets-ii/) | Medium | [backtracking](patterns/backtracking.md) · [explained](concepts/backtracking.html) | - | - | not yet solved |
| medium/057 | [Combination Sum II](medium/057-combination-sum-ii/) | Medium | [backtracking](patterns/backtracking.md) · [explained](concepts/backtracking.html) | - | - | not yet solved |
| medium/058 | [Word Search](medium/058-word-search/) | Medium | [backtracking](patterns/backtracking.md) · [explained](concepts/backtracking.html) | - | - | not yet solved |
| medium/059 | [Palindrome Partitioning](medium/059-palindrome-partitioning/) | Medium | [backtracking](patterns/backtracking.md) · [explained](concepts/backtracking.html) | - | - | not yet solved |
| medium/060 | [Letter Combinations of a Phone Number](medium/060-letter-combinations-of-a-phone-number/) | Medium | [backtracking](patterns/backtracking.md) · [explained](concepts/backtracking.html) | - | - | not yet solved |
| medium/061 | [Max Area of Island](medium/061-max-area-of-island/) | Medium | [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | - | - | not yet solved |
| medium/062 | [Walls and Gates](medium/062-walls-and-gates/) | Medium | [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | - | - | not yet solved |
| medium/063 | [Rotting Oranges](medium/063-rotting-oranges/) | Medium | [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | - | - | not yet solved |
| medium/064 | [Pacific Atlantic Water Flow](medium/064-pacific-atlantic-water-flow/) | Medium | [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | - | - | not yet solved |
| medium/065 | [Surrounded Regions](medium/065-surrounded-regions/) | Medium | [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | - | - | not yet solved |
| medium/066 | [Course Schedule II](medium/066-course-schedule-ii/) | Medium | [topological-sort](patterns/topological-sort.md) · [explained](concepts/topological-sort.html) | - | - | not yet solved |
| medium/067 | [Graph Valid Tree](medium/067-graph-valid-tree/) | Medium | [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | - | - | not yet solved |
| medium/068 | [Number of Connected Components in an Undirected Graph](medium/068-number-of-connected-components-in-an-undirected-graph/) | Medium | [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | - | - | not yet solved |
| medium/069 | [Redundant Connection](medium/069-redundant-connection/) | Medium | [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | - | - | not yet solved |
| medium/070 | [Network Delay Time](medium/070-network-delay-time/) | Medium | [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | - | - | not yet solved |
| medium/071 | [Min Cost to Connect All Points](medium/071-min-cost-to-connect-all-points/) | Medium | [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | - | - | not yet solved |
| medium/072 | [House Robber](medium/072-house-robber/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/073 | [House Robber II](medium/073-house-robber-ii/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/074 | [Palindromic Substrings](medium/074-palindromic-substrings/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/075 | [Decode Ways](medium/075-decode-ways/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/076 | [Maximum Product Subarray](medium/076-maximum-product-subarray/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/077 | [Word Break](medium/077-word-break/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/078 | [Longest Increasing Subsequence](medium/078-longest-increasing-subsequence/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/079 | [Partition Equal Subset Sum](medium/079-partition-equal-subset-sum/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/080 | [Unique Paths](medium/080-unique-paths/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/081 | [Longest Common Subsequence](medium/081-longest-common-subsequence/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/082 | [Best Time to Buy and Sell Stock with Cooldown](medium/082-best-time-to-buy-and-sell-stock-with-cooldown/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/083 | [Coin Change II](medium/083-coin-change-ii/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/084 | [Target Sum](medium/084-target-sum/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/086 | [Jump Game](medium/086-jump-game/) | Medium | [greedy](patterns/greedy.md) · [explained](concepts/greedy.html) | - | - | not yet solved |
| medium/087 | [Jump Game II](medium/087-jump-game-ii/) | Medium | [greedy](patterns/greedy.md) · [explained](concepts/greedy.html) | - | - | not yet solved |
| medium/088 | [Gas Station](medium/088-gas-station/) | Medium | [greedy](patterns/greedy.md) · [explained](concepts/greedy.html) | - | - | not yet solved |
| medium/089 | [Hand of Straights](medium/089-hand-of-straights/) | Medium | [greedy](patterns/greedy.md) · [explained](concepts/greedy.html) | - | - | not yet solved |
| medium/090 | [Merge Triplets to Form Target Triplet](medium/090-merge-triplets-to-form-target-triplet/) | Medium | [greedy](patterns/greedy.md) · [explained](concepts/greedy.html) | - | - | not yet solved |
| medium/091 | [Partition Labels](medium/091-partition-labels/) | Medium | [greedy](patterns/greedy.md) · [explained](concepts/greedy.html) | - | - | not yet solved |
| medium/092 | [Valid Parenthesis String](medium/092-valid-parenthesis-string/) | Medium | [greedy](patterns/greedy.md) · [explained](concepts/greedy.html) | - | - | not yet solved |
| medium/093 | [Non-overlapping Intervals](medium/093-non-overlapping-intervals/) | Medium | [intervals](patterns/intervals.md) · [explained](concepts/intervals.html) | - | - | not yet solved |
| medium/095 | [Rotate Image](medium/095-rotate-image/) | Medium | [matrix](patterns/matrix.md) · [explained](concepts/matrix.html) | - | - | not yet solved |
| medium/096 | [Spiral Matrix](medium/096-spiral-matrix/) | Medium | [matrix](patterns/matrix.md) · [explained](concepts/matrix.html) | - | - | not yet solved |
| medium/097 | [Set Matrix Zeroes](medium/097-set-matrix-zeroes/) | Medium | [matrix](patterns/matrix.md) · [explained](concepts/matrix.html) | - | - | not yet solved |
| medium/099 | [Multiply Strings](medium/099-multiply-strings/) | Medium | [math](patterns/math.md) · [explained](concepts/math.html) | - | - | not yet solved |
| medium/100 | [Detect Squares](medium/100-detect-squares/) | Medium | [hash-map](patterns/hash-map.md) · [explained](concepts/hash-map.html) | - | - | not yet solved |
| medium/101 | [Sum of Two Integers](medium/101-sum-of-two-integers/) | Medium | [bit-manipulation](patterns/bit-manipulation.md) · [explained](concepts/bit-manipulation.html) | - | - | not yet solved |
| medium/085 | [Interleaving String](medium/085-interleaving-string/) | Medium | [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | - | - | not yet solved |
| medium/094 | [Meeting Rooms II](medium/094-meeting-rooms-ii/) | Medium | [intervals](patterns/intervals.md) · [explained](concepts/intervals.html) | - | - | not yet solved |
| medium/098 | [Pow(x, n)](medium/098-powx-n/) | Medium | [math](patterns/math.md) · [explained](concepts/math.html) | - | - | not yet solved |
| medium/102 | [Reverse Integer](medium/102-reverse-integer/) | Medium | [math](patterns/math.md) · [explained](concepts/math.html) | - | - | not yet solved |
| medium/103 | [String Compression III](medium/103-string-compression-iii/) | Medium | [two-pointers](patterns/two-pointers.md) · [explained](concepts/two-pointers.html) | - | - | not yet solved |

## Due for review

_(Problems whose next review date has passed. Updated at the start of each session.)_

- none yet

## Concepts

Beginner explainers under `concepts/`, one per pattern. Suggested reading order, top to bottom.

| Group | Pages |
|-------|-------|
| Foundations | [Time & Space Complexity](concepts/time-space-complexity.html), [Recursion](concepts/recursion.html) |
| Data structures | [Hash Maps & Sets](concepts/hash-map.html), [Linked Lists](concepts/linked-list.html), [Stacks & Monotonic Stacks](concepts/stack.html), [Heaps & Top-K](concepts/heap.html), [Tries](concepts/trie.html) |
| Array & string patterns | [Two Pointers](concepts/two-pointers.html), [Sliding Window](concepts/sliding-window.html), [Fast & Slow Pointers](concepts/fast-slow-pointers.html), [Prefix Sums](concepts/prefix-sum.html), [Cyclic Sort](concepts/cyclic-sort.html), [Binary Search](concepts/binary-search.html), [Merge Intervals](concepts/intervals.html), [Bit Manipulation](concepts/bit-manipulation.html), [Matrix Manipulation](concepts/matrix.html), [Math Tricks](concepts/math.html) |
| Recursion, search & optimisation | [Backtracking](concepts/backtracking.html), [Dynamic Programming](concepts/dynamic-programming.html), [Greedy](concepts/greedy.html) |
| Trees & graphs | [Tree Traversal](concepts/tree-traversal.html), [Graph Traversal](concepts/graph-traversal.html), [Topological Sort](concepts/topological-sort.html) |

## Patterns

| Pattern | Problems |
|---------|----------|
| [hash-map](patterns/hash-map.md) · [explained](concepts/hash-map.html) | easy/001, easy/002, medium/001, medium/026, medium/042, medium/100 |
| [hash-set](patterns/hash-set.md) · [explained](concepts/hash-map.html) | easy/003, medium/027, medium/028 |
| [stack](patterns/stack.md) · [explained](concepts/stack.html) | easy/004, medium/031, medium/032, medium/034, medium/035 |
| [sliding-window](patterns/sliding-window.md) · [explained](concepts/sliding-window.html) | easy/005, medium/003, medium/013, medium/030 |
| [two-pointers](patterns/two-pointers.md) · [explained](concepts/two-pointers.html) | easy/006, medium/004, medium/005, medium/012, easy/023, medium/029, medium/041, medium/103 |
| [linked-list](patterns/linked-list.md) · [explained](concepts/linked-list.html) | easy/007, easy/008, medium/006, medium/011, medium/040 |
| [binary-search](patterns/binary-search.md) · [explained](concepts/binary-search.html) | easy/009, medium/021, medium/036, medium/037, medium/038, medium/039 |
| [dynamic-programming](patterns/dynamic-programming.md) · [explained](concepts/dynamic-programming.html) | easy/010, medium/007, medium/008, easy/020, medium/072, medium/073, medium/074, medium/075, medium/076, medium/077, medium/078, medium/079, medium/080, medium/081, medium/082, medium/083, medium/084, medium/085 |
| [prefix-sum](patterns/prefix-sum.md) · [explained](concepts/prefix-sum.html) | medium/002, medium/022 |
| [intervals](patterns/intervals.md) · [explained](concepts/intervals.html) | medium/009, medium/020, easy/021, medium/093, medium/094 |
| [graph](patterns/graph.md) · [explained](concepts/graph-traversal.html) | medium/010, medium/019, medium/061, medium/062, medium/063, medium/064, medium/065, medium/067, medium/068, medium/069, medium/070, medium/071 |
| [tree](patterns/tree.md) · [explained](concepts/tree-traversal.html) | easy/011, medium/014, medium/015, medium/016, medium/017, medium/023, easy/013, easy/014, easy/015, easy/016, easy/017, medium/044, medium/045, medium/046 |
| [trie](patterns/trie.md) · [explained](concepts/trie.html) | medium/024, medium/047, medium/048 |
| [fast-slow-pointers](patterns/fast-slow-pointers.md) · [explained](concepts/fast-slow-pointers.html) | easy/012, easy/022, medium/043 |
| [topological-sort](patterns/topological-sort.md) · [explained](concepts/topological-sort.html) | medium/018, medium/066 |
| [heap](patterns/heap.md) · [explained](concepts/heap.html) | easy/018, easy/019, medium/025, medium/049, medium/050, medium/051, medium/052 |
| [bit-manipulation](patterns/bit-manipulation.md) · [explained](concepts/bit-manipulation.html) | easy/024, easy/025, easy/026, easy/027, easy/028, medium/101 |
| [backtracking](patterns/backtracking.md) · [explained](concepts/backtracking.html) | medium/033, medium/053, medium/054, medium/055, medium/056, medium/057, medium/058, medium/059, medium/060 |
| [greedy](patterns/greedy.md) · [explained](concepts/greedy.html) | medium/086, medium/087, medium/088, medium/089, medium/090, medium/091, medium/092 |
| [matrix](patterns/matrix.md) · [explained](concepts/matrix.html) | medium/095, medium/096, medium/097 |
| [math](patterns/math.md) · [explained](concepts/math.html) | medium/099, medium/098, medium/102 |

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
