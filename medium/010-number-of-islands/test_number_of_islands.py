from number_of_islands import num_islands


def make_grid(rows):
    # Build a fresh list-of-lists grid from strings so each case gets its own copy.
    return [list(row) for row in rows]


def test_num_islands():
    cases = [
        # (rows, expected)
        (["11000",
          "11000",
          "00100",
          "00011"], 3),
        (["111",
          "010",
          "111"], 1),                    # connected through the middle
        (["0"], 0),                      # single water cell
        (["1"], 1),                      # single land cell
        (["11111"], 1),                  # one row
        (["1", "0", "1", "0", "1"], 3),  # one column
        (["10101",
          "01010",
          "10101"], 8),                  # checkerboard: diagonals do not connect
        (["1111",
          "1001",
          "1001",
          "1111"], 1),                   # ring around water
        (["0000",
          "0000"], 0),                   # all water
        (["1100",
          "1100",
          "0011",
          "0011"], 2),                   # two blocks touching only at a corner
        (["1" * 300] * 300, 1),          # upper bound, one giant island (would overflow naive recursion)
    ]

    failures = 0
    for rows, expected in cases:
        result = num_islands(make_grid(rows))
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        shown = rows if len(rows) < 20 else f"[{len(rows)}x{len(rows[0])} all land]"
        print(f"{status}  grid={shown} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_num_islands()
