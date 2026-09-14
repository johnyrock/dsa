# 058. Word Search

**Difficulty:** Medium | **Pattern:** [backtracking](../../patterns/backtracking.md) ([explained](../../concepts/backtracking.html)) | **Source:** LeetCode #79

## Problem

Given an `m x n` grid of characters `board` and a string `word`, decide whether `word` can be spelled by walking through the grid: start at any cell, and each next letter must come from a cell that is horizontally or vertically adjacent to the previous one. A cell may be used at most once in a single spelling.

Return `true` if such a path exists, `false` otherwise.

## Examples

```
Input:  board = [["A","B","C","E"],
                 ["S","F","C","S"],
                 ["A","D","E","E"]], word = "ABCCED"
Output: true          # (0,0) A → (0,1) B → (0,2) C → (1,2) C → (2,2) E → (2,1) D

Input:  board = same, word = "SEE"
Output: true          # (1,3) S → (2,3) E → (2,2) E; the S at (1,0) has no E beside it

Input:  board = same, word = "ABCB"
Output: false         # the only B is at (0,1), and it was already used for the second letter
```

## Constraints

- `m == board.length`, `n == board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consist of only lowercase and uppercase English letters

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from enumerating every path to a depth-first search that marks cells in place and unmarks them on the way back, with complexity.

## Follow-up

- Word Search II (LeetCode #212) asks for every word from a list of up to 30,000 that appears on the board. Why does running this search once per word blow up, and what structure lets one DFS serve all words at once?
- Before searching, count the letters on the board and in the word. Which cheap check lets you return `false` without any DFS, and when is it worth reversing the word first?
- What changes if a cell may be reused (no marking)? Which of the three examples flips its answer?
