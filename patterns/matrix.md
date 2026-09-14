# Matrix

## When to use

- The input is a 2-D grid and the problem is about *rearranging or marking* it, not searching it (searching is the [graph](graph.md) pattern).
- "In place" or O(1) extra space is requested, so you need a trick to store state inside the grid itself.
- The traversal order is unusual: spiral, diagonal, layer by layer, rotated.

## Templates

**Rotate 90 degrees clockwise = transpose, then reverse each row:**

```python
def rotate(matrix):
    n = len(matrix)
    for r in range(n):
        for c in range(r + 1, n):         # upper triangle only, or you swap back
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    for row in matrix:
        row.reverse()
```

**Spiral order with four shrinking bounds:**

```python
def spiral(matrix):
    out = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):          # top row, left -> right
            out.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):          # right column, top -> bottom
            out.append(matrix[r][right])
        right -= 1
        if top <= bottom:                          # guard: a single row is left
            for c in range(right, left - 1, -1):
                out.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:                          # guard: a single column is left
            for r in range(bottom, top - 1, -1):
                out.append(matrix[r][left])
            left += 1
    return out
```

**Use row 0 and column 0 as marker storage (set matrix zeroes):**

```python
def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
    first_col_zero = any(matrix[r][0] == 0 for r in range(rows))

    for r in range(1, rows):                        # record zeroes in the borders
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    for r in range(1, rows):                        # apply the markers
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    if first_row_zero:                              # borders last, from saved flags
        for c in range(cols):
            matrix[0][c] = 0
    if first_col_zero:
        for r in range(rows):
            matrix[r][0] = 0
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [medium/095 Rotate Image](../medium/095-rotate-image/) | Medium | transpose in the upper triangle, then reverse every row |
| [medium/096 Spiral Matrix](../medium/096-spiral-matrix/) | Medium | four bounds shrink inward; guard the last row and column |
| [medium/097 Set Matrix Zeroes](../medium/097-set-matrix-zeroes/) | Medium | first row / column hold the flags; remember their own state separately |

## Common mistakes

- Transposing over the full square (`for c in range(n)`) so every pair is swapped twice and nothing changes.
- Reversing columns instead of rows after the transpose, which rotates counter-clockwise.
- Spiral loops without the `top <= bottom` / `left <= right` guards; a non-square matrix then repeats the middle row or column.
- Zeroing cells as soon as you see a zero, which cascades and wipes the whole grid. Record first, apply second.
- Overwriting the corner `matrix[0][0]` as both a row flag and a column flag. Keep a separate boolean for at least one of the borders.
- Assuming `rows == cols`; index with `len(matrix)` and `len(matrix[0])` separately.
